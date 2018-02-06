from django.db import models


# Facebook과는 다르게 내가 팔로잉한다 해서 상대방이 나를 팔로잉 하는 것은 아님.
class InstagramUser(models.Model):
    name = models.CharField(max_length=50)
    following = models.ManyToManyField(
        'self',
        # 대칭관계가 아님
        symmetrical=False,
        related_name='followers'
    )

    def __str__(self):
        return self.name

