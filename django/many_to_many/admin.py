from django.contrib import admin

from many_to_many.models import (
    # basic
    Pizza, Topping,
    # intermediate
    Post, User, PostLike,
    # self
    FacebookUser,
)

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(PostLike)
admin.site.register(FacebookUser)