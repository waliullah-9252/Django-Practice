from django.shortcuts import render
import datetime

# Create your views here.

def home(request):

    d = {'author': 'Humayoun Ahmed', 'age': 55, 'List' : ['Django', 'is', 'a', 'most', 'useful', 'framwork',], 'today' : datetime.datetime.now(), 'value' : 'welcome to django course.', 'val' : 'Welcome To Our Django Course', "size" : 23454345, 'student' : [
        {
            'name' : 'Waliullah',
            'age' : 23,
        },
        {
            'name' : 'Abdullah',
            'age' : 22,
        },
        {
            'name' : 'Tamim',
            'age' : 22,
        },
    ],
         
         
         
         
         
    }
    return render(request, 'first_app/home.html' , d)
