from django.http        import JsonResponse
from django.views       import View

from restaurants.models import Category, ImageCategory

class CategoryMainView(View):
    def get(self, request):
        try:
            categories    = Category.objects.all()
            food_category = [
                {
                    'category_name': category.name,
                    'image_url'    : ImageCategory.objects.get(category=category).url,
                }for category in categories
            ]
                
            return JsonResponse({'result' : food_category}, status=200) 
            
        except:
            return JsonResponse({'Message' : 'FAILED'}, status=400)