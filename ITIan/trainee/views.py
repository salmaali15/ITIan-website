from django.shortcuts import render,redirect
from .models import *

def addTrainee(req):
    if req.method == 'POST':
        name = req.POST["name"]
        email = req.POST["email"]
        age = req.POST["age"]
        Trainee.objects.create(name=name,email=email,age=age)
        return redirect("t_list")
    return render(req,'trainee/add_trainee.html')

def updateTrainee(req, id):
    trainee = Trainee.objects.get(id=id)
    if not trainee:
        return redirect("t_list")
    
    if req.method == 'POST':
        trainee.name = req.POST["name"]
        trainee.email = req.POST["email"]
        trainee.age= req.POST["age"]
        trainee.save()
        return redirect("t_list")
    return render(req, 'trainee/update_trainee.html', {'trainee': trainee})

def traineeList(req):
    trainees = Trainee.objects.all()
    return render(req,'trainee/trainee_list.html',{'trainees':trainees})


def deleteTrainee(req,id):
    Trainee.objects.get(id=id).delete()
    return redirect("t_list")