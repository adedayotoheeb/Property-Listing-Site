from django.shortcuts import render, redirect
from . models import *
from .forms import *
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from .forms import *
from django.views.generic import (
    View,
    TemplateView,
    CreateView,
    UpdateView,
    DeleteView,
    DetailView,
    ListView
    )
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .decorators import unauthenticated_user
from django.core.exceptions import ObjectDoesNotExist
# Create your views here.


def index(request):
    properties = Property.objects.all()
    services = Service.objects.all()
    blogs = Blog.objects.all()
    category = Category.objects.all()
    context = {'properties': properties, 'services': services,
               'blogs': blogs, 'category': category}

    return render(request, 'hose/index.html', context)

def about(request):
    agent = Agents.objects.all()
    proper = Property.objects.all()
    context = {'agent': agent, 'property': proper}
    return render(request, 'hose/about.html', context)


def blog(request):
    blog = Blog.objects.all()
    context = {'blog': blog}
    return render(request, 'hose/blog.html', context)


def contact(request):
    return render(request, 'hose/contact.html')


def single_list(request):
    return render(request, 'hose/single-list.html')




def single_blog(request,b_id):
    blog_detail = Blog.objects.get(id=b_id)
    context = {'blog': blog_detail}
    return render(request, 'hose/single-blog.html', context)


def categories(request):
    propert = Property.objects.all()
    context = {'property': propert}
    return render(request, 'hose/categories.html', context)





@login_required(login_url='/logiin/')
def my_properties(request):
    return render(request, 'hose/my-properties.html')

@login_required(login_url='/logiin/')
def messages(request):
    return render(request, 'hose/messages.html')

@login_required(login_url='/logiin/')
def invoice(request):
    return render(request, 'hose/my-invoices.html')


@login_required(login_url='/logiin/')
def bookings(request):
    return render(request, 'hose/bookings.html')


@login_required(login_url='/logiin/')
def favorite(request):
    return render(request, 'hose/favorited-properties.html')





@login_required(login_url='/logiin/')
def my_profile(request):
    userprofile = request.user.userprofile
    form = UserProfileForm(instance=userprofile)
    if request.method == "POST":
        form = UserProfileForm(request.FILES, request.POST, instance=userprofile)
        if form.is_valid():
            form.save()
    context = {'forms':form}
    return render(request, 'hose/my-profile.html', context)


@login_required(login_url='/logiin/')
def submit_property(request):
    return render(request, 'hose/submit-property.html')


@login_required(login_url='/logiin/')
def invoices(request):
    return render(request, 'hose/my-invoices.html')

def add_property(request):
    if request.method =="POST":
        propform=PropertyForm(request.POST, request.FILES)
        if propform.is_valid(commit=False):
            instance.user = request.user
            propform.save()
            messages.success(request, "PROPERTY SUCCESSFULLY ADDDED")
    else:
        propform = PropertyForm()
    return render(request, 'hose/testing.html', {'f':propform})


class CreateProperty(LoginRequiredMixin, CreateView):
    model= Property
    template_name= "hose/add-property.html"
    fields = ['street_name', 'city', 'price', 'bedroom', 'garage','property_status', 'bathroom','cat','property_size','prop_pic' ]
    template_name = 'hose/add-property.html'
    success_url = reverse_lazy("hose:dashboard")

    def form_valid(self, form):
        form.instance.prop_user= self.request.user.userprofile
        return super().form_valid(form)

# class UpdateProperty(UpdateProperty):
#     model= Property
#     template_name= "hose/add-property.html"
#     fields = ['prop_pic', 'street_name', 'city', 'price', 'bedroom', 'garage','property_status', 'bathroom','cat','property_size' ]
#     template_name = 'hose/add-property.html'

#






@unauthenticated_user
def logiin(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            try:
                user_prof = UserProfile.objects.get(user=user)
                login(request, user)
            except UserProfile.DoesNotExist:
                user_prof = UserProfile(user=user, title="Mr", description="Yea love and Live")
                user_prof.save()
                login(request, user)
            return redirect("hose:dashboard")
        else:
            messages.success(request, "Username lr password incorrect")
    return render(request, 'hose/login.html')

    


@login_required(login_url='/logiin/')
def dashboard(request):
    return render(request, 'hose/dashboard.html')


def logoutuser(request):
    logout(request)
    return redirect('/logiin/')


class PropertyByUser(LoginRequiredMixin, ListView):
    login_url='/logiin/'
    model = Property
    template_name ='hose/my-properties.html'
    context_obeject_name ='per'

    def get_queryset(self):
        return Property.objects.filter(User=self.request.user)

@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == "POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()   
            return redirect('hose:logiin')
    context = {'form': form}
    return render(request, 'hose/user.html', context)


           # user = form.cleaned_data.get('username')
            # messages.success(request,"Account was created for " + user)