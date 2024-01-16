# python modules
import os
from re import M
import uuid
from datetime import date

# Django modules
from django.conf import settings
from django.core.exceptions import ValidationError

# DRF modules
from rest_framework import serializers

# models
from users.models import (
    User
)

from feeds.models import (
    Feed,
    FeedImage
)

class FeedUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'pk',
            'username',
            'profile'
        ]

class FeedSerializer(serializers.ModelSerializer):
    user = FeedUserSerializer(read_only=True)
    images = serializers.SerializerMethodField()
    class Meta:
        model = Feed
        fields = (
            'pk',
            'user',
            'images',
            'description',
            'like',
            'created',
            'updated'
        )

    def get_images(self, feed):
        images = feed.feed_images.all()
        return [self.context['request'].build_absolute_uri(image.image.url) for image in images]

    def create(self, validated_data):
        today = date.today()
        image_files = self.context['request'].FILES.getlist('images', None)

        if image_files is None:
            raise ValidationError("이미지 파일이 없습니다.")
        
        feed = Feed.objects.create(**validated_data, user=self.context['request'].user)

        images = []
        for image_file in image_files:
            if 'image' not in image_file.content_type:
                for image in images:
                    feed.delete()
                raise ValidationError("이미지가 아닌 파일이 포함됐습니다. 이미지만 업로드해주세요.")
            ext = image_file.content_type.split('/')[-1]

            while True:
                filename = f"{uuid.uuid4()}.{ext}"
                file_dir = today.strftime("%Y/%m/%d")
                # /opt/instaclone/var/media/feeds/%Y/%m/%d/filename.ext
                filepath = os.path.join(settings.MEDIA_ROOT, f"feeds/{file_dir}/{filename}")
                if not os.path.exists(filepath):
                    break
            
            image = FeedImage(feed=feed)
            image.image.save(filename, image_file)
            image.save()
            images.append(image)
        
        return feed