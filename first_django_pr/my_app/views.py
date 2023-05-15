from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import User
# Create your views here.

index_template = f"""
           <form method="post" action="/login/">
              <div>
                <label for="name">Name:</label>
                <input type="text" id="name" name="name">
              </div>
              <div>
                <label for="password">Password:</label>
                <input type="text" id="password" name="password">
              </div>
              <div>
                <input type="radio" id="python" name="course" value="Python Programming">
                <label for="python">Python Programming</label>
              </div>
              <div>
                <input type="radio" id="java" name="course" value="Java Programming">
                <label for="java">Java Programming</label>
              </div>
              <div>
                <input type="radio" id="web" name="course" value="Web Development">
                <label for="web">Web Development</label>
              </div>
              <button type="submit">Submit</button>
            </form>
"""

def index(request):
    return HttpResponse(index_template)

#Дописав
def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        return HttpResponse(f"Username: {name}, password: {password}")
#Дописав

#Дописав
def course(request):
    if request.method == 'POST':
        course = request.POST.get('course')
        user = User()
        user.choose_course(course)
        context = {'user': user}
        return render(request, 'get_grade.html', context) #потім створю html
    else:
        return HttpResponse('Congratulations on the course method!')
#Дописав
def grade(request):
    user = User()
    grade = user.get_grade()
    context = {'user': user, 'grade': grade}
    return HttpResponse('Congratulations on the grade method!')
#Дописав