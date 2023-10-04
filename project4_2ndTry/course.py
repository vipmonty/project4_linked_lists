class Course:
    def __init__(self, number=0, name="", credit_hour=0.0, grade=0.0):
        if not isinstance(number, int) or not isinstance(credit_hour, float) or not (0.0 <= grade <= 4.0):
            raise ValueError("Invalid parameter type or value")

        self.number = number
        self.name = name
        self.credit_hour = credit_hour
        self.grade = grade

    def number(self):
        return self.number

    def name(self):
        return self.name

    def credit_hr(self):
        return self.credit_hour

    def grade(self):
        return self.grade

    def __str__(self):
        return f"{self.name} Grade: {self.grade} Credit Hours: {self.credit_hour}"

    def __eq__(self, other):
        return self.number == other.number

    def __lt__(self, other):
        return self.number < other.number

    def __le__(self, other):
        return self.number <= other.number
