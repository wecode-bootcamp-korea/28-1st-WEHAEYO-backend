import json

from django.db.models.aggregates import Avg, Count

from django.http                 import JsonResponse
from django.views                import View
from json.decoder                import JSONDecodeError

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

class ListPageView(View):
    def get(self, request):
        try:
            category_name = request.GET['category']
            sorts         = request.GET.get('sort','name')
            category      = Category.objects.get(name=category_name)
            restaurants   = Restaurant\
                          .objects\
                          .annotate(avg_rating=Avg('review__rating'), review_count=Count('review'))\
                          .filter(category=category)\
                          .order_by(sorts)
            result = [{
                'id'      : restaurant.id,
                'name'    : restaurant.name,
                'rating'  : restaurant.avg_rating,
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

        except:
            return JsonResponse({'message' : 'FAILED'}, status=400)
