from django.dispatch import receiver
from allauth.account.signals import user_signed_up
from django.shortcuts import redirect, render

from .models import UserProfile

@receiver(user_signed_up)
def handle_user_signed_up(request, sociallogin, user, **kwargs):
     #grab the user's data
     new_user_data = sociallogin.account.extra_data
     profile_image_url = new_user_data.get('picture')
     
     print('This is the user data: ', new_user_data)
     # Save the profile picture URL to the user's profile
      # Create a new profile for the user
     profile = UserProfile(user=user, profile_picture=profile_image_url)
     profile.save()

     # Redirect to the index page
     return redirect('/')