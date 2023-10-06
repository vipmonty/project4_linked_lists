class Course:
    def __init__(self, number=0, name="", credit_hour=0.0, grade=0.0):
        # Parameter validation
        if not isinstance(number, int) or number < 0:
            raise ValueError("Course number must be a non-negative integer")
        
        if not isinstance(name, str):
            raise ValueError("Course name must be a string")
        
        if not isinstance(credit_hour, (int, float)) or credit_hour < 0:
            raise ValueError("Credit hours must be a non-negative number")
        
        if not isinstance(grade, (int, float)) or grade < 0 or grade > 4.0:
            raise ValueError("Grade must be a number between 0.0 and 4.0")
        
        self._number = number
        self._name = name
        self._credit_hour = credit_hour
        self._grade = grade
        self._value = None

    def number(self):
        return self._number

    def name(self):
        return self._name

    def credit_hr(self):
        return self._credit_hour

    def grade(self):
        return self._grade

    def __str__(self):
        return f"{self._name} Grade: {self._grade} Credit Hours: {self._credit_hour}"

    def __eq__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() == cnumb

    def __lt__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() < cnumb

    def __le__(self, other):
        return self.__lt__(other) or self.__eq__(other)

# # Example usage:
# course1 = Course(101, "Intro to Programming", 3.0, 3.5)
# course2 = Course(102, "Data Structures", 4.0, 3.7)

# print(course1)
# print(course2)

# # Comparisons
# print(course1 < course2)
# print(course1 == course2)