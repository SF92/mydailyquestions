from django.contrib import admin

# Register your models here.

import q_and_a.models as mods

# Register your models here.

admin.register(mods.Question, mods.Answer)(admin.ModelAdmin)

