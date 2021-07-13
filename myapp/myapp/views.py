from django.shortcuts import render
from django.http import HttpResponse
def index(request):
    context = {
        'name' : 'Patrick',
        'age' : 23,
        'nationality' : 'British'
    }
    return render(request, 'index.html', context) 
def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'amount' : amount_of_words})

#text = 'hey how ar ewe doing 
#print(len(text.splt())) count each word 


'''
    return HttpResponse('<h1> hey, Welcome </h1>')
    name = 'Patrick'
    return render(request, 'index.html', {'name': name})  #this , curly brace after index html 
    #is like a dictionary send variable to html file 
    #in html file change <p>Welcome , John/p>
    #to <p>Welcome , {{name}}/p>
    can also have user.name='Patrick'
''' 
