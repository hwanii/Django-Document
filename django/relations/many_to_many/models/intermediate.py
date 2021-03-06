import datetime

from django.db import models
from django.utils import timezone

__all__ = (
    'Post',
    'User',
    'PostLike',
)


class Post(models.Model):
    title = models.CharField(max_length=50)
    like_users = models.ManyToManyField(
        'User',
        through='PostLike',
        # MTM으로 연결된 반대편에서 (지금의 경우 특정 User가 좋아요 누른 Post목록을 가져오고 싶은 경우)
        # 자동 생성되는 역방향 매니저 일므인 post_set대신 like_posts라는 이름을 사용하도록 한다.
        related_name='like_posts',
    )

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = 'Intermediate - Post'


class User(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Intermediate - User'


class PostLike(models.Model):
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
    )
    created_date = models.DateTimeField(
        auto_now_add=True
    )

    def __str__(self):
        return '"{title}"글의 좋아요({name}, {date})'.format(
            title=self.post.title,
            name=self.user.name,
            date=datetime.strftime(
                # timezone.make_naive(self.created_date), '%Y.%m.%d'),
                timezone.localtime(self.created_date), '%Y.%m.%d'),
        )

    class Meta:
        verbose_name_plural = 'Intermediate - PostLike'
