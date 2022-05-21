from rest_framework import serializers
from .models import UploadImage, Customer, Tiers


class ListImageSerializer(serializers.ModelSerializer):
    """List images"""

    class Meta:
        model = UploadImage
        fields = ['user', 'image']


class ListUserSerializer(serializers.ModelSerializer):
    """List customers"""

    class Meta:
        model = Customer
        fields = '__all__'


class AddImageSerializer(serializers.ModelSerializer):
    """Add images"""

    class Meta:
        model = UploadImage
        fields = ['image']


class UserSerializer(serializers.ModelSerializer):
    """Customer(user) detail"""

    user = serializers.CharField(source='user.username', read_only=True)
    tiers = serializers.CharField(source='tiers.name', read_only=True)
    user_upload_image = serializers.SerializerMethodField('upload_image')

    def upload_image(self, requset):
        user_upload_image = UploadImage.objects.values('image')
        return user_upload_image

    class Meta:
        model = Customer
        fields = ['user', 'tiers', 'user_upload_image']


class TiersSerializer(serializers.ModelSerializer):
    """Tiers list and adding embedded tiers"""

    class Meta:
        model = Tiers
        fields = ['name', 'slug', 'size_thumbnail_image', 'size_thumbnail_image_two', 'url_original_image',
                  'random_expiring_url', 'link_expiration_date']