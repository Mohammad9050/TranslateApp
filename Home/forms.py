from django import forms

class WordForm(forms.Form):
    CHOICES =(
        ('english', 'English'),
        ('persian', 'Persian'),
        ('italian', 'Italian'),
        ('french', 'French'),
        ('turkish', 'Turkish'),
        ('arabic', 'Arabic')
        )
    word = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'class': 'word_text'}))
    lan1 = forms.ChoiceField(choices=CHOICES, required=False)
    lan2 = forms.ChoiceField(choices=CHOICES, required=False)
    