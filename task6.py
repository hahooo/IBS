# Есть класс Animal c одним методом voice().
# class Animal:
# def voice(self):
# pass
# 1. Создать от него три класса наследника и для каждого сделать свою реализацию метода voice().
# 2. Создать по одному экземпляру всех наследников и вызвать для каждого переопределенный метод voice().

class Animal:

    def __init__(self, name, type_animal=None):
        self.name = name
        self.type_animal = type_animal

    def voice(self, voice):
        self.voice = voice
        print('[' + self.type_animal.capitalize() + ' "' + self.name + '" говорит: - ' + self.voice + ']')


class Lion(Animal):

    def __init__(self, name):
        Animal.__init__(self, name, 'Лев')

    def voice(self):
        Animal.voice(self, 'ррррр ...')

class Dog(Animal):

    def __init__(self, name):
        Animal.__init__(self, name, 'Пёс')

    def voice(self):
        Animal.voice(self, 'гав-гав')

class Cat(Animal):

    def __init__(self, name):
        Animal.__init__(self, name, 'Кот')

    def voice(self):
        Animal.voice(self, 'мяу-мяу')

cow = Animal('Маша', 'корова')
cock = Animal('Петя', 'петух')
cow.voice(voice='муууу ...')
cock.voice(voice='кукареку ...')

lion = Lion('Андрей')
dog = Dog('Шарик')
cat = Cat('Вася')

lion.voice()
dog.voice()
cat.voice()