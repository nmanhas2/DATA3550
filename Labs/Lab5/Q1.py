#Q1
#Ask for height in cm, weight in kg
#calculate BMI
#Categories:

#Underweight < 18.5
#Healthy weight 18.5-24.9
#Overweight 25.0 - 29.9
#Obesity >= 30

def isValidInput(myInput):
  try:
    myInput = float(myInput)
    if(myInput > 0):
      return myInput
    else:
      print("Enter a number > 0!")
      return -1   
  except Exception as e:
    print(e)
    return -1

def getInputs(prompt):
    testInput = -1
    while testInput == -1:
        myInput = input(prompt)
        testInput = isValidInput(myInput)
    return testInput

def calculateBMI(weight, height):
   return round(weight / ((height/100)**2), 1)

def output(bmi):
    status = ""

    myDict = {"underweight": "Time to gain some weight! Eat high caloric foods!",
              "overweight": "Time to hit the gym!",
              "normal": "Keep going! Make sure to maintain a healthy diet.",
              "obese": "Gym and diet is everything, you got this! Try low caloric, high density foods!"}
    
    if bmi < 18.5:
        status = "underweight"
    elif bmi >= 18.5 and bmi <= 24.9:
       status = "normal"
    elif bmi >= 25 and bmi <= 29.9:
       status = "overweight"
    else:
       status = "obese"
        
    print(f"Your BMI is {bmi}, {status}.")
    print(myDict[status])

def main():
    height = round(getInputs("Enter your height in cm: "), 2)
    weight = round(getInputs("Enter your weight in kg: "), 2)
    bmi = calculateBMI(weight, height)
    output(bmi)

if __name__ == '__main__':
    main()

    


  

