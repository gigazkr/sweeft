from random import choices
from string import ascii_letters, digits

from django.shortcuts import redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from shortener.models import URL
from .serializers import URLSerializer


def short_generator():
    url_length = 7
    random_chars = ascii_letters + digits

    # Generate a random string of length 7
    short_url = ''.join(choices(random_chars, k=url_length))

    # Checks if short_url id exists
    if URL.objects.filter(short_url=short_url).exists():
        short_generator()
    return short_url


def redirect_url(request, short):
    urlshort = URL.objects.filter(short_url=short).first()
    urlshort.click_times += 1
    urlshort.save()
    return redirect(urlshort.long_url)


class URLShortener(APIView):
    def post(self, request):

        if 'short_url' in request.data:
            del request.data['short_url']

        random = short_generator()
        index = URL(short_url=random)

        serializer = URLSerializer(index, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'short_url': request.build_absolute_uri('/') + random}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CustomURLShortener(APIView):
    def post(self, request):

        serializer = URLSerializer(data=request.data)

        if serializer.is_valid():
            if not 'short_url' in request.data:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            serializer.save()
            return Response({'short_url': request.build_absolute_uri('/') + request.data['short_url']},
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
