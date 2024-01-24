from django.shortcuts import render,redirect
from main import forms
from main import models

# Create your views here.


def restrarent_reg(request):
    if request.method == "POST":
        form = forms.rest_form(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/view_rest")
        else:
            return redirect('/add_rest')
    else:
        form = forms.rest_form()
        context = {'form':form}
        return render(request,'res_register.html',context)