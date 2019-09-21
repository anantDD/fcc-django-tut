from django.db import models

# Create your models here.


class Article(models.Model):
    text = models.CharField(blank=False, null=False,
                            default='', max_length=200)

    def get_absolute_url(self):
        return reverse("article_detail", kwargs={"id": self.id})
