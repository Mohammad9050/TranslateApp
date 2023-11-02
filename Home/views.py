from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import requests
from django.urls import reverse
from .forms import WordForm
from account.models import UserWords


def home_view(request):
    result = ''
    result2 = []
    if request.method == 'POST':
        form = WordForm(request.POST)
        if form.is_valid():
            word = form.cleaned_data['word']
            lan1 = form.cleaned_data['lan1']
            lan2 = form.cleaned_data['lan2']
            url = f'https://api.mymemory.translated.net/get?q={word}&langpair={lan1}|{lan2}'
            
       
            j_data = requests.get(url).json()
            result = j_data['responseData']["translatedText"]
            result2 = list(set([i['translation'] for i in j_data['matches']]))
            request.session['word'] = word
            request.session['word2'] = result
    else:
        form = WordForm()

    return render(request, 'Home/home.html', {'form':form, 'result':result, 'result2':result2})


def saving_view(request):
    word = request.session['word']
    word2 = request.session['word2']

    obj = UserWords.objects.get_or_create(user=request.user, first_word=word, second_word=word2)
   # obj.save()
    return HttpResponseRedirect(reverse('home'))
    

def saved_view(request):
    user = request.user
    words = UserWords.objects.filter(user=user).order_by('date')[:20]
    return render(request,'Home/saved.html' ,{'words':words})