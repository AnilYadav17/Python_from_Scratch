import os

def main():
    try:
        file = open("students.txt", "r")
        lines = file.readlines()
        file.close()
    except FileNotFoundError:
        print("Error: Input file 'students.txt' not found.")
        return

    result_file = open("result.txt", "w")
    error_file = open("error_log.txt", "w")

    for line in lines:
        line = line.strip() 
        
        if line == "":
            continue
            
        data = line.split(",")
        
        if len(data) < 4:
            error_file.write(f"Error: {line} -> Marks are missing\n")
            continue
            
        student_id = data[0]
        name = data[1]
        subject = data[2]
        marks_str = data[3]
        
        if student_id == "" or name == "" or subject == "" or marks_str == "":
            error_file.write(f"Error: {line} -> Missing fields\n")
            continue
            
        if not marks_str.isdigit():
            error_file.write(f"Error: {line} -> Marks must be numeric\n")
            continue
            
        marks = int(marks_str)
        
        if marks < 0 or marks > 100:
            error_file.write(f"Error: {line} -> Marks must be between 0 and 100\n")
            continue
            
        if marks >= 90 and marks <= 100:
            result = "Excellent"
        elif marks >= 75 and marks <= 89:
            result = "Very Good"
        elif marks >= 60 and marks <= 74:
            result = "Good"
        elif marks >= 40 and marks <= 59:
            result = "Pass"
        else:
            result = "Fail"
            
        final_string = student_id + " - " + name + " - " + subject + " - " + str(marks) + " - " + result + "\n"
        result_file.write(final_string)

    result_file.close()
    error_file.close()

    print("Student result processing completed successfully.")
    print("Valid records have been written to result.txt")
    print("Invalid records have been written to error_log.txt")

main()
