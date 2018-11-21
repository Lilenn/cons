from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    class Meta:
        verbose_name = '作者'
        verbose_name_plural = '作者'
    def __str__(self):
        return self.name
class Article(models.Model):
    title = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    public_date = models.DateField(auto_now_add=True)
    author = models.ForeignKey(Author,on_delete=models.CASCADE)
    class Meta:
        verbose_name = '文章'
        verbose_name_plural = '文章'
    def __str__(self):
        return self.title