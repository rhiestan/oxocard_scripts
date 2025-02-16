url = "http://192.168.1.28:8080"
backlight(0)
clearRequestHeaders()
addRequestHeader("Content-Type", "text/plain")
addRequestHeader("Accept", "application/json")
setAutostart(true)
setInterval(10000)
#setTimer(1000)

def updateValue(url: byte[], valueName: byte[], value: float)
    fullURL = url + "/rest/items/" + valueName
    body = "" + value
    postRequest(fullURL, body)

def onClick():
	if getButton():
		if returnToMenu():
			return

def onTimer():
    sensorValue:float = getTemperature()
    if(sensorValue != -5.0)
        updateValue(url, "virtualOxocardTemperature", sensorValue)
    sensorValue = getHumidity()
    if(sensorValue > 0)
        updateValue(url, "virtualOxocardHumidity", sensorValue)
    sensorValue = getCO2()
    if(sensorValue != -1.0)
        updateValue(url, "virtualOxocardCO2", sensorValue)
    sensorValue = getVOCIndex()
    if(sensorValue != -1.0)
        updateValue(url, "virtualOxocardVOCIndex", sensorValue)
    sensorValue = getNOxIndex()
    if(sensorValue != -1.0)
        updateValue(url, "virtualOxocardNOxIndex", sensorValue)
    sensorValue = getIAQ()
    if(sensorValue != -1.0)
        updateValue(url, "virtualOxocardIAQ", sensorValue)
    updateValue(url, "virtualOxocardPressure", getPressure())
    updateValue(url, "virtualOxocardAmbientLux", getAmbientLux())
    updateValue(url, "virtualOxocardAmbientIR", getAmbientIR())
    updateValue(url, "virtualOxocardMicrophoneDecibel", getMicrophoneDecibel())
