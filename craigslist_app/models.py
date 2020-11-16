from django.db import models

class Search(models.Model):
    search=models.CharField(max_length=500)
    created=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.search


class Meta:
    verbrose_name_plural="Searches"


