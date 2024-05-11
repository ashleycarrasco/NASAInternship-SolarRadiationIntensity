#calculation for solar radiation intensity

def calculateSolarIntensity(distance):
    #constants
    radiusSun = 695e6
    radiantSolarIntensity = 64e6

    #chaning distance from string to float
    distanceFloat = float(distance)

    #changing distance units from au to meters
    distanceInMeters =  distanceFloat * 1.496e11
    
    #calculating the solar intensity
    solarIntensity = (((radiusSun**2)/(distanceInMeters)**2) * radiantSolarIntensity)


    resultInScientificNotation = "{: .{}f} * 10^{}".format((solarIntensity / 1e14), 10, 14)

    return solarIntensity

#method in scientific notation
def calculateSolarIntensitySN(distance):
    #constants
    raduisSun = 695e6
    radiantSolarInensity = 64e6

    #chaning distance from string to float
    distanceFloat = float(distance)

    #changing distance units from a.u. to meters
    distanceInMeters =  distanceFloat * 1.496e11
    
    #calculating the solar intensity
    solarInensity = (raduisSun**2/distanceInMeters**2) * radiantSolarInensity

    resultInScientificNotation = "%.2f"% solarInensity

    print(resultInScientificNotation)
    return resultInScientificNotation