class Plane:
    """
    Клас представлання літака
    """
    def __init__(self, tank_capacity=0, name='', num_passengers=0, max_speed=0, model=''):
        self.__tank_capacity = tank_capacity
        self.__name = name
        self.__num_passengers = num_passengers
        self.__max_speed = max_speed
        self.__model = model

    def __del__(self):
        print(f'{self.__name} deleted successfully')

    def get_name(self):
        return self.__name

    def get_tank_capacity(self):
        return self.__tank_capacity

    def get_num_passengers(self):
        return self.__num_passengers

    def get_info(self):
        """
        Отримання інформації про об'єкт
        """
        return self.__name, self.__tank_capacity, self.__num_passengers

    def __str__(self):
        return (f'Name = {self.__name}, '
                f'Model = {self.__model}, '
                f'Max speed = {self.__max_speed}, '
                f'Tank capacity = {self.__tank_capacity}, '
                f'Number of passengers = {self.__num_passengers}')

    def __repr__(self):
        return f'Plane {self.__name}({self.__model}): Tank capacity = {self.__tank_capacity}, Number of passengers = {self.__num_passengers}, Max speed = {self.__max_speed}'

def main():

    plane1 = Plane(405000, 'Мрія', 600, 850, 'Aн-255')
    plane2 = Plane(15, 'BambooPlane', 1, 160, 'A321CEO')
    plane3 = Plane(26000, 'Boeing', 200, 850, '737' )

    print(Plane.__doc__)
    print(Plane.get_info.__doc__)

    print(repr(plane1))
    print(repr(plane2))
    print(plane2)
    print(repr(plane3))
    print(plane3)

    #print(plane2.name)

    print(plane1.get_name())
    print(plane2.get_num_passengers())
    p = plane3.get_tank_capacity()
    print(p)
   # print(plane3.name)

    print('\n\n\n', plane1.get_info())

main()
