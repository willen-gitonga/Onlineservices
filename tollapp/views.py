from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .forms import BillingForm
from django.conf import settings
from django.views.generic.base import TemplateView

def home(request):
    return render(request,'home.html')

def contact(request):
    return render(request,'contact.html')

def team(request):
    return render(request,'team.html')

def courses(request):
    return render(request,'courses.html')

def about(request):
    return render(request,'about.html')
def cart(request):
    return render(request,'cart.html')

def results(request):
    return render(request,'results.html')
    
def vid1(request):
    return render(request,'vid1.html')

def vid2(request):
    return render(request,'vid2.html')

def vid3(request):
    return render(request,'vid3.html')

def vid4(request):
    return render(request,'vid4.html')

def vid5(request):
    return render(request,'vid5.html')

def vid6(request):
    return render(request,'vid6.html')

def vid7(request):
    return render(request,'vid7.html')

def vid8(request):
    return render(request,'vid8.html')

def vid9(request):
    return render(request,'vid9.html')

def vid10(request):
    return render(request,'vid10.html')

def vid11(request):
    return render(request,'vid11.html')
def vid12(request):
    return render(request,'vid12.html')

def vid13(request):
    return render(request,'vid13.html')

def vid14(request):
    return render(request,'vid14.html')

def vid15(request):
    return render(request,'vid15.html')

def vid16(request):
    return render(request,'vid16.html')

def paypal(request):
    return render(request,'Paypal.html')

def perfect(request):
    return render(request,'perfect.html')

def btc(request):
    return render(request,'btc.html')

def checkout(request):
    current_user = request.user

    if request.method == 'POST':
        form = BillingForm(request.POST)
        if form.is_valid():
            student = form.save(commit=False)
            student.save()
            return redirect('payout')
    else:
        form = BillingForm()

    return render(request,'checkout.html',locals())

@login_required(login_url='/accounts/login/')
def  portal(request):
    return render(request,'student.html')


class HomePageView(TemplateView):
    template_name = 'pay.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['key'] = settings.RAVE_PUBLIC_KEY
        return context


