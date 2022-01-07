from json.decoder import JSONDecodeError

from django.http                 import JsonResponse
from django.views                import View
from json.decoder                import JSONDecodeError
from django.core.exceptions      import FieldError

from .models            import Restaurant
from reviews.models     import Menu
from restaurants.models import Category, ImageCategory, Restaurant
from django.db.models.aggregates import Avg, Count
from django.db.models            import Q

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

class RestaurantListView(View):
    def get(self, request):
        try:
            category_dict = {
                'korean'   : '한식',
                'chinese'  : '중식',
                'japanese' : '일식'      
            }
            category_name   = request.GET.get('category', None)
            restaurant_name = request.GET.get('name', None)
            sorts           = request.GET.get('sort','name')

            q = Q()

            if category_name:
                q &= Q(name=category_dict[category_name])

            category      = Category.objects.filter(q)
            restaurants   = Restaurant.objects\
                            .annotate(avg_rating=Avg('review__rating'), review_count=Count('review'))\
                            .filter(category__in=category, ).order_by(sorts)
            print(restaurants.count(), restaurants[0].avg_rating)

            result = [{
                'id'      : restaurant.id,
                'name'    : restaurant.name,
                'rating'  : round(restaurant.avg_rating, 1) if restaurant.avg_rating else 0,
                'reviews' : restaurant.review_count,
                'image'   : restaurant.imagerestaurant_set.first().url,
            }for restaurant in restaurants]
            
            return JsonResponse({'result' : result}, status=200)
        
        except JSONDecodeError:
            return JsonResponse({'message' : 'JSON_DECODE_ERROR'}, status=400)

        except Category.DoesNotExist:
            return JsonResponse({'message' : 'Category_DoesNotExist'}, status=404)

        except KeyError:
            return JsonResponse({'message' : 'KEYERROR'}, status=401)

        except FieldError:
            return JsonResponse({'message' : 'Bad_Request'}, status=404)


class RestaurantDetailView(View):       
    def get(self, request, restaurant_id):
        try:
            restaurant = Restaurant.objects.get(id=restaurant_id)
            avg_rating = restaurant.review_set.aggregate(Avg('rating'))['rating__avg']
            
            result = {
                "id"             : restaurant.id,
                "name"           : restaurant.name,
                "restaurant_img" : restaurant.imagerestaurant_set.first().url,
                "phone"          : restaurant.phone,
                "address"        : restaurant.address,
                "rating"         : round(avg_rating, 1) if avg_rating else 0,
                "category"      : [{
                    "category_id"   : menu_type.id,
                    "category_name" : menu_type.name,
                    "food": [{
                        "id"    : menu.id,
                        "name"  : menu.name,
                        "price" : int(menu.price),
                        "image" : menu.imagemenu_set.first().url
                        } for menu in menu_type.group_menu.filter(restaurant=restaurant)]
                    }for menu_type in restaurant.menutype_set.all()]
                }
                
            return JsonResponse({"restaurants_detail": result}, status=200)
        
        except Restaurant.DoesNotExist:
            return JsonResponse({"message": "invalid_restaurant"}, status=404)