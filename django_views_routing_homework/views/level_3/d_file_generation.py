"""
В этом задании вам нужно научиться генерировать текст заданной длинны и возвращать его в ответе в виде файла.

- ручка должна получать длину генерируемого текста из get-параметра length;
- дальше вы должны сгенерировать случайный текст заданной длины. Это можно сделать и руками
  и с помощью сторонних библиотек, например, faker или lorem;
- дальше вы должны вернуть этот текст, но не в ответе, а в виде файла;
- если параметр length не указан или слишком большой, верните пустой ответ со статусом 403

Вот пример ручки, которая возвращает csv-файл: https://docs.djangoproject.com/en/4.2/howto/outputting-csv/
С текстовым всё похоже.

Для проверки используйте браузер: когда ручка правильно работает, при попытке зайти на неё, браузер должен
скачивать сгенерированный файл.
"""

from faker import Faker   
from django.http import HttpResponse, HttpRequest, HttpResponseNotAllowed


def generate_file_with_text_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if not request.GET.get('length'):
          return HttpResponse("Only 'length' paramter is allowed")
        
        length_param = request.GET.get('length')

        try:
           length_param = int(length_param)
        except:
           return HttpResponse("Only integer value is allowed")
        
        faker = Faker() 
        generate_text = faker.text(max_nb_chars=length_param)

        response = HttpResponse(
            headers = {
              "Content-Type": "text/plain",
              "Content-Disposition": 'attachment; filename="file.txt"',
              }
        )
        response.write(generate_text)
        
        return response

    return HttpResponseNotAllowed(permitted_methods=['GET'])
