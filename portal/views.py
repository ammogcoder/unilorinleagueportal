# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from rest_framework import generics
from django.shortcuts import render
from .models import Post
from .serializers import PostSerializer
from django.http import HttpRequest, HttpResponse, request


# Create your views here.
class CreateView(generics.ListCreateAPIView):
	queryset = Post.objects.all()
	serializer_class = PostSerializer

	def perform_create(self, serializer):
		serializer.save()


