from django.contrib import admin

from .models import (
    # basic
    Pizza, Topping,
    # intermediate
    Post, User, PostLike,
    # self
    FacebookUser, InstagramUser,
    #
    Relation, TwitterUser,
)

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(PostLike)
admin.site.register(FacebookUser)
admin.site.register(InstagramUser)
admin.site.register(Relation)
admin.site.register(TwitterUser)
