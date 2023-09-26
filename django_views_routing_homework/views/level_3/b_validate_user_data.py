"""
В этом задании вам нужно реализовать вьюху, которая валидирует данные о пользователе.

- получите json из тела запроса
- проверьте, что данные удовлетворяют нужным требованиям
- если удовлетворяют, то верните ответ со статусом 200 и телом `{"is_valid": true}`
- если нет, то верните ответ со статусом 200 и телом `{"is_valid": false}`
- если в теле запроса невалидный json, вернуть bad request

Условия, которым должны удовлетворять данные:
- есть поле full_name, в нём хранится строка от 5 до 256 символов
- есть поле email, в нём хранится строка, похожая на емейл
- есть поле registered_from, в нём одно из двух значений: website или mobile_app
- поле age необязательное: может быть, а может не быть. Если есть, то в нём хранится целое число
- других полей нет

Для тестирования рекомендую использовать Postman.
Когда будете писать код, не забывайте о читаемости, поддерживаемости и модульности.
"""
import json

from django.http import HttpResponse, HttpRequest, JsonResponse, HttpResponseNotAllowed
from django.core.validators import validate_email
from django.core.exceptions import ValidationError


def is_full_name_valid(data: dict[str, str]) -> bool:
    if data.get('full_name'):
        return len(data['full_name']) >= 5 and len(data['full_name']) <= 256
    return None


def is_email_valid(data: dict[str, str]) -> bool:
    if data.get('email'):
        try:
            validate_email(data['email'])
            return True
        except ValidationError:
            return False


def is_registered_from_valid(data: dict[str, str]) -> bool:
    if data.get('registered_from'):
        return data['registered_from'] in ["website", "mobile_app"]
    return None


def is_age_valid(data: dict[str, str]) -> bool:
    if data.get('age'):
        return isinstance(data['age'], int)
    return None


def validate_user_data_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            if data.get('age'):
                if is_full_name_valid(data) and is_email_valid(data) \
                    and is_registered_from_valid(data) and is_age_valid(data):
                    return JsonResponse(data={"is_valid": True}, safe=False, status=200)
                
                return JsonResponse(data={"is_valid": False}, safe=False, status=200)

            if is_full_name_valid(data) and is_email_valid(data) \
                and is_registered_from_valid(data):
                return JsonResponse(data={"is_valid": True}, safe=False, status=200)
            
            return JsonResponse(data={"is_valid": False}, safe=False, status=200)
        except Exception:
            return JsonResponse(data={}, status=400)
    
    return HttpResponseNotAllowed(permitted_methods=['POST'])
