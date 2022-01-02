import jwt

from django.http import JsonResponse

from .models     import User
from my_settings import SECRET_KEY, ALGORITHM

def login_decorator(func):
    def wrapper(self, request, *args, **kwargs):
    
        if "Authorization" not in request.headers:
            return JsonResponse({"error_code":"INVALID_LOGIN"}, status=401)
        
        token = request.headers["Authorization"] 

        try:
            data = jwt.decode(token, SECRET_KEY, ALGORITHM)

            user = User.objects.get(id = data["id"])
            request.user = user 

        except jwt.InvalidTokenError:
            return JsonResponse({"message": "INVALID_TOKEN"}, status = 400)

        except jwt.DecodeError: 
            return JsonResponse({"error_code" : "DECODE_ERROR"}, status = 401)

        except User.DoesNotExist:
            return JsonResponse({"error_code" : "UNKNOWN_USER"}, status = 401)

        return func(self, request, *args, **kwargs)

    return wrapper