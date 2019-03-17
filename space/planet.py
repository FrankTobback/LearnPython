class Planet:
    #class level attribute
    shape = 'round'
    #__init__ runs when we create a new instance of a class (a new object based on this class)
    # self refererce to the instance of the object
    #instance attribute
    def __init__(self, name, radius, gravity, system):
        self.name = name
        self.radius = radius
        self.gravity = gravity
        self.system = system

    def orbit(self):
        return f'{self.name} is orbiting in the {self.system}'

    @classmethod
    #cls refers to planet class
    def commons(cls):
        return f'All planets are {cls.shape} because of gravity'

    @staticmethod
    def spin(speed):
        return f'The planet spins and spins at {speed}'
