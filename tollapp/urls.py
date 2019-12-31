from django.urls import path
from . import views
from django.conf import settings

urlpatterns=[
    path('',views.home,name='home'),
    path('contact/', views.contact, name='contact'),
    path('cart/', views.cart, name='cart'),
    path('shopping/', views.courses, name='courses'),
    path('about/', views.about, name='about'),
    path('checkout/', views.checkout, name='checkout'),
    path('results/',views.results, name='results'),    
    path('portal/', views.portal, name='portal'),
    path('video1/', views.vid1, name='vid1'),
    path('video2/', views.vid2, name='vid2'),
    path('video3/', views.vid3, name='vid3'),
    path('video4/', views.vid4, name='vid4'),
    path('video5/', views.vid5, name='vid5'),
    path('video6/', views.vid6, name='vid6'),
    path('video7/', views.vid7, name='vid7'),
    path('video8/', views.vid8, name='vid8'),
    path('video9/', views.vid9, name='vid9'),
    path('video10/', views.vid10, name='vid10'),
    path('payout/', views.HomePageView.as_view(), name='payout'),
    


]