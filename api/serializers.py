from rest_framework import serializers

from .models import Url


class UrlSerializer(serializers.HyperlinkedModelSerializer):
    shorten = serializers.SlugField(required=False)

    class Meta:
        model = Url
        fields = "__all__"
        read_only_fields = ("count",)

    def validate_shorten(self, value):
        if value[0].isdigit():
            raise serializers.ValidationError(
                "Cтрока обязательно должна начинаться с буквы"
            )
        if Url.objects.all().filter(shorten=value):
            raise serializers.ValidationError(
                "Этот адрес уже занят!"
            )
        return value
