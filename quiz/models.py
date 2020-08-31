from django.db import models

# Create your models here.

class Story(models.Model):
    title = models.CharField(max_length=100, null=True)
    text = models.TextField(max_length=5000, null=True)
    def __str__(self):
        return self.text
    class Meta:
        verbose_name_plural = 'Stories'
    

class Answer(models.Model):
    option = models.CharField(max_length=1, null=True)

    def __str__(self):
        return self.option


class Question(models.Model):
    label = models.CharField(max_length=100, null=True)
    a = models.CharField(max_length=100, null=True)
    b = models.CharField(max_length=100, null=True)
    c = models.CharField(max_length=100, null=True)
    d = models.CharField(max_length=100, null=True)
    answer = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.label


