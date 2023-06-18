"""
user_auth/views.py
"""
import firebase_admin
from firebase_admin import credentials
from firebase_admin import auth

from django.contrib import messages
from django.views.generic.base import View
from django.shortcuts import render, redirect


cred = credentials.Certificate("user_auth/firebaseCred.json")
firebase_admin.initialize_app(cred)

class HomeView(View):
    """
    homeView
    """
    def get(self, request):
        """
        get
        """
        return render(request, 'user_auth/home.html')


class SignupView(View):
    """SignupView

    Args:
        View (django.views.generic.base): Methods to override get(), post()
    """
    template = 'user_auth/signup.html'

    def get(self, request):
        """get for SignUp"""
        return render(request, self.template)

    def post(self, request):
        """post for SignUp"""
        name = request.POST.get("name")
        username = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")

        try:
            user = auth.create_user(
                email=email,
                password=password
            )

            # adding username and name fields as custom claims
            auth.update_user(user.uid, custom_claims = {
                'name': name,
                'username': username
            })

            return redirect('home')
        except firebase_admin.exceptions.UnauthenticatedError as error:
            messages.error(request, str(error))

        return render(request, self.template)
