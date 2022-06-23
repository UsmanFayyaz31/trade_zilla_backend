from django.contrib import admin
from ad_post.models import AdPost, ExchangeRequest, FavoriteProduct
from users.models import User
from location.models import Location


class AdPostAdmin(admin.ModelAdmin):
    list_display = ('id', 'product_name', 'item_required', 'get_user_email', 'address', 'get_location')

    @admin.display(description='User Email')
    def get_user_email(self, obj):
        return User.objects.get(id=obj.user_id)

    @admin.display(description='Location')
    def get_location(self, obj):
        return Location.objects.get(id=obj.location_id)


class ExchangeWithRequestsAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'product', 'exchange_with')


class FavoriteProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'get_product_name', 'get_user_email')

    @admin.display(description='User Email')
    def get_user_email(self, obj):
        return User.objects.get(id=obj.user_id)

    @admin.display(description='Product Name')
    def get_product_name(self, obj):
        return AdPost.objects.get(id=obj.product_id)


# Register your models here.
admin.site.register(AdPost, AdPostAdmin)
admin.site.register(ExchangeRequest, ExchangeWithRequestsAdmin)
admin.site.register(FavoriteProduct, FavoriteProductsAdmin)
