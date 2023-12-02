from datetime import datetime

def calculate_age(birthdate):
    today = datetime.now()
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

while True:
    # Get user's date of birth
    dob_str = input("Enter your date of birth (dd-mm-yyyy): ")

    # Validate the date format
    try:
        birthdate = datetime.strptime(dob_str, "%d-%m-%Y")
    except ValueError:
        print("Invalid date format. Please use dd-mm-yyyy.")
    else:
        # Calculate age if the date format is correct
        age = calculate_age(birthdate)
        print(f"You are {age} years old.")
        break  # Exit the loop if the date is valid