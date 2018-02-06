from django.db import models

__all__ = (
    'TwitterUser',
)


class TwitterUser(models.Model):
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
        related_name='+', # +는 역참조 없앤다는 의미
    )


class Relation(models.Model):
    """
    유저 간의 관계를 정의하는 모델
    단순히 자신의 MTM이 아닌 중개 모델의 역할을 함
    추가적으로 받는 정보는 관계의 타입(팔로잉 또는 차단)
    """
    RELATION_TYPE_FOLLOWING = 'f'
    RELATION_TYPE_BLOCK = 'b'
    CHOICE_TYPE = (
        (RELATION_TYPE_FOLLOWING, '팔로잉'),
        (RELATION_TYPE_BLOCK, '차단')
    )
    from_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        # 자신이 from_user인 경우의 Relation 목록은 가져오고 싶을 경우
        related_name='relations_by_from_user'
    )
    to_user = models.ForeignKey(
        TwitterUser,
        on_delete=models.CASCADE,
        # 자신이 to_user인 경우의 Relation 목록은 가져오고 싶을 경우
        related_name='relations_by_to_user'
    )
    type = models.CharField(max_length=1, choices=CHOICE_TYPE)
