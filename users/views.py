import json
import bcrypt

from django.http            import JsonResponse
from django.views           import View
from django.core.exceptions import ValidationError

from .models      import User
from .validations import is_email_valid, is_password_valid

class SignupView(View):
    def post(self, request):
        data = json.loads(request.body)
        try:
            name         = data['name']
            password     = data['password']
            email        = data['email']
            phone_number = data['phone_number']

            if not is_email_valid(email):
                raise ValidationError('INVALID_EMAIL')
            
            if not is_password_valid(password):
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
