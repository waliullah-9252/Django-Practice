from django.shortcuts import render
from .forms import ExampleForm

# Create your views here.

def home(request):
    return render(request, 'first_app/home.html')

def django_form(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST, request.FILES)
        if form.is_valid():
            # file = form.cleaned_data['file']
            # with open('./first_app/upload/' + file.name, 'wb+') as destination:
            #     for chunk in file.chunks():
            #         destination.write(chunk)
            print(form.cleaned_data)
    else:
        form = ExampleForm()
    return render(request, 'first_app/django_form.html', {'form': form})
