from django.views.generic import View
from django.shortcuts import render, redirect
from django.contrib import messages


def run_generator(arg1, arg2):
    # Пробуем преобразовать строки в числа
    try:
        interval = int(arg1)
        col_steps = int(arg2)
        # Обрабатываем данные
        # ...
        answer = interval + col_steps
        # ...
        # strOut возвращает результат в терминал
        strOut = f"{answer}, '<- Your answer!'"
        return strOut

    except ValueError:
        # Выдаем ошибку, в случае неверного ввода данных
        print('Ввод только чисел!')

    return None

    
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


