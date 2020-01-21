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
    path('video11/', views.vid11, name='vid11'),
    path('video12/', views.vid12, name='vid12'),
    path('video13/', views.vid13, name='vid13'),
    path('video14/', views.vid14, name='vid14'),
    path('video15/', views.vid15, name='vid15'),
    path('video16/', views.vid16, name='vid16'),
    path('video17/', views.vid17, name='vid17'),
    path('video18/', views.vid17, name='vid17'),
    path('payout/', views.HomePageView.as_view(), name='payout'),
    path('pay/', views.paypal, name='pay'),
    path('processing/', views.perfect, name='paid'),
    path('btc/', views.btc, name='btc'),

]