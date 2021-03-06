from django.contrib.auth import get_user_model
from django.contrib.sites.models import Site

from socialregistration.models import (FacebookProfile, TwitterProfile, 
                                       OpenIDProfile, LinkedInProfile)

class Auth(object):
    supports_object_permissions = False
    supports_anonymous_user = False
    def get_user(self, user_id):
        try:
            return get_user_model().objects.get(pk=user_id)
        except get_user_model().DoesNotExist:
            return None

class FacebookAuth(Auth):
    def authenticate(self, uid=None):
        try:
            return FacebookProfile.objects.get(
                uid=uid,
                site=Site.objects.get_current()
            ).user
        except FacebookProfile.DoesNotExist:
            return None

class TwitterAuth(Auth):
    def authenticate(self, twitter_id=None):
        try:
            return TwitterProfile.objects.get(
                twitter_id=twitter_id,
                site=Site.objects.get_current()
            ).user
        except TwitterProfile.DoesNotExist:
            return None

class LinkedInAuth(Auth):
    def authenticate(self, linkedin_id=None):
        try:
            return LinkedInProfile.objects.get(
                linkedin_id=linkedin_id,
                site=Site.objects.get_current()
            ).user
        except LinkedInProfile.DoesNotExist:
            return None

class OpenIDAuth(Auth):
    def authenticate(self, identity=None):
        try:
            return OpenIDProfile.objects.get(
                identity=identity,
                site=Site.objects.get_current()
            ).user
        except OpenIDProfile.DoesNotExist:
            return None
