from .models import Post
from rest_framework import serializers


class PostSerializer(serializers.ModelSerializer):

	class Meta:
		model = Post
		fields = ('identity', 'title', 'content',
			'author', 'category', 'pub_date')

