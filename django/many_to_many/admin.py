from django.contrib import admin

from many_to_many.models import Pizza, Topping, Post, User, PostLike

admin.site.register(Pizza)
admin.site.register(Topping)
admin.site.register(Post)
admin.site.register(User)
admin.site.register(PostLike)