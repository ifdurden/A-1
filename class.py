from classfile import Student
def main():
    try:
        student = Student.get()
        print(student)
    except ValueError as v: 
        print(f"Error : {v}")
        
if __name__ == "__main__":
    main()
