from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("zones", views.zones, name="zones"),
    path("area/<str:area_name>", views.area, name="area"),
    path("problem/<int:problem_id>", views.problem, name="problem"),
    path("problems", views.problems, name="problems"),
    path("addproblem", views.addproblem, name="addproblem"),
    path("search", views.search, name="search"),
    path("addfavorite<int:problem_id>", views.addfavorite, name="addfavorite"),
    path("removefavorite/<int:problem_id>", views.removefavorite, name="removefavorite"),
    path("profile", views.profile, name="profile"),
    path("ratings/<int:problem_id>", views.ratings, name="ratings"),
    path("addcomment/<int:problem_id>", views.addcomment, name="addcomment"),
    
]