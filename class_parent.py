class Parent:
    prod='frukt'
    def __init__(self,sort_fr):
        self.sort_fr=sort_fr
    def __str__(self):
        return self.sort_fr
    def sort(self):
        print(f'сорт фрукта {self.sort_fr}')
class Aple(Parent):
    pass
class Pear(Parent):
    def fruk_l (self):
        print(self.prod)
shtr=Aple('shtrifel')
zim=Pear('zimn')

print(shtr.__str__())
print(zim.__str__())
shtr.sort()
zim.sort()

zim.fruk_l()