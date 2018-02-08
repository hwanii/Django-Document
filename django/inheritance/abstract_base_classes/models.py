from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    # 추상클래스이기 때문에 objects가 생성이 안됨.
    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
