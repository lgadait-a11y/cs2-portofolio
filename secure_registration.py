name = input("Enter Your Student Name: ")
if name: 
  print(f"Name:{name} ")
else:
  print("Error: Student Name Is Required")
  print("-------------------------")
  print("REGISTRATION NOT ACCEPTED") 
  print("-------------------------")
  exit()
section = input("Enter Your Section: ")
if section == "dahlia":
  print(f"Section:{section} ")
elif section == "rosal":
  print(f"Section:{section} ")
elif section == "sampaguita":
  print(f"Section:{section} ")
elif section == "ilang ilang":
  print(f"Section:{section} ")
else:
  print("Error: Unknown Section")
  print("-------------------------")
  print("REGISTRATION NOT ACCEPTED")
  print("-------------------------")
  exit()
valid_club = ["robotics", "science", "mathematics", "programming"]
club = input("Enter Your Club: ")
if club in valid_club:
  print(f"Club:{club} ")
else:
  print("Error: Please Choose A Valid Club.")
  print("-------------------------")
  print("REGISTRATION NOT ACCEPTED")
  print("-------------------------")
  exit()
email = input("Enter Your Email: ")
if "@" in email and "." in email:
  print(f"Email:{email} ")
else:
  print("Invalid Email Format")
  print("-------------------------")
  print("REGISTRATION NOT ACCEPTED")
  print("-------------------------")
  exit()
valid_attendance_status = ["present" , "absent" , "late"]
attendance_status = input("Enter Your Attendance Status: ")
if attendance_status in valid_attendance_status:
  print(f"Attendace Status:{attendance_status} ")
else:
  print("Invalid Attendace Status")
  print("-------------------------")
  print("REGISTRATION NOT ACCEPTED")
  print("-------------------------")
  exit()

print("---------------------")
print("REGISTRATION ACCEPTED")
print("---------------------")
print(f"Name:{name}")
print(f"Section:{section}")
print(f"Club:{club}")
print(f"Email:{email}")
print(f"Attendace Status:{attendance_status}")
