import re

from rest_framework import serializers


class ValidatorLinks:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        desc = dict(value).get(self.field)

        link_pattern = r'https?://\S+|www\.\S+'
        youtube_url_pattern = r'(?:https?://)?(?:www\.)?youtube\.com'

        all_links = re.findall(link_pattern, desc)
        for link in all_links:
            if not bool(re.match(youtube_url_pattern, link)):
                raise serializers.ValidationError(f'You can add only YouTube links')
