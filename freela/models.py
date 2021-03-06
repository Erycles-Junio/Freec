from django.contrib.auth.models import User
from django.db import models


class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sender')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='receiver')
    message = models.CharField(max_length=1200)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return self.message

    class Meta:
        ordering = ('timestamp',)


class Project(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    budget = models.IntegerField()
    description = models.CharField(max_length=1200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Service(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    budget = models.IntegerField()
    description = models.CharField(max_length=1200)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    area = models.IntegerField()

    def __str__(self):
        return self.name


class Comment(models.Model):
    post = models.ForeignKey(Project, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=4000)

    def __str__(self):
        return self.text

class Enviroment(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    post = models.ForeignKey(Project, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.post.name




    
