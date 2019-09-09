from django import forms
from .models import Project, Profile, Review


class UploadForm(forms.ModelForm):
    class Meta:
        model = Project
        exclude = ('design', 'usability', 'creativity', 'content', 'overall', 'posted', 'user' )



class ReviewForm(forms.ModelForm):
    class Meta:
        model=Review
        exclude=['overall_score','profile','project']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('profile_photo','bio', 'contact')