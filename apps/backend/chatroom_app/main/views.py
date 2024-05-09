from django.shortcuts import render
from django.http import HttpResponseRedirect
from Admin.form import send_messageForm
from Message.models import Massage
from User.models import User

def aadmin(request):
    users = User.objects.all()
    a=users.get(username='admin')
    y=users.get(username='yasin')
    if request.method == 'POST':
        form = send_messageForm(request.POST)
        if form.is_valid():
            Massage.objects.create(see=False, sender=a, receiver=y, text=form.cleaned_data['text'])
        return HttpResponseRedirect('/aadmin/')
    else:
        form = send_messageForm()
        return render(request, "test.html",{"form":form})
def index(request):
    users = User.objects.all()
    return render(request, "base.html", {"users":users})
