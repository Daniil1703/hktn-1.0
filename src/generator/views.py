from django.views.generic import View
from django.shortcuts import render, redirect

class SendData(View):
    def get(self, request):
        return render(request, template_name='index.html', context=None)

    def post(self, request):
        col_steps = request.POST['col_steps']
        print(col_steps)
        interval = request.POST['interval']
        print(interval)
        return redirect('generator:index')


