from django.contrib.sites.shortcuts import get_current_site
from django.core.files.storage import FileSystemStorage
from django.shortcuts import redirect
from django.conf import settings
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from django.core.mail import EmailMessage
from .serializers import *
from rest_framework import viewsets


class ListImageView(viewsets.ModelViewSet):
    """List images"""

    queryset = UploadImage.objects.all()
    serializer_class = ListImageSerializer


class TiersView(viewsets.ModelViewSet):
    """Tiers list"""

    queryset = Tiers.objects.all()
    serializer_class = TiersSerializer


class AddTiersView(APIView):
    """Adding embedded tiers"""

    def get(self, request):
        create_tiers_basic, __ = Tiers.objects.get_or_create(name='Basic', slug='basic', size_thumbnail_image='200',
                                                             size_thumbnail_image_two='0', url_original_image='False',
                                                             random_expiring_url='None', link_expiration_date='300')
        create_tiers_premium, __ = Tiers.objects.get_or_create(name='Premium', slug='premium',
                                                               size_thumbnail_image='200',
                                                               size_thumbnail_image_two='400',
                                                               url_original_image='True',
                                                               random_expiring_url='None', link_expiration_date='300')

        create_tiers_enterprise, __ = Tiers.objects.get_or_create(name='Enterprise', slug='enterprise',
                                                                  size_thumbnail_image='200',
                                                                  size_thumbnail_image_two='400',
                                                                  url_original_image='True',
                                                                  random_expiring_url='http://127.0.0.1:8000/30df5d751a3489a87370956ab9558b30',
                                                                  link_expiration_date='300')
        serializer = TiersSerializer()
        return Response(serializer.data)


class ListUserView(APIView):
    """List customers"""

    def get(self, request):
        customer = Customer.objects.all()
        serializer = ListUserSerializer(customer, many=True)
        return Response(serializer.data)


class DetailUserView(APIView):
    """Customer(user) detail"""

    serializer_class = AddImageSerializer

    def get(self, request, pk, username):
        customer = Customer.objects.filter(pk=pk)

        for u in customer:
            if u.user.username == username:
                if request.user.is_authenticated:
                    serializer = UserSerializer(customer, many=True)
                else:
                    return redirect("user_list")
            else:
                return redirect("user_list")
            return Response(serializer.data)

    def post(self, request, pk, username, *args, **kwargs):
        image_data = request.data
        customer = Customer.objects.filter(pk=pk)
        for u in customer:

            new_image = UploadImage.objects.create(user=request.user, image=image_data["image"],
                                                   thumbnail_image=image_data["image"],
                                                   thumbnail_image_two=image_data["image"]
                                                   )
            serializer = AddImageSerializer(new_image)
            new_image.save()

            email_subject = 'Your present for {} plan'.format(u.tiers.name)
            current_site = get_current_site(request)
            fs = FileSystemStorage()

            if u.tiers.size_thumbnail_image > 0 and u.tiers.size_thumbnail_image_two > 0 \
                    and u.tiers.url_original_image == 'True' and u.tiers.random_expiring_url != 'None':
                email = EmailMessage(
                    email_subject,
                    'Hi ' + u.user.username + ', thanks you for trusting us. \n' +
                    'Your present: \n' +
                    '1. ' + current_site.domain + fs.url(new_image.thumbnail_image) + '\n' +
                    '2. ' + current_site.domain + fs.url(new_image.thumbnail_image_two) + '\n' +
                    '3. ' + current_site.domain + fs.url(new_image.image) + '\n' +
                    '4. ' + u.tiers.random_expiring_url,
                    settings.EMAIL_HOST_USER,
                    [u.user.email],
                )
                email.send(fail_silently=False)

            elif u.tiers.size_thumbnail_image > 0 and u.tiers.size_thumbnail_image_two > 0 \
                    and u.tiers.url_original_image == 'True' and u.tiers.random_expiring_url == 'None':
                email = EmailMessage(
                    email_subject,
                    'Hi ' + u.user.username + ', thanks you for trusting us. \n' +
                    'Your present: \n' +
                    '1. ' + current_site.domain + fs.url(new_image.thumbnail_image) + '\n' +
                    '2. ' + current_site.domain + fs.url(new_image.thumbnail_image_two) + '\n' +
                    '3. ' + current_site.domain + fs.url(new_image.image),
                    settings.EMAIL_HOST_USER,
                    [u.user.email],
                )
                email.send(fail_silently=False)

            elif u.tiers.size_thumbnail_image > 0 and u.tiers.size_thumbnail_image_two > 0 \
                    and u.tiers.url_original_image == 'False' and u.tiers.random_expiring_url == 'None':
                email = EmailMessage(
                    email_subject,
                    'Hi ' + u.user.username + ', thanks you for trusting us. \n' +
                    'Your present: \n' +
                    '1. ' + current_site.domain + fs.url(new_image.thumbnail_image) + '\n' +
                    '2. ' + current_site.domain + fs.url(new_image.thumbnail_image_two),
                    settings.EMAIL_HOST_USER,
                    [u.user.email],
                )
                email.send(fail_silently=False)

            elif u.tiers.size_thumbnail_image > 0 and u.tiers.size_thumbnail_image_two == 0 \
                    and u.tiers.url_original_image == 'False' and u.tiers.random_expiring_url == 'None':
                email = EmailMessage(
                    email_subject,
                    'Hi ' + u.user.username + ', thanks you for trusting us. \n' +
                    'Your present: \n' +
                    '1. ' + current_site.domain + fs.url(new_image.thumbnail_image),
                    settings.EMAIL_HOST_USER,
                    [u.user.email],
                )
                email.send(fail_silently=False)

            elif u.tiers.size_thumbnail_image_two > 0 and u.tiers.size_thumbnail_image == 0 \
                    and u.tiers.url_original_image == 'False' and u.tiers.random_expiring_url == 'None':

                email = EmailMessage(
                    email_subject,
                    'Hi ' + u.user.username + ', thanks you for trusting us. \n' +
                    'Your present: \n' +
                    '1. ' + current_site.domain + fs.url(new_image.thumbnail_image_two),
                    settings.EMAIL_HOST_USER,
                    [u.user.email],
                )
                email.send(fail_silently=False)

            return Response(serializer.data, status=status.HTTP_201_CREATED)





