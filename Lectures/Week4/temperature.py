#Read twelve temperature values (one for each)
#month), and display the # of the month w/
#the highest temperature.

#Example list of temperatures:
#18.2 22.6 26.4 31.1 36.6 42.2
#45.7 44.5 40.2 33.1 24.2 17.6
#Highest is the 7th number, ie. 45.7

#temperatureList = [18.2, 22.6, 26.4, 31.1,
#                   36.6, 42.2, 45.7, 44.5
#                   40.2, 33.1, 24.2, 17.6]
#highestTemp = 0
#for number in temperature:
#   if number > highestTemp:
#       highestTemp = number
#print(f"The month with the highest temperature is {highestTemp}")

temperatureList = [18.2, 22.6, 26.4, 31.1,36.6, 42.2, 45.7, 44.5, 40.2, 33.1, 24.2, 17.6]
highestTemp = 0
highestTempIndex = 0
for i in range(0, len(temperatureList)):
   currenTemp = temperatureList[i]
   if  currenTemp > highestTemp:
       highestTemp = currenTemp
       highestTempIndex = i
print(f"The month with the highest temperature ({highestTemp}) is {highestTempIndex + 1}")