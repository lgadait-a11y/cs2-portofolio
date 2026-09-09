#Expected Result
##Made by AI to show the difference
def get_student_registration():
    # Track overall validation status
    is_valid = True
    error_message = ""

    # 1. Student Name - Presence Validation
    name = input("Enter student name: ").strip()
    if not name:
        is_valid = False
        error_message = "Student name is required."

    # 2. Age - Data Type + Range Validation
    if is_valid:
        age_input = input("Enter age: ").strip()
        try:
            age = int(age_input)
            if age < 11 or age > 18:
                is_valid = False
                error_message = "Age must be from 11 to 18."
        except ValueError:
            is_valid = False
            error_message = "Age must be a number."

    # 3. Grade Level - Acceptable Value Validation
    if is_valid:
        grade_input = input("Enter grade level: ").strip()
        if grade_input not in ["7", "8", "9", "10", "11", "12"]:
            is_valid = False
            error_message = "Invalid grade level."

    # 4. Email - Simple Pattern Validation
    if is_valid:
        email = input("Enter email: ").strip()
        if "@" not in email or "." not in email:
            is_valid = False
            error_message = "Invalid email format."

    # 5. Registration Code - Length Validation
    if is_valid:
        reg_code = input("Enter registration code: ").strip()
        if len(reg_code) != 6:
            is_valid = False
            error_message = "The registration code must contain exactly 6 characters."

    # Output Results
    print("\n" + "-" * 23)
    if is_valid:
        print("REGISTRATION ACCEPTED")
        print("-" * 23)
        print(f"Student: {name}")
        print(f"Age: {age}")
        print(f"Grade Level: {grade_input}")
        print(f"Email: {email}")
        print(f"Registration Code: {reg_code}")
    else:
        print("REGISTRATION NOT ACCEPTED")
        print("-" * 23)
        print(error_message)

if __name__ == "__main__":
    get_student_registration()
  

##Actual Output
 

name = input("Enter student name: ")
if name:
    print(f"Name: {name}")
else:
    print("\nREGISTRATION NOT ACCEPTED")
    print("-----------------------")
    print("Student name is required.")
    exit()


age_input = input("Please Enter Your Age: ")
if age_input.isdigit():
    age = int(age_input)
    if 11 <= age <= 18:
        print(f"Age: {age}")
    else:
        print("\nREGISTRATION NOT ACCEPTED")
        print("-----------------------")
        print("Age must be from 11 to 18.")
        exit()
else:
    print("\nREGISTRATION NOT ACCEPTED")
    print("-----------------------")
    print("Age must be a number.")
    exit()


grade_input = input("Please Enter Your Grade Level: ")
if grade_input.isdigit():
    grade_level = int(grade_input)
    if 7 <= grade_level <= 12:
        print(f"Grade Level: {grade_level}")
    else:
        print("\nREGISTRATION NOT ACCEPTED")
        print("-----------------------")
        print("Invalid grade level.")
        exit()
else:
    print("\nREGISTRATION NOT ACCEPTED")
    print("-----------------------")
    print("Invalid grade level.")
    exit()


email = input("Please Enter Your Email: ")
if "@" in email and "." in email:
    print(f"Email: {email}")
else:
    print("\nREGISTRATION NOT ACCEPTED")
    print("-----------------------")
    print("Invalid email format.")
    exit()


reg_code = input("Please Enter Your Registration Code: ")
if len(reg_code) == 6:
    print(f"Registration Code: {reg_code}")
else:
    print("\nREGISTRATION NOT ACCEPTED")
    print("-----------------------")
    print("The registration code must contain exactly 6 characters.")
    exit()


print("\n-----------------------")
print("REGISTRATION ACCEPTED")
print("-----------------------")
