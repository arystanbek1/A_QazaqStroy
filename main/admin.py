from django.contrib import admin
from .models import SaveConcrete, Registration, Object, Block, Floor


@admin.register(Registration)
class RegistrationAdmin(admin.ModelAdmin):
    list_display = ["name", "surname", "phone", "object", "job"]


@admin.register(SaveConcrete)
class SaveConcreteAdmin(admin.ModelAdmin):
    list_display = ["data", "factory_name", "object_name",
                    "block", "mark", "constructive", "floor",
                    "fact_concrete", "sum_concrete", "accepted"]


admin.site.register(Object)

admin.site.register(Floor)


@admin.register(Block)
class BlockAdmin(admin.ModelAdmin):
    list_display = ["object", "name_block"]
