#create class and attributes
class University:
    
    def __init__(self, university_name, location, undergraduate_students, graduate_students):
        self.university_name = university_name
        self.location = location
        self.undergraduate_students = undergraduate_students
        self.graduate_students = graduate_students
    
    #create method to calculate and print the sum of undergraduate and graduate
    def print_university_size(self):
        total_students = self.undergraduate_students + self.graduate_students
        print("The university size is", total_students)
    
    #create a method to check which of undergraduate and graduate is greater
    def is_undergraduate_greater(self):
        if self.undergraduate_students > self.graduate_students:
            print("There are more undergraduate students than graduate students.")
        elif self.undergraduate_students <= self.graduate_students:
            print("There are more graduate students than undergraduate students")


#create SPU object and define each attributes based on actual information from SPU website
SPU = University("Saint Peters University", "New Jersey", 2134, 875)
SPU.print_university_size()
SPU.is_undergraduate_greater()



#Bonus 
#create a second class College with inheritence
class College(University):
    
    #add a new method to check the times of undergraduate with graduate
    def ratio_student(self):
        if self.undergraduate_students > self.graduate_students:
            times_students = int(self.undergraduate_students//self.graduate_students)
            print("Undergraduate students are", times_students, "times of graduate students.")
        elif self.undergraduate_students < self.graduate_students:
            print("Graduate students are", times_students, "times of undergraduate students.")
        else:
            print("Graduate students are same as undergraduate students.")
SPU2 = College("Saint Peters University", "New Jersey", 2134, 875)
SPU2.ratio_student()


    