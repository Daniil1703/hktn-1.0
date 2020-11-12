def run_generator(arg1, arg2):
    try:
        # Пробуем преобразовать строки в числа
        interval = int(arg1)
        col_steps = int(arg2)
        # Обрабатываем данные
        # ...
        answer = interval + col_steps
        # ...
        # strOut возвращает результат в терминал
        strOut = f"{answer} <- Your answer!"
        return strOut

    except ValueError:
        # Выдаем ошибку, в случае неверного ввода данных
        print('Ввод только чисел!')

    return None