from django import forms
from .models import Area

class ProblemForm(forms.Form):
    areas = Area.objects.all()
    area = forms.ModelChoiceField(label="Area", queryset=areas, empty_label="New Zone")
    name = forms.CharField(label="Name", max_length=100)
    description = forms.CharField(label="Description", max_length=300, widget=forms.Textarea)
    grade = forms.IntegerField(label="Grade V:", min_value=0, max_value=17)
    fa = forms.CharField(label="First Ascent", max_length=50)
    image = forms.ImageField(label="Image", required=False)
