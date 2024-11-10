from django.contrib import admin

from todo.models import Item, Project


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "is_completed", "project")
    search_fields = ("title", "content")
    list_filter = ("project", "is_completed")

    save_as = True
