from django.urls import path

from . import views

urlpatterns = [
	path('excel/', views.GetExcel),
	path('gr/<userEmail>/', views.SendGr),
]
