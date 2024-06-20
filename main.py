import random

# read the file and put the student names in a list
def read_file(file_name):  
  my_file = open(file_name, "r")
  data = my_file.read()
  student_list = data.splitlines()
  return student_list

# read the user input and make the seats fixed
def convert_to_int_list(fixed_str):
  fixed_seats = fixed_str.split(" ")
  for i in range(0, len(fixed_seats)):
    fixed_seats[i] = int(fixed_seats[i])
  return fixed_seats

# shuffle the student seats
def shuffle_list(student_list, fixed_seats):
  if fixed_seats[0] == 11:
    return student_list
  else:
    for i in range(0, len(student_list) - 1):
      j = random.randint(0, len(student_list) - 1)
      if i + 1 not in fixed_seats and j + 1 not in fixed_seats:
        temp = student_list[i]
        student_list[i] = student_list[j]
        student_list[j] = temp
  return student_list

# print the list out in vertical order starting with 1
def print_list(list):
  x = 1
  for letter in list:
    print(str(x) + ". " + letter)
    x = x + 1

    
# MAIN PROGRAM
file_name = "students.txt"
print("Welcome to Seating Chart R Izer!")
# Prints list of names
student_list = read_file(file_name)
print("Here is your current seating chart:")
print_list(student_list)

print("Enter the seats to fix (separated by a space)")
fixed_str = input("Options: 0 for full shuffle, 11 to keep current seats: ")

# Converts input to a list
fixed_seats = convert_to_int_list(fixed_str)

print("Here is your new seating chart: ")
print_list(shuffle_list(student_list, fixed_seats))