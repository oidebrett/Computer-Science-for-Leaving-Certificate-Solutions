#Tasks on page 18
"""Task 2 Sum difference and product"""
num1 = float(10)
num2 = float(5)
print ("Sum:",num1+num2, "Difference:", num1-num2, "Product:", num1*num2)

#Task 3
print("Average:", (num1+num2)/2,"Remainder or Modulus:", num1%num2, "To the power of:", num1**num2)

#Tasks on page 19

#Task 4 temp conversion
chicagoTemp = int(87)
celsiusTemp = ((5/9)*(chicagoTemp-32))
answer = round(celsiusTemp)
print (answer)

#Task 5 fly to singapore
distanceKm = int(7136*1.60935)
cost = (900*distanceKm)
print (cost)

#Task 6 Water cylinder
h=10
r=5
pi=3.14
vol = (pi*r**2)*h
#print("Volume:", vol)
totalLiquid = 10000
numCylinders= round(totalLiquid/vol)
print ("Number of cylinders:",numCylinders)

#my version with user input
"""
print("Hi lets calculate cylinders")
h = int(input("Enter Height:"))
r= int(input("Enter radius"))
print ("ok your cylinder will hold:", vol,"litres")
totalLiquid = int(input("Enter the amount of liquid you need to carry:"))
print ("ok you will need:" ,round(totalLiquid/vol),"cylinders")
"""

#Task 7 weight on earth / moon

weightMoon = (75/100)*16.5
print ("Weight on moon:", weightMoon)

#TASK 8 working out lawn mowing
lGarden = 75
wGarden = 55
areaGarden = (lGarden*wGarden)
lHouse = 15
wHouse = 12
areaHouse = (lHouse*wHouse)
#take away house from Garden
areaLeft = (areaGarden-areaHouse)
cuttingTime = round((areaLeft/2)/60, 2)
print ("It will take:", cuttingTime,"minutes to cut grass with an area of", areaLeft,"sq metres")



"""
inputs always calculate as a string so you need to convert to
int if you want a number input
"""
yachtPrice=int(input("Enter number of nights:"))*257
print(yachtPrice)
