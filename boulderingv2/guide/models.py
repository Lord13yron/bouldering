from django.contrib.auth.models import AbstractUser, User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models

# Create your models here.

class Zone(models.Model):
    name = models.CharField(max_length=100)
    

    def __str__(self):
        return self.name
    

class Area(models.Model):
    name = models.CharField(max_length=100)
    map = models.ImageField(null=True, blank=True)
    approach = models.TextField(null=True, blank=True)
    best_problems = models.CharField(max_length=200, null=True, blank=True)
    zone = models.ForeignKey(Zone, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    

class Problem(models.Model):
    area = models.ForeignKey(Area, blank=True, null=True, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=300)
    grade = models.PositiveIntegerField()
    fa = models.CharField(max_length=50)
    image = models.ImageField(null=True, blank=True)
    map_id = models.PositiveIntegerField(null=True, blank=True)
    avgrating = models.DecimalField(null=True, max_digits=3, decimal_places=2, default=0.00)
    avggrade = models.DecimalField(null=True, max_digits=3, decimal_places=2)

    def __str__(self):
        return f"{self.name} V{self.grade}"
    

class Profile(models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    favorites = models.ManyToManyField(Problem, blank=True, related_name="favorites")
    sends = models.ManyToManyField(Problem, blank=True, related_name="sends")
    
    def __str__(self):
        return f"{self.user}" 
    

class Rating(models.Model):
    user = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, blank=True, null=True, on_delete=models.CASCADE)
    user_rating = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(5)])
    user_grade = models.PositiveIntegerField(validators=[MinValueValidator(0), MaxValueValidator(17)])

    def __str__(self):
        return f"{self.user} - {self.problem}"
    

class Comment(models.Model):
    user = models.ForeignKey(Profile, blank=True, null=True, on_delete=models.CASCADE)
    problem = models.ForeignKey(Problem, blank=True, null=True, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    comment = models.TextField()

    def __str__(self):
        return f"{self.user} - {self.problem}"