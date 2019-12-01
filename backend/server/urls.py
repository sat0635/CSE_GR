from django.urls import path

from . import views

urlpatterns = [
	path('excel/', views.GetExcel),
	path('subject/<userEmail>/', views.SendSubject),
	path('nonsubject/<userEmail>/',views.SendNonSubject),
]
