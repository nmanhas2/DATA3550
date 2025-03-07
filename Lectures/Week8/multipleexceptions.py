# wrap up in a function
def get_customer_age():
  while True:
    try:
      age = input("Enter the customer's age: (quit to exit the program)")
      if age.lower() == "quit":
        print(f"Thank you for using the program. Now existing the program... ...")
        return None
      age = int(age)

      if age < 0:
        raise ValueError("Age cannot be negative.")

    except ValueError:
      print("Invalid input. Please enter a number.")
    except KeyboardInterrupt:
      print("Input cancelled.")
      return None
    except Exception as e:
      print(f"An error occurred: {e}")
    else:
      return age
    finally:
      print("This line will always be executed. Thank you for using the program.")

def main():
  age = get_customer_age()
  if age is not None:
    print(f"The customer is {age} years old. ")

if __name__ == "__main__":
  main()