from django.db import models
from django.db.models import Manager


class OtherManager(Manager):
    def get_queryset(self):
        print('Other manager get_queryset!')
        return super().get_queryset()


class CustomManager(Manager):
    def get_queryset(self):
        print('Custom manager get_queryset!')
        return super().get_queryset()


class AbstractBase(models.Model):
    objects = CustomManager()

    class Meta:
        abstract = True


class ChildA(AbstractBase):
    pass

# AbstractBase에서의 objects도 사용 가능하지만 기본 objects를 나타내는 _default_manager라는 값에는 Other manager가 저장됨
# 이는 다른 써드파티 라이브러리와 같은 외부 패키지를 사용할 때 나타날 수 있는 상황.
class ChildB(AbstractBase):
    default_manager = OtherManager()


class ExtraManagerModel(models.Model):
    extra_manager = OtherManager()

    class Meta:
        abstract = True


class ChildC(AbstractBase, ExtraManagerModel):
    pass

# ExtraManagerModel에서 extra_manager라는 objects를 생성했기 떄문에 여기선 objects를 사용할 수 없음.
class ChildD(ExtraManagerModel):
    pass
