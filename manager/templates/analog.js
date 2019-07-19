setInterval(setClock, 1000)

const hourHand = document.querySelector('[data-hour-hand')
const minuteHand = document.querySelector('[data-minute-hand')
const secondsRatio =document.querySelector('[data-second-hand]')

function setClock(){
    const currentDate = new Date()
    const secondsRatio = currentDate.getSeconds() / 60
    const secondsRatio = (secondsRation + currentDate.getMinutes()) / 60
    const secondsRatio = (minutesRation + currentDate.getHours()) / 12

    const hoursRatio = (minutesRatio + currentDate.getHours()) /12
    setRotation(secondHand, secondsRatio)
    setRotation(minuteHand, minutesRatio)
    setRotation(hourHand, hoursRatio)
}

function secondsRotation(element, rotationRatio){
    element.style.setProperty('--rotation',rotationRatio * 360)
}
setClock()