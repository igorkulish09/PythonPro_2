from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import User, WeekDay
from django.template import loader
from django.shortcuts import get_object_or_404

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

def login(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        return HttpResponse(f"Username: {name}, password: {password}")

def my_week(request):

    template = loader.get_template("my_app/week.html")
    context = {
        "days": WeekDay.objects.all()
    }

    return HttpResponse(template.render(context, request))

def my_day(request, week_day_id):
    day = get_object_or_404(WeekDay, pk=week_day_id)
    #day = WeekDay.objects.get(pk=week_day_id)
    return render(request, "my_app/week_day.html", {"week_day": day})
