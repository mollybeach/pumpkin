from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature 

def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html',{'features': features})

# we have new variable that we get from feature.object.all() this variable is a list 
def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username already used')
                return redirect('register')
            else: 
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save();
                return redirect('login')
    else:
        messages.info(request, 'Passwords do not match ')
        return redirect('register')
    return render(request, 'register.html')
    
def counter(request):
    words = request.POST['words']
    amount_of_words = len(words.split())
    return render(request, 'counter.html', {'amount' : amount_of_words})


    '''
    feature1 = Feature()
    feature1.id = 0
    feature1.name = 'Fast'
    feature1.is_true = True
    feature1.details = 'Our Service is Very Quick '

    feature2 = Feature()
    feature2.id = 1
    feature2.name = 'Reliable'
    feature2.is_true = True
    feature2.details = 'Our Service is Very Reliable '

    feature3 = Feature()
    feature3.id = 2
    feature3.name = 'Easy to Use'
    feature3.is_true = True
    feature3.details = 'Our Service is Very Easy to use '

    feature4 = Feature()
    feature4.id = 4
    feature4.name = 'Affordable'
    feature4.is_true = False
    feature4.details = 'Our Service is Very affordable  '

    feature5 = Feature()
    feature5.id = 5
    feature5.name = 'Trustworthy'
    feature5.is_true = True
    feature5.details = 'Our Service is Very trusting  '
    
    features = [feature1, feature2, feature3, feature4, feature5]
    return render(request, 'index.html', {'features' : features}
    ) 
    #return render(request, 'index.html', context) 



#text = 'hey how ar ewe doing 
#print(len(text.splt())) count each word 

'''
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
