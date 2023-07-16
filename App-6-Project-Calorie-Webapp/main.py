class Calorie:
    """
    Represent amount of calories calculated with
    BMR = 18*weight + 6.25*height - 5*age -10*temperature.
    """

    def __init__(self, weight, height, age, temperature):
        self.weight = weight
        self.height = height
        self.age = age
        self.temperature = temperature

    def calculate(self):
        pass


class Temperature:
    """
    Represent a temperature value extracted from timeanddate.com/weather_webpage.
    """

    def __init__(self, country, city):
        self.country = country
        self.city = city

    def get(self):
        pass
