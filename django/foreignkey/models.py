from django.db import models


class Manufacturer(models.Model):
    name = models.CharField("Manufacturer's name", max_length=50)

    def __str__(self):
        return self.name


class Car(models.Model):
    manufacturer = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    name = models.CharField("Car's name", max_length=60)

    def __str__(self):
        return f'{self.manufacturer.name} {self.name}'


class Person(models.Model):
    name = models.CharField(max_length=60)
    # 자기자신을 다대일로 연결하는 필드
    # 비어있어도 무관, 연결된 객체가 삭제되면 함께 삭제되지 않고 해당필드를 비움
    teacher = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return self.name


class Type(models.Model):
    name = models.CharField(max_length=60)
    type_number = models.IntegerField(primary_key=True)

    def __str__(self):
        return f'{self.type_number} | {self.name}'


class Pokemon(models.Model):
    dex_number = models.IntegerField(primary_key=True)

    type = models.ForeignKey(Type, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.dex_number}, {self.name} {self.type.name}'
