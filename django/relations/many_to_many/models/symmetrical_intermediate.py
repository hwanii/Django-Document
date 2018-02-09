from django.db import models

__all__ = (
    'TwitterUser',
    'Relation',
)


class TwitterUser(models.Model):
    name = models.CharField(max_length=50)
    relations = models.ManyToManyField(
        'self',
        symmetrical=False,
        through='Relation',
        related_name='+',  # +는 역참조 없앤다는 의미
    )

    def __str__(self):
        return self.name

    @property
    def following(self):
        """
        내가 following하고 있는 user 목록
        :return:
        """
        # following이 f인 모든 관계를 가져옴
        following_relations = self.relations_by_from_user.filter(
            type=Relation.RELATION_TYPE_FOLLOWING,
        )
        # 위의 쿼리셋에서 'to_user'값만 가져옴(내가 팔로잉하는 유저의 pk)
        # 리스트로 만들어줌. flat이 True가 아니면 튜플 형태로 오기 때문에 False로 해줌
        following_pk_list = following_relations.values_list('to_user', flat=True)
        # 리스트로 만들어져 있기 때문에 filter. 트위터 유저들 목록에서 pk가 가져온 pk와 일치하는 것들 뽑아오기
        following_users = TwitterUser.objects.filter(pk__in=following_pk_list)
        return following_users

    @property
    def followers(self):
        pk_list = self.relations_by_to_user.filter(
            type=Relation.RELATION_TYPE_FOLLOWING).values_list('from_user', flat=True)
        return TwitterUser.objects.filter(pk__in=pk_list)

    @property
    def block_users(self):
        pk_list = self.relations_by_from_user.filter(type=Relation.RELATION_TYPE_BLOCK, ).values_list('to_user',
                                                                                                      flat=True)
        return TwitterUser.objects.filter(pk__in=pk_list)

    def is_followee(self, to_user):
        return self.following.filter(pk=to_user.pk).exists()

    def is_follower(self, from_user):
        return self.followers.filter(pk=from_user.pk).exists()

    def follow(self, to_user):
        """
        to_user에 주어진 TwitterUser를 follow함
        """
        self.relations_by_from_user.filter(to_user=to_user).delete()
        self.relations_by_from_user.create(
            to_user=to_user,
            type=Relation.RELATION_TYPE_FOLLOWING,
        )

    def block(self, to_user):
        self.relations_by_from_user.filter(to_user=to_user).delete()
        self.relations_by_from_user.create(
            to_user=to_user,
            type=Relation.RELATION_TYPE_BLOCK,
        )

    class Meta:
        verbose_name_plural = 'symmetrical_Intermediate - TwitterUser'


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

    created_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = (
            # from_user와 to_user의 값이 이미 있을 경우
            # DB에 중복 데이터 저장을 막음
            # ex) from_user가 1, to_user가 3인 데이터가 이미 있다면
            #   두 항목의 값이 모두 같은 또 다른 데이터가 존재할 수 없음
            ('from_user', 'to_user'),
        )
        verbose_name_plural = 'symmetrical_Intermediate - Relation'
