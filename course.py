# course.py

class Course:
    def __init__(self, number=0, name="", credit_hr=0.0, grade=0.0):
        """
        Initializes a Course instance with the specified parameters.
        Parameter validation is performed for each parameter.
        """
        if not isinstance(number, int):
            raise ValueError("Course number must be an integer")
        if not isinstance(name, str):
            raise ValueError("Course name must be a string")
        if not isinstance(credit_hr, float):
            raise ValueError("Credit hour must be a float")
        if not (0.0 <= grade <= 4.0):
            raise ValueError("Grade must be between 0.0 and 4.0")

        self.number = number
        self.name = name
        self.credit_hr = credit_hr
        self.grade = grade



    def number(self):
        """
        Returns the course number as an integer.
        """
        return self.number

    def name(self):
        """
        Returns the course name as a string.
        """
        return self.name

    def credit_hr(self):
        """
        Returns the number of credit hours as a floating-point number.
        """
        return self.credit_hr

    def grade(self):
        """
        Returns the grade as a numeric value in the range 4.0 - 0.0.
        """
        return self.grade



    def __eq__(self, other):
        cnumb = other
        if isinstance(other, Course):
            cnumb = other.number()
        return self.number() == cnumb
    # def __eq__(self, other):
    #     if self.number == other.number:
    #         return True
    #     else: return False
    #     """
    #     Returns True if self's value is equal to other's, False otherwise.
    #     """

        # return self.number == other.number

    def __ne__(self, other):
        if self.number != other.number:
            return True
        else: return False
        # return self.number != other.number
        if self.name != other.number:
            return True
        else: return False

    def __lt__(self, other):
        if self.number < other.number:
            return True
        else: return False
        """
        Returns True if self's value is less than other's, False otherwise.
        """
        # return self.number < other.number
        if self.name < other.number:
            return True
        else: return False

    def __gt__(self,other):
        if self.number > other.number:
            return True
        else: return False
        '''
        greater than operator
        '''
        # return self.number > other.number

    def __le__(self, other):
        if self.number <= other.number:
            return True
        else: return False
        """
        Returns True if self's value is less than or equal to other's, False otherwise.
        """
        # return self.number <= other.number

    def __ge__(self,other):
        if self.number >= other.number:
            return True
        else: return False
        '''
        Returns True if self's value is less greater than or equal to, False otherwise.
        '''
        # return self.number >= other.number

    def __mul__(self,other):
        if self.number is int:
            return self.number * other.number
        elif self.grade is float:
            return self.grade * other.grade
        elif self.credit_hr is float:
            return self.credit_hr * other.credit_hr

    def __str__(self):
        """
        Returns a string representing the contents of the course.
        """
        return f"{self.name} Grade: {self.grade} Credit Hours: {self.credit_hr}"