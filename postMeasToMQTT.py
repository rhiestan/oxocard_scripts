uri = "mqtt://192.168.1.xx"
username = ""
password = ""

publishTopic = "oxocard/meas/"

connectMQTT(uri, username, password)

backlight(0)
setInterval(10000)
#setTimer(1000)


def updateValue(publishTopic: byte[], valueName: byte[], value: float)
    body = "" + value
    publishMQTT(publishTopic + valueName, body)

def onClick():
	if getButton():
		if returnToMenu():
			return

def onTimer():
    systemTime:long = getSystemTime()
    sensorValue:float = getTemperature()
    if sensorValue != -5.0:
        updateValue(url, "virtualOxocardTemperature", sensorValue)
    sensorValue = getHumidity()
    if sensorValue > 0:
        updateValue(url, "virtualOxocardHumidity", sensorValue)
    sensorValue = getCO2()
    if sensorValue != -1.0:
        updateValue(url, "virtualOxocardCO2", sensorValue)
    sensorValue = getVOCIndex()
    if sensorValue != -1.0:
        updateValue(url, "virtualOxocardVOCIndex", sensorValue)
    sensorValue = getNOxIndex()
    if sensorValue != -1.0:
        updateValue(url, "virtualOxocardNOxIndex", sensorValue)
    sensorValue = getIAQ()
    if sensorValue != -1.0:
        updateValue(url, "virtualOxocardIAQ", sensorValue)
    updateValue(url, "virtualOxocardPressure", getPressure())
    updateValue(url, "virtualOxocardAmbientLux", getAmbientLux())
    updateValue(url, "virtualOxocardAmbientIR", getAmbientIR())
    updateValue(url, "virtualOxocardMicrophoneDecibel", getMicrophoneDecibel())

    # Reboot every 24h
    secondsSinceBoot:long = systemTime / 1000000
    hoursSinceBoot:long = secondsSinceBoot / 3600
    if hoursSinceBoot > 24:
        restart()
