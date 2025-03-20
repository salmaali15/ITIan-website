from django.shortcuts import render,redirect

trainees = []
def addTrainee(req):
    if req.method == 'POST':
        name = req.POST["name"]
        email = req.POST["email"]
        age = req.POST["age"]
        id = len(trainees)+1
        trainee = {'id':id,'name':name,'email':email,'age':age}
        trainees.append(trainee)
        return redirect("t_list")
    return render(req,'trainee/add_trainee.html')

def updateTrainee(req, id):
    global trainees
    trainee = next((t for t in trainees if t['id'] == id), None)
    if not trainee:
        return redirect("t_list")
    
    if req.method == 'POST':
        trainee['name'] = req.POST["name"]
        trainee['email'] = req.POST["email"]
        trainee['age'] = req.POST["age"]
        return redirect("t_list")
    
    return render(req, 'trainee/update_trainee.html', {'trainee': trainee})

def traineeList(req):
    return render(req,'trainee/trainee_list.html',{'trainees':trainees})


def deleteTrainee(req,id):
    global trainees
    trainees=[trainee for trainee in trainees if trainee['id']!=id]
    return redirect("t_list")