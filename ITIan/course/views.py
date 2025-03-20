from django.shortcuts import render, redirect

courses = []

def addCourse(req):
    if req.method == 'POST':
        name = req.POST["name"]
        description = req.POST["description"]
        duration = req.POST["duration"]
        id = len(courses) + 1
        course = {'id': id, 'name': name, 'description': description, 'duration': duration}
        courses.append(course)
        return redirect("c_list")
    return render(req, 'course/add_course.html')

def updateCourse(req, id):
    global courses
    course = next((c for c in courses if c['id'] == id), None)
    if not course:
        return redirect("c_list")
    
    if req.method == 'POST':
        course['name'] = req.POST["name"]
        course['description'] = req.POST["description"]
        course['duration'] = req.POST["duration"]
        return redirect("c_list")
    
    return render(req, 'course/update_course.html', {'course': course})

def courseList(req):
    return render(req, 'course/course_list.html', {'courses': courses})

def deleteCourse(req, id):
    global courses
    courses = [course for course in courses if course['id'] != id]
    return redirect("c_list")