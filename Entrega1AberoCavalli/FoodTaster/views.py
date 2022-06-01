from multiprocessing import context
from django.shortcuts import render
from FoodTaster.models import Dish

# Create your views here.
def index(request):
    dishes = Dish.objects.all()[:5]

    context_dict = {
        'dishes': dishes
    }

    return render(request,
                  context=context_dict,
                  template_name="FoodTaster/home.html")


def dish(request):
    dishes = Dish.objects.all()

    context_dict = {
        'dishes': dishes
    }

    return render(
        request=request,
        context=context_dict,
        template_name="FoodTaster/dish.html"
    )


from django.urls import reverse_lazy
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin

class dishListView(ListView):
    model = dish
    template_name = "FoodTaster/dish_list.html"


class dishDetailView(DetailView):
    model = dish
    template_name = "FoodTaster/dish_detail.html"


class dishCreateView(LoginRequiredMixin, CreateView):
    model = dish
    # template_name = "FoodTaster/dish_form.html"
    # success_url = "/FoodTaster/dishs"
    success_url = reverse_lazy('FoodTaster:dish-list')
    fields = ['name', 'description', 'rating']


class dishUpdateView(LoginRequiredMixin, UpdateView):
    model = dish
    # template_name = "FoodTaster/dish_form.html"
    # success_url = "/FoodTaster/dishs"
    success_url = reverse_lazy('FoodTaster:dish-list')
    fields = ['name', 'code']


class dishDeleteView(LoginRequiredMixin, DeleteView):
    model = dish
    # success_url = "/FoodTaster/dishs"
    success_url = reverse_lazy('FoodTaster:dish-list')


def Recipe(Request):
    pass


def form_hmtl(request):

    if request.method == 'POST':

        return render(
            request=request,
            template_name="FoodTaster/index.html"
        )

    return render(
        request=request,
        template_name='FoodTaster/formHTML.html'
    )


from django.shortcuts import redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import login, logout, authenticate
from FoodTaster.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(
                request=request,
                context={"mensaje": "Usuario Registrado satisfactoriamente."},
                template_name="FoodTaster/index.html",
            )
    else:
        form = UserCreationForm()
        # form = UserRegisterForm()
    return render(
        request=request,
        context={"form":form},
        template_name="FoodTaster/register.html",
    )


def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                template_name = "FoodTaster/index.html"
        else:
            template_name = "FoodTaster/login.html"
        return render(
            request=request,
            context={'form': form},
            template_name=template_name,
        )

    form = AuthenticationForm()
    return render(
        request=request,
        context={'form': form},
        template_name="FoodTaster/login.html",
    )


def logout_request(request):
      logout(request)
      return redirect("FoodTaster:home")