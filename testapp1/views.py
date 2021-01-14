from django.shortcuts import render
from testapp1.forms import LoginForm
from django.template import loader
from django.http import HttpResponse
# Create your views here.


def index(request):
    return HttpResponse("Hello")
#CAN BE ACCESSED THROUGH http://127.0.0.1:8000/testapp1/next/


def responseform(request):
   #if form is submitted
   if request.method == 'POST':
      res_LoginForm = LoginForm(request.POST)

      if res_LoginForm.is_valid():
         res_user_name = res_LoginForm.cleaned_data['username']
         res_password = res_LoginForm.cleaned_data['password']
         res_captcha = res_LoginForm.cleaned_data['captcha']
         context = {
            'stored_username': res_user_name,
            'stored_password': res_password,
            'stored_captcha': res_captcha
         }
         return render(request, 'testapp1/response_received.html', context)
   else :
      form = LoginForm()
      return render(request, 'testapp1/response_form.html', {'form': form})
#CAN BE ACCESSED THROUGH 127.0.0.1:8000/testapp1/thankyou