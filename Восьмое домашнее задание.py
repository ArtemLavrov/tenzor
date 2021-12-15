#Написать класс “animals” (животные), который включает общие признаки и поведения животных. От “animals” наследовать класс “mammals” (млекопитающие),
#который включает общие признаки и поведения млекопитающих. От “mammals” наследовать “human” (человек), “cat”(кот), “dog”(собака), у каждого свои признаки и поведения.


class Animals:
    def __init__(self,gender,name,height,weight):
        self.gender = gender
        self.name = name
        self.height = height
        self.weight = weight
    def Say(self,string):
        print("{a} сказал: '{b}'".format(a = self.name,b = string))

class mammals(Animals):
    def __init__(self, gender, name, height, weight,heterotrophs,nutrition):
        super().__init__(gender, name, height, weight)
        self.heterotrophs = heterotrophs
        self.nutrition = nutrition
    
class human(mammals):
    def __init__(self, gender, name, height, weight, heterotrophs, nutrition, mind, language):
        super().__init__(gender, name, height, weight, heterotrophs, nutrition)
        self.mind = mind
        self.language = language
    
class cat(mammals):
    def __init__(self, gender, name, height, weight, heterotrophs, nutrition):
        super().__init__(gender, name, height, weight, heterotrophs, nutrition)
    def Say_meow(self):
        print("MEEEEEOW!!!!!")

class dog(mammals):
    def __init__(self, gender, name, height, weight, heterotrophs, nutrition):
        super().__init__(gender, name, height, weight, heterotrophs, nutrition)
    def Say_WOUTH(self):
        print("WOUTH, WOUTH!!!!")


Barsik=cat('male', 'Barsik', '60', '10','Хищник', 'Всеядный')
print(Barsik.name,Barsik.gender,Barsik.height,Barsik.weight,Barsik.heterotrophs,Barsik.nutrition)
Barsik.Say_meow()

oleg=human('male',"Олег",180,90,"Всеядный", "Мясо и картошка","Разумный","Русский язык")
oleg.Say("Привет я Олег")
print(oleg.name)
print(oleg.gender)
print(oleg.height)
print(oleg.weight)
print(oleg.heterotrophs)
print(oleg.nutrition)
print(oleg.mind)
print(oleg.language)

Whale = mammals("female","whale",4000,1000,"травоядный", "Планктон")
print(Whale.gender,"\n ",Whale.name, "\n ", Whale.height,"\n ", Whale.weight,"\n ", Whale.heterotrophs, "\n ", Whale.nutrition)


# 2 Написать класс “Student”, который наследует класс human, у которого среди прочих признаков есть “Количество сданных дз”.
# *Перегрузить операторы сравнения так, чтобы студенты сравнивались по количеству сданных ими дз.

class Student(human):
    def __init__(self, gender, name, height, weight, heterotrophs, nutrition, mind, language, college, course, count_of_homework):
        super().__init__(gender, name, height, weight, heterotrophs, nutrition, mind, language)
        self.college = college
        self.course = course
        self.count_of_homework = count_of_homework
    def __lt__(self,other):
        return self.count_of_homework < other.count_of_homework
    def __eq__(self,other):
        return self.count_of_homework == other.count_of_homework
    def __le__(self,other):
        return self.count_of_homework <= other.count_of_homework


student1=Student("male","Boris",180,80,"Всеядный","чипсы","Разумный","Руссыкий","ЯРГУ",4,12)
student2=Student("male","Artem",180,80,"Всеядный","чипсы","Разумный","Руссыкий","ЯРГУ",4,14)
print(student1 == student2)
print(student1 != student2)
print(student1 > student2)
print(student1 < student2)
print(student1 >= student2)
print(student1 <= student2)


