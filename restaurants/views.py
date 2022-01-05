from django.http            import JsonResponse
from django.views           import View
from django.db.models       import Q

from .models        import Restaurant
from reviews.models import Review, MenuType, Menu

class DetailView(View):
    def get(self, request, restaurant_id):
        print("restaurant_id : ", restaurant_id)
        try:
            restaurant      = Restaurant.objects.get(id = restaurant_id)
            restaurant_img  = restaurant.imagerestaurant_set.all()[0]  #### 여기 이미지를 각 레스토랑 별로 매칭되는 로직 구현
            rating          = Review.objects.filter(restaurant_id = restaurant_id)[0] #### 여기 별점을 각 레스토랑 별로 매칭되는 로직 구현
            # 리뷰 구현칸
            signature_menu  = MenuType.objects.get(id=1)
            signature_menus = signature_menu.group_menu.all()
            season_menu = MenuType.objects.get(id=2)    
            season_menus = season_menu.group_menu.all()
            other_menu = MenuType.objects.get(id=3)
            other_menus = other_menu.group_menu.all()
            
            signature_list = []
            for signature in signature_menus:
                images = signature.imagemenu_set.all()
                signature_list.append({
                    "id"    : signature.id,
                    "name"  : signature.name,
                    "price" : int(signature.price),
                    "image" : images[0].url
                })
                
            season_list = []
            for season in season_menus:
                images = season.imagemenu_set.all()
                season_list.append({
                    "id"    : season.id,
                    "name"  : season.name,
                    "price" : int(season.price),
                    "image" : images[0].url
                })
            
            other_list = []
            for other in other_menus:
                images = other.imagemenu_set.all()
                other_list.append({
                    "id"    : other.id,
                    "name"  : other.name,
                    "price" : int(other.price),
                    "image" : images[0].url
                })

            data = {
                "id"             : restaurant.id,
                "name"           : restaurant.name,
                "restaurant_img" : restaurant_img.url,
                "rating"         : rating.rating,
                "signature_menu" : signature_list,
                "season_menu"    : season_list,
                "other_menu"     : other_list
            }
            return JsonResponse({"restaurants_detail": data}, status=200)

        except Restaurant.DoesNotExist:
            return JsonResponse({"message":"Restaurant_DoesNotExist"}, status=404)