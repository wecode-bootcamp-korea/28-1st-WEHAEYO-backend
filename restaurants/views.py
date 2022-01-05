import json

from django.db.models.aggregates import Avg, Count
from django.db.models            import Q

from django.http                 import JsonResponse
from django.views                import View
from json.decoder                import JSONDecodeError
from django.core.exceptions      import FieldError

from restaurants.models          import Category, ImageCategory, Restaurant, ImageRestaurant

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
            category_name   = request.GET.get('category',None)
            restaurant_name = request.GET.get('name',None)
            sorts           = request.GET.get('sort','name')

            q = Q()

            if category_name:
                q &= Q(name=category_dict[category_name])

            category      = Category.objects.filter(q)
            restaurants   = Restaurant.objects\
                            .annotate(avg_rating=Avg('review__rating'), review_count=Count('review'))\
                            .filter(category__in=category, ).order_by(sorts)
            print(restaurants.count(), restaurants[0].avg_rating)

            round_avg = lambda mean_value : round(mean_value,1) if mean_value else mean_value

            result = [{
                'id'      : restaurant.id,
                'name'    : restaurant.name,
                'rating'  : round_avg(restaurant.avg_rating),
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