from django.db import models
from course.models import Course

# Create your models here.
class Trainee(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    age = models.IntegerField()
    course = models.ForeignKey(to=Course,on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    @classmethod
    def get_trainee_by_id(cls,id):
        return cls.objects.get(id=id)
    
    @classmethod
    def get_all_trainee(cls):
        return cls.objects.all()
    