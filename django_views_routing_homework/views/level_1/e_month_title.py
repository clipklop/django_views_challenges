from django.http import HttpResponse, HttpResponseNotFound
from django.http import JsonResponse


"""
Вьюха get_month_title_view возвращает название месяца по его номеру. 
Вся логика работы должна происходить в функции get_month_title_by_number.

Задания:
    1. Напишите логику получения названия месяца по его номеру в функции get_month_title_by_number
    2. Если месяца по номеру нет, то должен возвращаться ответ типа HttpResponseNotFound c любым сообщением об ошибке
    3. Добавьте путь в файле urls.py, чтобы при открытии http://127.0.0.1:8000/month-title/тут номер месяца/ 
       вызывалась вьюха get_month_title_view. Например http://127.0.0.1:8000/month-title/3/ 
"""
MONTH_MAPPER = {
        1: 'January',
        2: 'February',
        3: 'March',
        4: 'April',
        5: 'May',
        6: 'June',
        7: 'July',
        8: 'August',
        9: 'September',
        10: 'October',
        11: 'November',
        12: 'December'
    }

def get_month_title_by_number(month_number: int):
    return MONTH_MAPPER.get(month_number)


def get_month_title_view(request, month_number: int):
    # код писать тут
    if get_month_title_by_number(month_number):
        return JsonResponse(data=MONTH_MAPPER[month_number], safe=False)
    
    return HttpResponseNotFound('Месяца с таким номером не существует')
