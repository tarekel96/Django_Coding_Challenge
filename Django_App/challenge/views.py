from django.shortcuts import render
from django.http import HttpResponse
from .userController import *
from .forms import ProfileForm

# Create your views here.


def home(request, id=1):
    user = user_by_id(id)
    id = user.id
    context = {'user': user, 'id': id}
    return render(request, 'challenge/home.html', context)


def profile(request, id=1):
    user = user_by_id(id)
    id = user.id
    form = ProfileForm(request.POST or None, instance=user)
    context = {'user': user, 'id': id, "form": form}
    message = ""
    # HANDLE FORM DATA
    if request.method == "POST":
        # binding data to the form
        form.save(commit=True)
        if form.is_valid():
            return render(request, 'challenge/profile.html', context)

# return HttpResponse('Success')
        else:
            return HttpResponse('ERROR')
    return render(request, 'challenge/profile.html', context)
