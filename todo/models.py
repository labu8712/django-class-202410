from django.db import models


class Project(models.Model):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Item(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True)
    is_completed = models.BooleanField(default=False)
    end_time = models.DateTimeField(blank=True, null=True)

    project = models.ForeignKey(Project, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
