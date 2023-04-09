from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    
    def __str__(self):
            return self.name
    class Meta:
        managed = True
        db_table = 'Category'

class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    category_id = models.ForeignKey('Category', models.DO_NOTHING)
    title = models.CharField(max_length=45)
    desc = models.TextField()
    created_by = models.CharField(max_length=30, blank=False, null=True)
    date_created = models.DateField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'Article'