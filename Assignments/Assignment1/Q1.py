#Ask user for age in years, weight in
#pounds, heart rate in BPM, number of
#minutes exercising, and gender (M/W)

def validInteger(num, error):

    if num.isdigit():
        num = int(num)
        return num
    else:
        print(error)
        exit()
        return

def validFloat(num, error):

    if num.replace(".","").isdigit():
        num = float(num)
        return num
    else:
        print(error)
        exit()
        return

def womenCalories (age, weight, heartRate, time):

    calories = ((age * 0.074) + (weight * 0.05741) + (heartRate * 0.4472) - 20.4022) * time / 4.184

    print(f"{calories:.2f} calories burned for a woman.")


def menCalories (age, weight, heartRate, time):

    calories = ((age * 0.2017) + (weight * 0.09036) + (heartRate * 0.6309) - 55.0969) * time / 4.184

    print(f"{calories:.2f} calories burned for a man.")

def main():
    age = input("Enter your age: ")
    age = validInteger(age, "Please enter a positive integer for the age.")

    weight = input("Enter your weight in pounds: ")
    weight = validFloat(weight, "Enter a positive floating point number for the weight.")

    heartRate = input("Enter your heartrate (BPM): ")
    heartRate = validInteger(heartRate, "Please a positive integer for the heartrate.")

    time = input("Enter how long you exercised for in minutes: ")
    time = validInteger(time, "Please enter a positive floating point number for the time.")

    womenCalories(age, weight, heartRate, time)
    menCalories(age, weight, heartRate, time)

main()


