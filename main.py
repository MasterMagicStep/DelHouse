class House:
    #
    house_history=[]
    #
    def __new__(cls, *args, **kwargs):
        instance = object.__new__(cls)
        args=args[0]
        cls.house_history.append(args)
        return instance
    #
    def __init__(self, name, floors):
        self.name = name
        self.floors = floors
        if isinstance(floors, House):
            self.house_history = floors.append()
    #
    def Gt (self , New):
        if 0 < New <= self.floors:
            for f in range(1, New+1):
                print(f)
        else:
                print("Floor is not defined")
    #
    def __del__(self):
        return print(f'{self.name} deleted, but not forget')

    #
    def __lt__(self, other):
        return self.floors < other.floors
    def __eq__(self, other):
        return self.floors == other.floors
    def __le__ (self,other):
        return self.floors <= other.floors
    def __gt__(self,other):
        return self.floors > other.floors
    def __ge__(self, other):
        return self.floors >= other.floors
    def __ne__(self, other):
        return self.floors != other.floors
    #
    def __add__(self, value):
        self.floors += value
        return self
    def __radd__(self, other):
         return self + other
    def __iadd__(self,other):
        return self + other
    #
    def __len__ (self):
        return self.floors
    def __str__(self):
        return (f"Название: {self.name}, количество этажей: {self.floors}")


h1 = House('Doctrine', 10)
print(House.house_history)
h2 = House('Laclord', 11)
print(House.house_history)
h3 = House('ElfTreeGard', 15)
print(House.house_history)
#
del h3
#
print(House.house_history)