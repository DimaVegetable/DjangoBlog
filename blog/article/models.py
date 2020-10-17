from django.db import models
import datetime
# Create your models here.

class Article(models.Model):
    article_title = models.CharField('Заголовок', max_length=200)  # Zagolovok statbi
    article_text = models.TextField('Стаття') # sam text
    article_date = models.DateTimeField('Дата публикации', default=datetime.datetime.now)  # data

    class Meta():
        db_table = "article"