# Write a Python script to read a text file line by line and print its contents.

# def read_file(filename):
#     try:
#         file = open(filename, 'r')
#         print("Contents of the file", filename, ":")
#         for line in file:
#             print(line.strip())  # strip() removes leading and trailing whitespace
#     except FileNotFoundError:
#         print("File not found!")

# def main():
#     filename = input("Enter the name of the file to read: ")
#     read_file(filename)

# if __name__ == "__main__":
#     main()




# Create a program that writes user input to a file and then reads the content of that file.
    
def write_to_file(filename):
    f = open(filename, 'w')
    user_input = input("Enter text to write to file: ")
    f.write(user_input)

def read_from_file(filename):
    f = open(filename, 'r')
    content = f.read()
    print("Content of the file:")
    print(content)

def main():
    filename = "user_input.txt"
    
    write_to_file(filename)
    
    read_from_file(filename)

if __name__ == "__main__":
    main()















# Write a Python program that reads student marks from a file  Each line in the file represents the marks of a student
# Implement the program using a while loop to read the file line by line 
# and split each line into individual marks. Then, print the marks of each student for 
# each subject along with their respective student numbers

# f = open("myfile.txt", 'r')
# i = 0
# while True:
#     i = i+1
#     line = f.readline()
#     if not line:
#         break
#     m1 = line.split(",")[0]
#     m2 = line.split(",")[1]
#     m3 = line.split(",")[2]
#     m4 = line.split(",")[3]
#     m5 = line.split(",")[4]
#     print(f"Marks of student {i} in Maths is: {m1}")
#     print(f"Marks of student {i} in English is: {m2}")
#     print(f"Marks of student {i} in Urdu is: {m3}")
#     print(f"Marks of student {i} in PST is: {m4}")
#     print(f"Marks of student {i} in PF is: {m5}")
#     # print(line)







# Coding Question: Student Grade Calculator and Recorder

def calculate_average(grades):
    return sum(grades) / len(grades)

def main():
    try:
        num_students = int(input("Enter the number of students: "))
        file = ("student_records.txt", "w")
        for i in range(1, num_students + 1):
            name = input(f"\nEnter details for Student {i}:\nName: ")
            grades = [int(x) for x in input("Grades (separated by spaces): ").split()]
            average_grade = sum(grades) / len(grades)
            file.write(f"Name: {name}, Grades: {grades}, Average Grade: {average_grade:.2f}\n")
        print("\nStudent records have been saved successfully.")
    except ValueError:
        print("Error: Please enter valid numeric grades.")


if __name__ == "__main__":
    main()
