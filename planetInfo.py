#individual planet info screen

import sriCalculation as e
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime
import os

#global veriables
planetData = []
secWindow = "" 

#method for planets' information
def planetInfo(planet, numDays, primaryWindow):
    planetData = fileReader(planet)

    minimumSRI = 0
    maximumSRI = 0
    cumulativeSRI = 0
    averageSRI = 0 
    cumulativeDistance = 0
    averageDistance = 0

    for i in range(numDays):
        sri = e.calculateSolarIntensity(planetData[i][2]) 
        cumulativeDistance+= float(planetData[i][2])
        if i == 0:
            minimumSRI = sri
    
        if sri < minimumSRI:
            minimumSRI = sri

        if sri > maximumSRI:
            maximumSRI = sri
        cumulativeSRI += sri

    averageSRI = cumulativeSRI / numDays
    averageDistance = cumulativeDistance/numDays

    print(str(averageSRI))
    print(str(cumulativeSRI))
    print(str(averageDistance))

    #setting date to current date
    dateCurrent = datetime.now()
    format = '%m-%d-%Y'
    formattedDate = dateCurrent.strftime(format)

    secondaryWindow = tk.Tk()
    secondaryWindow.title("Planet Information")
    secondaryWindow.geometry('1400x800')

    #name of planet
    planetNameLabel = tk.Label(secondaryWindow, text = planet.upper(), font = ('Helvetica bold', 70))
    planetNameLabel.place(x=50,y=50)
    
    #date
    dateLabel = tk.Label(secondaryWindow, text= "Enter a date -- Ex: 01-01-2024", font=("Helvetica bold", 20))
    dateLabel.place(x=60, y=200)

    dateEntry = tk.Entry(secondaryWindow, font=("Helvetica bold", 20))
    dateEntry.insert(0, formattedDate)
    enterDatebttn = tk.Button(secondaryWindow, text="Enter", command=lambda: dateButtonClicked(dateEntry, distanceTEResultLabel, distanceTSResultLabel, solarIrridanceResult, planetData, font=("Helvetica bold", 20)))

    dateEntry.place(x=90,y=250)
    enterDatebttn.place(x=160,y=300)

    d1 = datetime.strptime(formattedDate, '%m-%d-%Y')
    d2 = datetime.strptime(planetData[0][0], '%m/%d/%y')

    #calculating the number of days it has been since inputted date
    delta = d1-d2

    print('Difference is ' + str(delta.days) + ' days')


    distanceToEarthLabel = tk.Label(secondaryWindow, text= "Distance from Earth (au): ", font= ("Helvetica bold", 17))
    distanceToEarthLabel.place(x=530, y=100)

    distanceTEResultLabel = tk.Label(secondaryWindow, text = planetData[delta.days][1], font= ("Helvetica bold", 16))
    distanceTEResultLabel.place(x=590, y=128)

    distanceToSunLabel = tk.Label(secondaryWindow, text= "Distance from the Sun (au): ", font= ("Helvetica bold", 17))
    distanceToSunLabel.place(x=1100, y=100)

    distanceTSResultLabel = tk.Label(secondaryWindow, text = planetData[delta.days][2], font= ("Helvetica bold", 16))
    distanceTSResultLabel.place(x=1168,y=128)

    solarIrridaiance = e.calculateSolarIntensitySN(planetData[delta.days][2])
    solarIrridanceLabel = tk.Label(secondaryWindow, text = "Solar Irridance of " + planet.capitalize() + " (W/m^2): ", font= ("Helvetica bold", 17))
    solarIrridanceLabel.place(x=530, y=250)

    solarIrridanceResult = tk.Label(secondaryWindow, text= solarIrridaiance, font= ("Helvetica bold", 16))
    solarIrridanceResult.place(x=620, y=280)

    solarIrridanceLabel = tk.Label(secondaryWindow, text = "Average Solar Radiation Intensity of " + planet.capitalize() + " (W/m^2): ", font= ("Helvetica bold", 17))
    solarIrridanceLabel.place(x=900, y=250)

    averageSRIResult = tk.Label(secondaryWindow, text= f"{averageSRI:.2f}", font= ("Helvetica bold", 16))
    averageSRIResult.place(x=1060, y=280)

    averageSRILabel = tk.Label(secondaryWindow, text = "Cumulative Solar Radiation Intensity of " + planet.capitalize() + " (W/m^2): ", font= ("Helvetica bold", 17))
    averageSRILabel.place(x=665, y=350)

    averageSRIResult = tk.Label(secondaryWindow, text= f"{cumulativeSRI:.2f}", font= ("Helvetica bold", 16))
    averageSRIResult.place(x=845, y=386)

    averageDistanceLabel = tk.Label(secondaryWindow, text = "Average Distance to Sun (au): ", font= ("Helvetica bold", 17))
    averageDistanceLabel.place(x=760, y=450)

    averageSRIResult = tk.Label(secondaryWindow, text= f"{averageDistance:.2f}", font= ("Helvetica bold", 16))
    averageSRIResult.place(x=860, y=480)


    secondaryWindow.mainloop()

#method to read file
def fileReader(planet):
    local = []
    planetFile = open("files/" + planet + ".csv", "r")
    planetData = planetFile.read()

    listOfPlanets = planetData.split("\n")

    for data in listOfPlanets:
        local.append(data.split(","))

    local.pop(0)
    print(local)
    
    planetFile.close()
    return local

#button event
def dateButtonClicked(dateEntry, distanceTEResultLabel, distanceTSResultLabel, solarIrridanceResult, planetData, font):

    enteredDate = dateEntry.get()
    d1 = datetime.strptime(enteredDate, '%m-%d-%Y')

    for data in planetData:
        d2 = datetime.strptime(data[0], '%m/%d/%y')
        if d2 == d1:
            distanceTEResultLabel.config(text=data[1])
            distanceTSResultLabel.config(text=data[2])
            solarIrridance = e.calculateSolarIntensitySN(data[2])
            solarIrridanceResult.config(text=solarIrridance + " W/m^2")
            break
    else:
        print('Enter a valid date: 01-01-24 to 12-31-26')
