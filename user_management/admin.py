from django.contrib import admin

# Register your models here.

import user_management.models as mods

# Register your models here.

admin.register(mods.UserInfo)(admin.ModelAdmin)

