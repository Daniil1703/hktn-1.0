from django.views.generic import View
from .generator import run_generator
from django.shortcuts import render, redirect
from django.contrib import messages


    
class SendData(View):
    message_succ = 'Данные успешно отправлены!'
    message_error = 'данные введены неверно'

    def get(self, request):
        return render(request, template_name='index.html', context=None)

    def post(self, request):
        col_steps = request.POST['col_steps']
        interval = request.POST['interval']
        if run_generator(col_steps, interval) == None:
            messages.error(request, self.message_error)
        else:
            print(run_generator(col_steps, interval))
            messages.success(request, self.message_succ)
        return redirect('generator:index')


