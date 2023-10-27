from typing import Any
from django import http
from django.shortcuts import render, redirect

from django.views.generic import TemplateView, View

from django.core.files.storage import default_storage
from main.models import Profile
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from main.forms import StarsForm
import math
import logging

logger = logging.getLogger("info")

class UserListView(TemplateView):

    template_name= 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        form = StarsForm()
        users = User.objects.all().exclude(username="admin").order_by("-profile__rating")
        context['users'] = users
        context['form'] = form
        logger.info(f"{self.request.user} opened /")
        
        
        
        return context


    def post(self,request, **kwargs):
        form = StarsForm(self.request.POST)
        data = form.data
        print(data)
        if form.is_valid():
            print("form redirect!")
        else:
            print("invalid form")

        rated_user = User.objects.get(username=data['rated_user'])
        given_rating = float(data['stars'])

        if not request.user.is_authenticated:
            return redirect("accounts/login")

        if rated_user.username != 'admin':
            print(rated_user)
            current_rating = rated_user.profile.rating
            print(current_rating)
            times_rated = rated_user.profile.times_rated

            my_rating = request.user.profile.rating
            new_rating = current_rating-((my_rating/6)*(current_rating - given_rating)*(1/(times_rated+1)))
            rated_user.profile.rating = new_rating
            rated_user.profile.times_rated += 1
            rated_user.save()

            logger.info(f"{request.user} rated {rated_user} {given_rating} stars!")
        else:
            print(request.user,'can\'t rate admin!')

        return redirect('/')

class RateView(View):
    pass    


class UploadProfileView(TemplateView):
    template_name= 'upload.html'
 
    @csrf_exempt
    def post(self, request, *args, **kwargs):
        file = request.FILES['file']
        file_name = default_storage.save("salam.jpg", file)
        return redirect('/')

