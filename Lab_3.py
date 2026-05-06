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
        return self.distance > other.distance

    def __le__(self, other):
        if not isinstance(other, stars):
            return NotImplemented
        return self.distance <= other.distance

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

class StarsDatabase():
    def __init__(self, filename="stars_db.txt"):
        self.filename = filename
        self.stars_list = []

    def add_star(self, star):
        self.stars_list.append(star)
        print(f"Добавлена звезда: {star.name}")

    def display_all(self):
        if not self.stars_list:
            print("База пуста")
            return
        for star in self.stars_list:
            print(star)

    def save_to_db(self):
        with open(self.filename, "w", encoding="utf-8") as f:
            for star in self.stars_list:
                line = f"{star.name}, {star.radius}, {star.mass}, {star.distance}, {star.type}\n"
                f.write(line)
        print(f"Сохранено {len(self.stars_list)} звёзд в {self.filename}")

    def load_from_db(self):
        self.stars_list = []
        with open(self.filename, "r", encoding="utf-8") as f:
            for line in f:
                parts = line.split(", ")
                star = stars(parts[0], float(parts[1]), float(parts[2]), float(parts[3]), parts[4])
                self.stars_list.append(star)
        print(f"Загружено {len(self.stars_list)} звёзд из {self.filename}")

    def sort_key_name(self, star):
        return star.name

    def sort_key_distance(self, star):
        return star.distance

    def sort_key_radius(self, star):
        return star.radius

    def sort_key_mass(self, star):
        return star.mass

    def sort_by_field(self, field):
        if field == "name":
            self.stars_list.sort(key=self.sort_key_name)
        elif field == "distance":
            self.stars_list.sort(key=self.sort_key_distance)
        elif field == "radius":
            self.stars_list.sort(key=self.sort_key_radius)
        elif field == "mass":
            self.stars_list.sort(key=self.sort_key_mass)
        else:
            print("Неизвестное поле")
            return
        print(f"Отсортировано по {field}")

    def delete_star(self, name):
        i = 0
        while i < len(self.stars_list):
            if self.stars_list[i].name == name:
                deleted = self.stars_list.pop(i)
                print(f"Удалена звезда: {deleted.name}")
                return
            i += 1
        print(f"Звезда {name} не найдена")
