from django.contrib import messages
from django.db.models import Sum
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse

from .forms import ProblemForm
from .models import Zone, Area, Problem, Rating, Comment

# Create your views here.

def index(request):
    return render(request, "guide/index.html",{})


def zones(request):
    return render(request, "guide/zones.html", {
        'areas': Area.objects.all(),
        'zones': Zone.objects.all()
    })


def area(request, area_name):
    area = Area.objects.get(name=area_name)
    name = area.name
    problems = Problem.objects.filter(area=area).order_by('map_id')
    
    return render(request, "guide/area.html" ,{
        "area": area,
        "problems": problems,
        'areas': Area.objects.all(),
        'zones': Zone.objects.all(),
    })

def problem(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    current_user = request.user
    return render(request, "guide/problem.html" ,{
        "problem": problem,
        'areas': Area.objects.all(),
        'zones': Zone.objects.all(),
        'favorites':  current_user.profile.favorites.all(),
        'sends': current_user.profile.sends.all(),
        'comments': Comment.objects.filter(problem=problem_id).order_by('created')
        
    })

def problems(request):
    return render(request, "guide/problems.html", {
        "problems": Problem.objects.all(),
        'areas': Area.objects.all(),
        'zones': Zone.objects.all(),
    })

def addproblem(request):
    if request.method == "POST" and request.FILES:
        form = ProblemForm(request.POST, request.FILES)
        area_id = request.POST["area"]
        area = Area.objects.get(id=area_id)
        if form.is_valid():
            problem = Problem(
                        area=area,
                        name=request.POST["name"],
                        description=request.POST["description"],
                        grade=request.POST["grade"],
                        fa=request.POST["fa"],
                        image=request.FILES["image"]
                        )
            problem.save()
            messages.success(request, "Problem sumitted successfully!")
            return redirect('addproblem')
    elif request.method == "POST":
        form = ProblemForm(request.POST)
        area_id = request.POST["area"]
        area = Area.objects.get(id=area_id)
        if form.is_valid():
            problem = Problem(
                        area=area,
                        name=request.POST["name"],
                        description=request.POST["description"],
                        grade=request.POST["grade"],
                        fa=request.POST["fa"],
                        )
            problem.save()
            messages.success(request, "Problem sumitted successfully!")
            return redirect('addproblem')
    else:
        form= ProblemForm()
    
    return render(request, "guide/addproblem.html",{
        'form': form,
        'areas': Area.objects.all(),
        'zones': Zone.objects.all()
    })

def search(request):
    if request.method == "POST":
        searched = request.POST['searched']
        problems = Problem.objects.filter(name__contains=searched).order_by("name")
        return render(request, "guide/search.html",{
            "searched": searched,
            "problems": problems,
            'areas': Area.objects.all(),
            'zones': Zone.objects.all(),
        })
    else:
        return render(request, "guide/search.html",{})
    
def addfavorite(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    current_user = request.user
    current_user.profile.favorites.add(problem)
    messages.success(request, "Problem added to favorites!")
    return redirect(f'/problem/{problem_id}', {
        'problem_id': problem_id
    })

def removefavorite(request, problem_id):
    problem = Problem.objects.get(id=problem_id)
    current_user = request.user
    current_user.profile.favorites.remove(problem)
    messages.success(request, "Problem removed from favorites!")
    return redirect(f'/problem/{problem_id}')

def profile(request):
    current_user = request.user
    return render(request, "guide/profile.html",{
        "user": current_user,
        'favorites':  current_user.profile.favorites.all(),
        "problems": Problem.objects.all(),
        'sends':  current_user.profile.sends.all(),
        
    })

 

def ratings(request, problem_id):
    if request.method == "POST" and request.POST.get('rating'):
        current_user = request.user.profile
        problem = Problem.objects.get(id=problem_id)
        current_user.sends.add(problem)
        rating = Rating(
            problem = problem, 
            user = current_user, 
            user_rating = request.POST.get('rating', False),
            user_grade = request.POST.get('grade', False)
        )
        rating.save()

        rating_sum = 0
        count = 0
        ratings = Rating.objects.all()
        for rating in ratings:
            if rating.problem == problem:
                rating_sum += rating.user_rating
                count += 1
        rating = rating_sum / count
        problem.avgrating = rating
        problem.save()

        grade_sum = 0
        grade_count = 0
        ratings = Rating.objects.all()
        for rating in ratings:
            if rating.problem == problem:
                grade_sum += rating.user_grade
                grade_count += 1
        grade = grade_sum / grade_count
        problem.avggrade = grade
        problem.save()


        messages.success(request, "Problem added to sends!")
        #return redirect(f'/problem/{problem_id}')
        return HttpResponseRedirect(reverse('problem', kwargs={'problem_id': problem_id}))
    return render(request, 'guide/ratings.html',{
      'problem': Problem.objects.get(id=problem_id)
    })


def addcomment(request, problem_id):
    return redirect(f'/problem/{problem_id}')