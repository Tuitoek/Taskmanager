# threads.py -- example of multiple threads using psycopg
# -*- encoding: latin1 -*-
#
# Copyright (C) 2001-2004 Federico Di Gregorio  <fog@debian.org>
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by the
# Free Software Foundation; either version 2, or (at your option) any later
# version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTIBILITY
# or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU General Public License
# for more details.

## put in DSN your DSN string

DSN = 'dbname=test'

## some others parameters
INSERT_THREADS = ('A', 'B', 'C')
SELECT_THREADS = ('1', '2')

ROWS = 1000

COMMIT_STEP = 20
SELECT_SIZE = 10000
SELECT_STEP = 500
SELECT_DIV  = 250

# the available modes are:
# 0 - one connection for all insert and one for all select threads
# 1 - connections generated using the connection pool

MODE = 1

## don't modify anything below tis line (except for experimenting)

import sys, psycopg2, threading
from psycopg2.pool import ThreadedConnectionPool

if len(sys.argv) > 1:
    DSN = sys.argv[1]
if len(sys.argv) > 2:
    MODE = int(sys.argv[2])
    
print "Opening connection using dns:", DSN
conn = psycopg2.connect(DSN)
curs = conn.cursor()

try:
    curs.execute("""CREATE TABLE test_threads (
                        name text, value1 int4, value2 float)""")
except:
    conn.rollback()
    curs.execute("DROP TABLE test_threads")
    curs.execute("""CREATE TABLE test_threads (
                        name text, value1 int4, value2 float)""")
conn.commit()


## this function inserts a big number of rows and creates and destroys
## a large number of cursors

def insert_func(conn_or_pool, rows):
    name = threading.currentThread().getName()

    if MODE == 0:
        conn = conn_or_pool
    else:
        conn = conn_or_pool.getconn()
        
    for i in range(rows):
        if divmod(i, COMMIT_STEP)[1] == 0:
            conn.commit()
            if MODE == 1:
                conn_or_pool.putconn(conn)
            s = name + ": COMMIT STEP " + str(i)
            print s
            if MODE == 1:
                conn = conn_or_pool.getconn()
        c = conn.cursor()
        try:
            c.execute("INSERT INTO test_threads VALUES (%s, %s, %s)",
                      (str(i), i, float(i)))
        except psycopg2.ProgrammingError, err:
            print name, ": an error occurred; skipping this insert"
            print err
    conn.commit()

## a nice select function that prints the current number of rows in the
## database (and transefer them, putting some pressure on the network)
    
def select_func(conn_or_pool, z):
    name = threading.currentThread().getName()

    if MODE == 0:
        conn = conn_or_pool
        conn.set_isolation_level(0)
    
    for i in range(SELECT_SIZE):
        if divmod(i, SELECT_STEP)[1] == 0:
            try:
                if MODE == 1:
                    conn = conn_or_pool.getconn()
                    conn.set_isolation_level(0)
                c = conn.cursor()
                c.execute("SELECT * FROM test_threads WHERE value2 < %s",
                          (int(i/z),))
                l = c.fetchall()
                if MODE == 1:
                    conn_or_pool.putconn(conn)
                s = name + ": number of rows fetched: " + str(len(l))
                print s
            except psycopg2.ProgrammingError, err:
                print name, ": an error occurred; skipping this select"
                print err

## create the connection pool or the connections
if MODE == 0:
    conn_insert = psycopg2.connect(DSN)
    conn_select = psycopg2.connect(DSN)
else:
    m = len(INSERT_THREADS) + len(SELECT_THREADS)
    n = m/2
    conn_insert = conn_select = ThreadedConnectionPool(n, m, DSN)
    
## create the threads
threads = []

print "Creating INSERT threads:"
for name in INSERT_THREADS:
    t = threading.Thread(None, insert_func, 'Thread-'+name,
                         (conn_insert, ROWS))
    t.setDaemon(0)
    threads.append(t)

print "Creating SELECT threads:"
for name in SELECT_THREADS:
    t = threading.Thread(None, select_func, 'Thread-'+name,
                         (conn_select, SELECT_DIV))
    t.setDaemon(0)
    threads.append(t)

## really start the threads now
for t in threads:
    t.start()

# and wait for them to finish
for t in threads:
    t.join()
    print t.getName(), "exited OK"


conn.commit()
curs.execute("SELECT count(name) FROM test_threads")
print "Inserted", curs.fetchone()[0], "rows."

curs.execute("DROP TABLE test_threads")
conn.commit()
