from django.http import JsonResponse
from django.views import View

from restaurants.models import Category, ImageCategory

class CategoryMainView(View):
    def get(self, request):
        try:
            categories=Category.objects.all()
            food_category = []
            for category in categories:
                images=ImageCategory.objects.get(category=category)
                food_category.append({
                    'category_name':category.name,
                    'image_url':images.url,
                })
            return JsonResponse({'RESULT' : food_category}, status=200) 
        except:
            return JsonResponse({'Message' : 'FAILED'}, status=400) 