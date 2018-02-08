from django.db import models


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    # 추상클래스이기 때문에 objects가 생성이 안됨.
    class Meta:
        abstract = True


class Student(CommonInfo):
    home_group = models.CharField(max_length=5)


# Be careful with related_name and related_query_name
class Other(models.Model):
    pass


class Base(models.Model):
    other = models.ForeignKey(
        Other,
        on_delete=models.CASCADE,
        related_name='%(app_label)s_%(class)s_set',
        related_query_name='%(app_label)s_%(class)s',
    )

    class Meta:
        abstract = True


class ChildA(Base):
    pass


class ChildB(Base):
    pass
