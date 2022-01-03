import json
import bcrypt

import jwt
from datetime               import datetime, timedelta
from json.decoder           import JSONDecodeError

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from .models                import User
from utils.validations      import is_valid_email, is_valid_password
from my_settings            import SECRET_KEY, ALGORITHM

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)

        try:
            name         = data['name']
            password     = data['password']
            email        = data['email']
            phone_number = data['phone_number']

            if not is_valid_email(email):
                raise ValidationError('INVALID_EMAIL')
            
            if not is_valid_password(password):
                raise ValidationError('INVALID_PASSWORD')
                
            if User.objects.filter(email=email).exists():
                raise ValidationError('DUPLICATED_EMAIL')

            hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                name         = name,
                password     = hashed_password,
                email        = email,
                phone_number = phone_number
            )

            return JsonResponse({'message' : 'created'}, status=201)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except ValidationError as e:
            return JsonResponse({"message": e.message}, status=400)

        except JSONDecodeError:
            return JsonResponse({'message':'INVALID_JSON_FORMAT'}, status=400)

class LoginView(View):
    def post(self, request):
        data = json.loads(request.body) 
        
        try:
            email    = data['email']
            password = data['password']

            if not User.objects.filter(email=email).exists():
                raise ValidationError('INVALID_USER')

            user_info = User.objects.get(email=email)

            hashed_password = user_info.password.encode("utf-8")

            if not bcrypt.checkpw(password.encode('utf-8'), hashed_password):
                raise ValidationError('INVALID_PASSWORD')
            
            payload = {
                "id" : user_info.id,
                "exp"     : datetime.now() + timedelta(days=3),
                "iat"     : datetime.now()
            }
            token = jwt.encode(payload, SECRET_KEY, ALGORITHM)
            
            return JsonResponse({'token' : token}, status=200)

        except KeyError:
            return JsonResponse({"message": "KEY_ERROR"}, status=400)

        except ValidationError as e:
            return JsonResponse({"message": e.message}, status=401)

        except JSONDecodeError:
            return JsonResponse({'message':' INVALID_JSON_FORMAT'}, status=400)