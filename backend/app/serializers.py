from rest_framework import serializers

from backend.app.models import CarImage, AIAnalyse


class CarImageSerialaizer(serializers.ModelSerializer):
    class Meta:
        model = CarImage
        fields = ("id", "owner", "image")


    def validate_image(self, value):
        """
        Validate uploaded image:
        - Format: JPEG or PNG
        """

        if not value.content_type in ["image/jpeg", "image/png"]:
            raise serializers.ValidationError("Only JPEG and PNG formats are supported.")

        return value


class AIAnalyseSerializer(serializers.ModelSerializer):
    format_price = serializers.SerializerMethodField()
    format_date = serializers.SerializerMethodField()

    class Meta:
        model = AIAnalyse
        fields = ("id", "estimated_price", "analyse", "evaluated_at", "format_price", "format_date")

    def get_format_price(self, obj):
        return obj.format_price()

    def get_format_date(self, obj):
        return obj.format_date()

