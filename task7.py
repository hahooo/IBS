# Необходимо дополнить "Практическое задание №6" таким образом,
# чтобы в конце программы мы вызвали статический метод родительского класса Animal,
# который вывел бы нам количество всех созданных экземпляров.
# Если мы создали трех наследников в предыдущем задании, то наш метод должен вывести на экран число 3.

class Animal:

    numInstanses = 0

    def __init__(self, name, type_animal=None):
        self.name = name
        self.type_animal = type_animal
        Animal.numInstanses = Animal.numInstanses + 1

    def voice(self, voice):
        self.voice = voice
        print('[' + self.type_animal.capitalize() + ' "' + self.name + '" говорит: - ' + self.voice + ']')

    def printNumInstanses():
        print(Animal.numInstanses)

    printNumInstanses = staticmethod(printNumInstanses)


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

# cow = Animal('Маша', 'корова')
# cock = Animal('Петя', 'петух')
# cow.voice(voice='муууу ...')
# cock.voice(voice='кукареку ...')

lion = Lion('Андрей')
dog = Dog('Шарик')
cat = Cat('Вася')

lion.voice()
dog.voice()
cat.voice()

lion.printNumInstanses()