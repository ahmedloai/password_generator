from django.urls import include, path
from rest_framework import routers
from . import views

generate_password_view = views.ApiGeneratePassword.as_view({'post': 'genrate_password'})

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path('', generate_password_view),
]