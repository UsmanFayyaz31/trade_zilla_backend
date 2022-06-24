from rest_framework import serializers
from .models import AdPost, ExchangeRequest, FavoriteProduct


class AdPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdPost
        fields = ("product_name",
                  "description",
                  "item_required",
                  "location",
                  "user",
                  'category',
                  "address",
                  "product_image")

    def create(self, validated_data):
        ad_post = AdPost.objects.create(
            product_name=validated_data['product_name'],
            description=validated_data['description'],
            item_required=validated_data['item_required'],
            location_id=validated_data['location'].id,
            user_id=validated_data['user'].id,
            category_id=validated_data['category'].id,
            address=validated_data['address'],
            product_image=validated_data['product_image']
        )

        return ad_post


class ExchangeRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeRequest
        fields = ("exchange_with", "user", "product")

    def create(self, validated_data):
        exchange_request = ExchangeRequest.objects.create(
            exchange_with=validated_data['exchange_with'],
            user_id=validated_data['user'].id,
            product_id=validated_data['product'].id
        )

        return exchange_request


class FavoriteProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteProduct
        fields = ("user", "product")

    def create(self, validated_data):
        favorite_product = FavoriteProduct.objects.create(
            user_id=validated_data['user'].id,
            product_id=validated_data['product'].id
        )

        return favorite_product
