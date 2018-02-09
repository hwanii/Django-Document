from django.db import models
from django.db.models.manager import Manager


class User(models.Model):
    name = models.CharField(max_length=50)
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_block = models.BooleanField(default=False)

    def __str__(self):
        return self.name


# AdminManager를 사용하는 class에 get_queryset을 실행하고 return되는 queryset을 objects로 쓸 수 있게 함
class AdminManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_admin=True)


class Admin(User):
    # objects를 AdminManager에서 정해준 query에 맞는 내용만 가져옴
    objects = AdminManager()

    class Meta:
        proxy = True

    def __str__(self):
        return f'{self.name} (관리자)'

    def drop(self, user):
        user.delete()


class StaffManager(Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_staff=True)


class Staff(User):
    objects = StaffManager()

    class Meta:
        proxy = True

    def block(self, user):
        user.is_block = True
        user.save()

    def __str__(self):
        return f'{self.name} (스태프)'
