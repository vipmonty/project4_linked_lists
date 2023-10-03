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
    mylyst = SList()
    mylyst.insert(1)
    mylyst.insert(10)
    mylyst.insert(99)
    mylyst.insert(8)
    mylyst.insert(8)
    mylyst.remove(8)
    mylyst.insert(8)
    mylyst.insert(8)
    mylyst.insert(8)
    mylyst.remove_all(8)
    mylyst.size()

    print(f"my list is =  {mylyst}")
    print(mylyst.size())
    print(mylyst.find(10))
    print(str(mylyst))
    print(mylyst[2])
if __name__ == "__main__":
    main()