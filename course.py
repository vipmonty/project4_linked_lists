# course.py

class Course:
    def __init__(self, number=0, name="", credit_hour=0.0, grade=0.0):
        """
        Initializes a Course instance with the specified parameters.
        Parameter validation is performed for each parameter.
        """
        if not isinstance(number, int):
            raise ValueError("Course number must be an integer")
        if not isinstance(name, str):
            raise ValueError("Course name must be a string")
        if not isinstance(credit_hour, float):
            raise ValueError("Credit hour must be a float")
        if not (0.0 <= grade <= 4.0):
            raise ValueError("Grade must be between 0.0 and 4.0")

        self.number = number
        self.name = name
        self.credit_hour = credit_hour
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

    def credit_hour(self):
        """
        Returns the number of credit hours as a floating-point number.
        """
        return self.credit_hour

    def grade(self):
        """
        Returns the grade as a numeric value in the range 4.0 - 0.0.
        """
        return self.grade

    def __str__(self):
        """
        Returns a string representing the contents of the course.
        """
        return f"{self.name} Grade: {self.grade} Credit Hours: {self.credit_hour}"

    def __eq__(self, other):
        """
        Returns True if self's value is equal to other's, False otherwise.
        """
        return self.number == other.number

    def __lt__(self, other):
        """
        Returns True if self's value is less than other's, False otherwise.
        """
        return self.number < other.number

    def __le__(self, other):
        """
        Returns True if self's value is less than or equal to other's, False otherwise.
        """
        return self.number <= other.number