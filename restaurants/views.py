from json.decoder import JSONDecodeError

from django.http                 import JsonResponse
from django.views                import View
from django.db.models.aggregates import Avg, Count

from .models            import Restaurant
from reviews.models     import Menu
from restaurants.models import Category, ImageCategory, Restaurant

class CategoryMainView(View):
    def get(self, request):
        try:
            categories    = Category.objects.all()
            food_category = [{
                    'category_name': category.name,
                    'image_url'    : ImageCategory.objects.get(category=category).url,
                }for category in categories]
                
            return JsonResponse({'result' : food_category}, status=200)

        except JSONDecodeError:
            return JsonResponse({'message' : 'JSON_DECODE_ERROR'}, status=400) 
            
        except:
            return JsonResponse({'message' : 'FAILED'}, status=400)

class RestaurantDetailView(View):
    def get(self, request, restaurant_id):
        try:
            restaurant        = Restaurant.objects.get(id = restaurant_id)
            restaurant.rating = round(float(restaurant.review_set.aggregate(Avg('rating'))['rating__avg']),1)

            result = {
                "id"             : restaurant.id,
                "name"           : restaurant.name,
                "restaurant_img" : restaurant.imagerestaurant_set.first().url,
                "rating"         : restaurant.rating,
                "menu_type"      : [{
                    "menu_type_id"   : menu_type.id,
                    "menu_type_name" : menu_type.name,
                    "food": [{
                        "id"    : menu.id,
                        "name"  : menu.name,
                        "price" : int(menu.price),
                        "image" : menu.imagemenu_set.first().url
                    } for menu in Menu.objects.filter(restaurant=restaurant)]
                }for menu_type in restaurant.menutype_set.all()]
            }
            
            return JsonResponse({"restaurants_detail": result}, status=200)

        except Restaurant.DoesNotExist:
            return JsonResponse({"message":"Restaurant_DoesNotExist"}, status=404)
