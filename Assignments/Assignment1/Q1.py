#Ask user for age in years, weight in
#pounds, heart rate in BPM, number of
#minutes exercising, and gender (M/W)

def validNumber(prompt, dataType=int):
    while 1:
        try:
            num = dataType(input(prompt))
            if num >= 0:
                return num
            else:
                print(f"Please input a positive number.")
        except ValueError as e:
            print(f"Invalid input. Error: {e}")
        

def womenCalories (age, weight, heartRate, time):

    calories = ((age * 0.074) + (weight * 0.05741) + (heartRate * 0.4472) - 20.4022) * time / 4.184

    print(f"{calories:.2f} calories burned for a woman.")


def menCalories (age, weight, heartRate, time):

    calories = ((age * 0.2017) + (weight * 0.09036) + (heartRate * 0.6309) - 55.0969) * time / 4.184

    print(f"{calories:.2f} calories burned for a man.")

def main():
    age = validNumber("Enter your age: ")

    weight = validNumber("Enter your weight in pounds: ", float)

    heartRate = validNumber("Enter your heartrate (BPM): ")

    time = validNumber("Enter how long you exercised for in minutes: ")

    womenCalories(age, weight, heartRate, time)
    menCalories(age, weight, heartRate, time)

main()


