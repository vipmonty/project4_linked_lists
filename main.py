from slist import SListNode
from slist import SList
from course import Course

def calculate_gpa(courseList):
    sumGrades = float(0)
    credits = float(0)
    string_test = ""
    for course in courseList:
        # sumGrades += course.grade() * course.credit_hr()
        # credits += course.credit_hr()
    # if credits == 0:
    #     return 0
    # return sumGrades / credits
        sumGrades += course.credit_hr * course.grade
        credits += course.credit_hr

    if credits == 0:
        return 0

    return(sumGrades/credits)

def is_sorted(lyst):
    for i in range(0, len(lyst)  - 1):
        if lyst[i] > lyst[i + 1]:
            return False
    return True

def main():
    lyst = SList()
    lyst.insert(1)
    lyst.insert(10)
    lyst.insert(99)
    lyst.insert(8)
    lyst.insert(8)
    lyst.remove(8)
    lyst.insert(8)
    lyst.insert(8)
    lyst.insert(8)
    lyst.remove(1)
    lyst.remove_all(8)
    lyst.size()
    lyst.insert(6)
    lyst.insert(6)
    lyst.insert(6)
    lyst.remove(6)
    lyst.remove(6)
    lyst.remove_all(6)

    print(f"my list is =  {lyst}")
    print(lyst.size())
    print(lyst.find(10))
    print(str(lyst))

# constructor for Course:    def __init__(self, number=0, name="", credit_hour=0.0, grade=0.0)
    course_instance1 = Course(2420,"Cs 2420",3.0,3.2)
    course_instance2 = Course(2420,"Cs 2420",3.0,2.8)
    course_instance3 = Course(2010, "Eg",3.0,3.2)
    courseList = [course_instance1,course_instance2,course_instance3]
    answer = calculate_gpa(courseList)
    print(f" Gpa Calcultion:, {answer}")
    tester = SListNode()
    print(tester.value)


    lyst.insert(3.002)
    lyst.remove(3.002)
    print(lyst.remove("3.15"))

    print(lyst)



if __name__ == "__main__":
    main()