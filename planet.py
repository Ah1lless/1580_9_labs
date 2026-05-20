class stars():
    id_counter = 0
    
    def __init__(self, name, radius, mass, distance, type):
        self.name = name
        self.radius = radius
        self.mass = mass
        self.distance = distance
        self.type = type
        stars.id_counter += 1
        self._id = stars.id_counter
        print(f"Создание ID {self._id}")

    def __str__(self):
        return f"({self.name}, {self.type}, {self.radius}, {self.mass}, {self.distance})"

    def __repr__(self):
        return f"Star-{self.name}, Type-{self.type}, Radius-{self.radius}, Mass-{self.mass}, Distance-{self.distance}"

    def __lt__(self, other):
        if not isinstance(other, stars):
            return NotImplemented
        return self.distance < other.distance

    def __eq__(self, other):
        if not isinstance(other, stars):
            return NotImplemented
        return self.name == other.name

    def __gt__(self, other):
        if not isinstance(other, stars):
            return NotImplemented
        return self.mass > other.mass

    def __le__(self, other):
        if not isinstance(other, stars):
            return NotImplemented
        return self.radius <= other.radius

    def __ge__(self, other):
        if not isinstance(other, stars):
            return NotImplemented
        return self.distance >= other.distance

    def __ne__(self, other):
        if not isinstance(other, stars):
            return NotImplemented
        return self.name != other.name

    def copy(self):
        return stars(self.name, self.radius, self.mass, self.distance, self.type)

    def __del__(self):
        print(f"Удаление ID {self._id}")



