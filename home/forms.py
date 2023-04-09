from django import forms
from .models import Article

class Add_Article(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['category_id', 'title', 'desc', 'created_by']

        widgets = {
            'category_id': forms.Select(attrs={'class': 'form-control'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'desc': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Article Description..'}),
            'created_by': forms.TextInput(attrs={'class': 'form-control'}),
        }