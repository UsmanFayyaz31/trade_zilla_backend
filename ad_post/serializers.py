from rest_framework import serializers
from .models import AdPost


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
