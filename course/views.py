from django.shortcuts import render, redirect
from .models import *

def addCourse(req):
    if req.method == 'POST':
        name = req.POST["name"]
        description = req.POST["description"]
        duration = req.POST["duration"]
        Course.objects.create(name=name,description=description,duration=duration)
        return redirect("c_list")
    return render(req, 'course/add_course.html')

def updateCourse(req, id):
    course = Course.objects.get(id=id)
    if not course:
        return redirect("c_list")
    
    if req.method == 'POST':
        course.name = req.POST["name"]
        course.description = req.POST["description"]
        course.duration = req.POST["duration"]
        course.save()
        return redirect("c_list")
    
    return render(req, 'course/update_course.html', {'course': course})

def courseList(req):
    courses=Course.objects.all()
    return render(req, 'course/course_list.html', {'courses': courses})

def deleteCourse(req, id):
    Course.objects.get(id=id).delete()
    return redirect("c_list")