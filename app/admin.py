from django.contrib import admin

from app.models import *
# Register your models here.
class UsersAdmin(admin.ModelAdmin):
    admin.site.register(Course)
    admin.site.register(Category)
    admin.site.register(CustemUser)
    admin.site.register(Direction)
    admin.site.register(Elon)
    list_display = [Course]
    list_display = ('username')

  #  admin.site.unregister(User)




