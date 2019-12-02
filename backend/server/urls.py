from django.urls import path

from . import views

urlpatterns = [
	path('excel/', views.GetExcel),
	path('subject/<userEmail>/', views.SendSubject),
	path('nonsubject/<userEmail>/',views.SendNonSubject),
	path('useremail/<userEmail>/', views.InsertUser),
	path('userinfo/<userEmail>/', views.SendUserInfo),
	path('userinfou/<userEmail>/<major>/<track>/', views.UpdateUserInfo),
]
