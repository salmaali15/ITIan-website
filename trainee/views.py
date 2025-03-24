from django.shortcuts import render,redirect
from .models import *
from .forms import TraineeForm
def addTrainee(req):
    context = {'courses': Course.get_all_courses(),'form':TraineeForm}
    if req.method == 'POST':
        name = req.POST["name"]
        email = req.POST["email"]
        age = req.POST["age"]
        course = Course.get_course_by_id(req.POST["course"]) 
        Trainee.objects.create(name=name,email=email,age=age,course=course)
        return redirect("t_list")
    return render(req,'trainee/add_trainee.html',context)

def updateTrainee(req, id):
    trainee = Trainee.objects.get(id=id)
    context = {'courses': Course.get_all_courses(),'trainee':trainee}
    if not trainee:
        return redirect("t_list")
    
    if req.method == 'POST':
        trainee.name = req.POST["name"]
        trainee.email = req.POST["email"]
        trainee.age= req.POST["age"]
        trainee.course = Course.get_course_by_id(req.POST["course"]) 
        trainee.save()
        return redirect("t_list")
    return render(req, 'trainee/update_trainee.html',context)

def traineeList(req):
    trainees = Trainee.objects.all()
    return render(req,'trainee/trainee_list.html',{'trainees':trainees})


def deleteTrainee(req,id):
    Trainee.objects.get(id=id).delete()
    return redirect("t_list")