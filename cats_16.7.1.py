from Class_cat import Cats
baron = Cats('Барон', 'мальчик', 2)
sem = Cats("Сэм", 'мальчик', 2)
print(f'{baron.name},{baron.gender},{baron.age} года')
print(baron.action())
print(sem.name,sem.age,'года' )
print(sem.action())