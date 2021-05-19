from django.db import models

# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name='виды одежды')

    def __str__(self):
        return self.name


# COISES = (
#     (1, 'S'),
#     (2, 'М'),
#     (3, 'L')
# )


class Post(models.Model):

    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=100, verbose_name='название одежды: ')
    text = models.TextField(verbose_name='описание продукта')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    text = models.TextField(verbose_name='Коментарии')

    def __str__(self):
        return self.text