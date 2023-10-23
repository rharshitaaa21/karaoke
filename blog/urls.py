from django.urls import path
from .import views

urlpatterns = [
    path("",views.index, name='home-page'),
    path('blog_page', views.blog_visit, name='blog_page'),
    path('about-page', views.about_page_redirect, name='about-page'),
    path('feedback', views.feedback, name='feedback'),
    # path('contact/', views.get_name, name='submit_contact'),
    path('', views.ContactFormView.as_view(), name='submit_contact'),


]

