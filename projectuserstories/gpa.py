class Course:
    """
    Class Description:
        class that holds course information for a student
    """
    def __init__(self, subject, grade, credit):
        """
            Description:
                creates a Course Object for a student
            Parameters:
                subject (str): the name of the major the course belongs to
                grade (str): the grade of the course
                credits (int): the number of credits for the course
        """
        self.subject = subject
        self.grade = grade
        self.credit = credit

    def __str__(self):
        return str(self.subject + " " + self.grade + " " + str(self.credit))
    
    def __repr__(self) -> str:
        return str(self)

class GPA_Calc():
    """
        Class Description:
            GPA calculator that calculates student's Major, Minor, and Overall GPA information
    """
    def __init__(self, major, minor):
        """
            Description:
                initializes course list
                assigns major and minor
            Parameters:
                major: student's major
                minor: student's minor
            Return:
                None
        """
        self.courses = []
        self.major = major
        self.minor = minor

    def addCourse(self, major, grade, credit):
        """
            Description:
                appends the course grade and credits to separate lists
            Parameters:
                major (str): the major
                grade (str): course grade 
                credits (int): course credits
            Return:
                None
        """
        self.courses.append(Course(major, grade, credit))

    def calculateGPA(self, courses):
        """
            Description:
                calculates the GPA for given grades and credits
            Parameters:
                courses (list): list of Course objects
            Return:
                int: GPA for given grades and credits
        """
        #variable assignment
        total_gpa = 0.0
        total_credits = 0.0

        #for loop iteration assigning GPA to given grades
        for course in courses:
            if course.grade == "A+":
                total_gpa += 4.33 * course.credit

            elif course.grade == "A":
                total_gpa += 4.0 * course.credit

            elif course.grade == "A-":
                total_gpa += 3.66 * course.credit

            elif course.grade == "B+":
                total_gpa += 3.33 * course.credit

            elif course.grade == "B":
                total_gpa += 3.0 * course.credit

            elif course.grade == "B-":
                total_gpa += 2.66 * course.credit

            elif course.grade == "C+":
                total_gpa += 2.33 * course.credit

            elif course.grade == "C":
                total_gpa += 2.0 * course.credit

            elif course.grade == "C-":
                total_gpa += 1.66 * course.credit

            elif course.grade == "D+":
                total_gpa += 1.33 * course.credit

            elif course.grade == "D":
                total_gpa += 1.0 * course.credit

            elif course.grade == "D-":
                total_gpa += 0.66 * course.credit

            elif course.grade == "F":
                total_gpa += 0.0 * course.credit

            else:
                raise ValueError("Invalid course.")
            
            total_credits += course.credit

        
        #if no credits have been earned
        if total_credits == 0:
            return 0.0
    
        else:
            gpa = total_gpa / total_credits
            return f"{gpa:.2f}"

    def major_grades(self):
        """
            Description:
                appends only the minor grades and credits
            Parameters:
                None
            Return:
                list: list of [grade, credit]
        """
        #empty list
        grades = []

        #for loop
        #iterating through each course and append major courses
        for course in self.courses:
            if course.subject == self.major:
                grades.append(course)

        return grades
    
    def minor_grades(self):
        """
            Description:
                appends only the minor grades and credits
            Parameters:
                None
            Return:
                list: list of [grade, credit]
        """
        #empty list
        grades = []

        #for loop
        #iterating through each course and append minor courses
        for course in self.courses:
            if course.subject == self.minor:
                grades.append(course)

        return grades

    def major_gpa(self):
        """
            Description:
                calculates the major GPA
            Parameters:
                None
            Return:
                int: major GPA
        """
        return self.calculateGPA(self.major_grades())

    def minor_gpa(self):
        """
            Description:
                calculates the minor GPA
            Parameters:
                None
            Return:
                int: minor GPA
        """
        return self.calculateGPA(self.minor_grades())

    def overall_gpa(self):
        return self.calculateGPA(self.courses)
    
    def repeating_class(self, other, type, index):
        """
            Description:
                This either overides GPA or averages it out based on Repeating classes
            Parameters:
                other, type
            Return:
                self
        """
        if type == "average":
            self.courses.append(other.courses[index])

        if type == "replace":
            self.courses[index]= other.courses[index]

        return self

    def locate_file(self, student_id):
        """
            Description:
                attempts to locate the file for the student
            Parameters:
                student_id: the id of the student
            Return:
                str reporting if the file is found
        """
        quit = False

        while not quit:
            file = f"{student_id}.txt"

            try:
                with open(f"{file}", "r") as a_file:
                    for line in a_file:
                        data = line.strip().split(",")
                        # Iterate over each data in the CSV file
                        # Append the data as a list to the data list
                        self.addCourse(data[0], data[1].strip(), float(data[2].strip()))
                
                quit = True
                return f"Transcript file sucessfully located."

            except:
                quit = True
                return "File not located. Enter the information again."

def GPA_getStudent():
    print("Student GPA Calculator")
    student_id = input("Enter the ID of the student: ")
    student_major = input("Enter the major of the student: ").upper()
    student_minor = input("Enter the minor of the student: ").upper()

    student = GPA_Calc(student_major, student_minor)
    student.locate_file(student_id)

    print("Student ID: ", student_id)
    print("Major: ", student.major, "Major GPA: ", student.major_gpa())
    print("Minor: ", student.minor, "Minor GPA: ", student.minor_gpa())
    print("Overall GPA: ", student.overall_gpa())

GPA_getStudent()