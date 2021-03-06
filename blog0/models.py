from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(u'', max_length=256)
    content = models.TextField(u'')
    pub_date = models.DateField(u'', auto_now_add=True, editable = True)
    update_date = models.DateField(u'', auto_now=True, null=True)

    def __str__(self):
        return self.title
