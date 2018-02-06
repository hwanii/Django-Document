from django.db import models

__all__ = (
    'FacebookUser',
)

# 누구를 친구 추가 했으면 서로 친구가 됨 -> 내가 너의 친구면 너도 나의 친구 -> 동등한 관계가 됨.
class FacebookUser(models.Model):
    name = models.CharField(max_length=50)
    friends = models.ManyToManyField('self')

    def __str__(self):
        # list comprehension 사용
        friends = ', '.join([friend.name for friend in self.friends.all()])

        # Manager의 values_list를 사용
        # DB에서 모든 friends의 'name'필드의 값만 가져옴
        friends = ', '.join(self.friends.values_list('name', flat=True))

        return f'{self.name} (친구: {friends})'

