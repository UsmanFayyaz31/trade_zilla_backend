from rest_framework import serializers
from .models import AdPost, ExchangeRequest


class AdPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdPost
        fields = ("product_name",
                  "description",
                  "item_required",
                  "location",
                  "user",
                  "address")

    def create(self, validated_data):
        ad_post = AdPost.objects.create(
            product_name=validated_data['product_name'],
            description=validated_data['description'],
            item_required=validated_data['item_required'],
            location_id=validated_data['location'].id,
            user_id=validated_data['user'].id,
            address=validated_data['address']
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
