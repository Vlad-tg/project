from django.core.files.uploadedfile import SimpleUploadedFile
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from main.models import Tiers, UploadImage, User, image_thumbnail_path, Customer


class TiersTest(TestCase):
    """Test tiers"""

    @classmethod
    def setUpTestData(cls):
        Tiers.objects.create(name='Basic', slug='basic', size_thumbnail_image='200',
                             size_thumbnail_image_two='0', url_original_image='False',
                             random_expiring_url='None', link_expiration_date='300')

    def test_field_name(self):
        new_image = Tiers.objects.get(pk=1)
        max_length = new_image._meta.get_field('name').max_length
        self.assertEqual(max_length, 255)


class ImageUploadTest(TestCase):
    """Test uploading image in media file"""

    @classmethod
    def setUpTestData(cls):
        user = User.objects.create_user(username='admin1', password='52asfD')

        UploadImage.objects.create(user=user,
                                   image='img/test_image.jpg',
                                   thumbnail_image='img_thumbnail/test_image.jpg',
                                   thumbnail_image_two='img_thumbnail_two/test_image.jpg'
                                   )

    def test_add_image(self):
        new_image = UploadImage()

        new_image.image = SimpleUploadedFile(name='test_image.jpg',
                                             content=open('media/img/test_image.jpg', 'rb').read()
                                             )
        new_image.save()
        self.assertEqual(UploadImage.objects.count(), 1)


class CustomerListViewTest(TestCase):
    """Test customer list"""

    def test_view_url_customer_list(self):
        resp = self.client.get(reverse('user_list'))
        self.assertEqual(resp.status_code, 200)


class CustomerDetailViewTest(TestCase):
    """Test customer detail"""

    def test_view_url_customer_detail(self):
        user = Customer.objects.all()
        for u in user:
            resp = self.client.get(reverse('detail_image pk=u.pk username=u.user.username'))
            self.assertEqual(resp.status_code, 200)


class ImageTests(APITestCase):
    """Image(post) test"""

    def test_create_account(self):
        user = Customer.objects.all()
        for u in user:
            url = reverse('detail_image pk=u.pk username=u.user.username')
            data = {'name': 'DabApps'}
            response = self.client.post(url, data, format='json')
            self.assertEqual(response.status_code, status.HTTP_201_CREATED)
            self.assertEqual(UploadImage.objects.count(), 10)
            self.assertEqual(UploadImage.objects.get().name, 'DabApps')




