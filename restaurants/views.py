import json

from django.http        import JsonResponse
from django.views       import View
from json.decoder       import JSONDecodeError

from restaurants.models import Category, ImageCategory, Restaurant, ImageRestaurant
from reviews.models     import Review

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
            rating_sum = request.GET.get('rating')