class Cats:
    def __init__(self, name, gender, age):
        self.name = name
        self.gender = gender
        self.age = age
    def action(self):
        if self.name == "Сэм":
            return f'{self.name} гуляет на свежем воздухе'
        elif self.name == "Барон":
            name_ = f'{self.name} пошел поесть'
            return name_
        # else:
        #     return "это точно кот?"