from slist import SList
from course import Course

def calculate_gpa(courseList):
    sumGrades = 0
    credits = 0
    for course in courseList:
        sumGrades += course.value.grade() * course.value.credit_hr()
        credits += course.value.credit_hr()
    if credits == 0:
        return 0
    return sumGrades / credits

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
    lyst.remove_all(8)
    lyst.size()

    print(f"my list is =  {lyst}")
    print(lyst.size())
    print(lyst.find(10))
    print(str(lyst))
    print(lyst[2])
# constructor for Course:    def __init__(self, number=0, name="", credit_hour=0.0, grade=0.0)
    course_instance1 = Course(2420,"Cs 2420",3.0,3.2)
    course_instance2 = Course(2420,"Cs 2420",3.0,2.8)
    courseList = [course_instance1,course_instance2]
    print(type(course_instance1.credit_hour))

if __name__ == "__main__":
    main()