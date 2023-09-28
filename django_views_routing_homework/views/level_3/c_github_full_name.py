"""
В этом задании вам нужно реализовать ручку, которая принимает на вход ник пользователя на Github,
а возвращает полное имя этого пользователя.

- имя пользователя вы узнаёте из урла
- используя АПИ Гитхаба, получите информацию об этом пользователе (это можно сделать тут: https://api.github.com/users/USERNAME)
- из ответа Гитхаба извлеките имя и верните его в теле ответа: `{"name": "Ilya Lebedev"}`
- если пользователя на Гитхабе нет, верните ответ с пустым телом и статусом 404
- если пользователь на Гитхабе есть, но имя у него не указано, верните None вместо имени
"""
import requests
from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseNotAllowed


URL = "https://api.github.com/users"


def fetch_name_from_github_view(request: HttpRequest, github_username: str) -> JsonResponse | HttpResponse:
    if request.method == 'GET':
        try:
            github_response = requests.get(f"{URL}/{github_username}")
            
            if github_response.status_code == 200:
                github_name = github_response.json().get('name')
                if github_name:
                    return JsonResponse(data={"name": github_name}, safe=False, status=200)
                return JsonResponse(data={"name": None}, safe=False, status=200)
            
            if github_response.status_code == 404:
                return JsonResponse(data={}, safe=False, status=404)
            
        except Exception as e:
            print(e)
    
    return HttpResponseNotAllowed(permitted_methods=['GET'])
