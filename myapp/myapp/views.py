from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature 
def index(request):
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.details = 'Our Service is Very Quick '

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.details = 'Our Service is Very Reliable '

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy to Use'
    feature3.details = 'Our Service is Very Easy to use '

    feature4 = Feature()
    feature4.id = 3
    feature4.name = 'Affordable'
    feature4.details = 'Our Service is Very affordable  '
    
    return render(request, 'index.html', 
    {
    'feature1': feature1,
    'feature2': feature2, 
    'feature3': feature3, 
    'feature4': feature4}
    ) 
    #return render(request, 'index.html', context) 

def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'amount' : amount_of_words})

#text = 'hey how ar ewe doing 
#print(len(text.splt())) count each word 


'''    
    context = {
        'name' : 'Patrick',
        'age' : 23,
        'nationality' : 'British'
    }
    return HttpResponse('<h1> hey, Welcome </h1>')
    name = 'Patrick'
    return render(request, 'index.html', {'name': name})  #this , curly brace after index html 
    #is like a dictionary send variable to html file 
    #in html file change <p>Welcome , John/p>
    #to <p>Welcome , {{name}}/p>
    can also have user.name='Patrick'
''' 
