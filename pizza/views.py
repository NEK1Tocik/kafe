from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .forms import EnterForm
from .models import PizzaItem, Flags, BasketItem, UserTG
from .tools import Parser
from threading import Thread
from django.contrib.auth.models import User
from django.db.models import Count
import pickle
from .qqueue import send_order
from django.db.models import Sum


# Create your views here.


def login(request):
    form = EnterForm()
    return render(request, 'registration/login.html',
                  {'form': form}
                  )


def index(request):
    basket_len = len(BasketItem.objects.filter(user=request.user.id))
    pizza = PizzaItem.objects.all()
    pizza2d = []
    i = 0
    frame = []
    while i < len(pizza):
        for j in range(4):
            frame.append(pizza[i])
            i += 1
            if i == len(pizza):
                break
        pizza2d.append(frame)
        frame = []
    print(pizza2d)
    content = '<div align="center"><h1>ВЫБИРАЙТЕ И НАСЛАЖДАЙТЕСЬ</h1></div>'
    return render(
        request,
        'base.html',
        {
            'content': content,
            'pizza': pizza2d,
            'current_page': 'index',
            'basket_len': basket_len,
            'userTG': getTG(request)
        },
    )
def getTG(request):
    try:
        res = UserTG.objects.get(user=request.user)
        return res
    except:
        return None


def redir_to_index(request):
    return redirect('index')


def parse(request):
    Flags.objects.create(name='thread_parser', condition=True)

    def aparser():
        parser = Parser()
        parser.run()
        Flags.objects.filter(name='thread_parser').update(condition=False)

    thread = Thread(target=aparser)
    thread.start()
    return render(
        request,
        'loading.html',
        {
            'userTG': getTG(request)
        }
    )


def basket(request):
    user = request.user
    basket_len = len(BasketItem.objects.filter(user=user))
    raw_items = BasketItem.objects.filter(user=user)
    items = raw_items.values('pizza__name').annotate(num_pizza=Count('pizza')).values_list('pizza__name',
                                                                                           'num_pizza',
                                                                                           'pizza_id',
                                                                                           'pizza__image_url'
                                                                                           )
    full_price = raw_items.aggregate(Sum('pizza__price'))['pizza__price__sum']
    if full_price is None:
        full_price = 0
    print(f'[X]- full price = {full_price}')
    raw_items.query = pickle.loads(pickle.dumps(items.query))
    return render(
        request,
        'basket.html',
        {
            'basket_items': raw_items,
            'basket_len': basket_len,
            'current_page': 'basket',
            'full_price': round(full_price, 2),
            'userTG': getTG(request)
        }
    )


def order(request):
    order_pizza = BasketItem.objects.filter(user=request.user)
    send_order(request.user)
    order_pizza.delete()
    return render(
        request,
        'orderok.html',
        {
            'current_page': 'order',
            'userTG': getTG(request)
        }
    )


def add_to_basket(request):
    user_id = request.user.id
    pizza_id = request.GET['pizza_id']
    pizza = PizzaItem.objects.filter(pk=pizza_id)[0]
    user = User.objects.get(pk=user_id)
    BasketItem.objects.create(user=user, pizza=pizza)
    if request.GET['current_page'] == 'index':
        return redirect('index')
    return redirect(request.GET['current_page'])


def drop_position(request):
    user_id = request.user.id
    pizza_id = request.GET['pizza_id']
    BasketItem.objects.filter(user__id=user_id, pizza__id=pizza_id)[0].delete()
    return redirect(request.GET['current_page'])


def check(request):
    while Flags.objects.filter(name='thread_parser')[0].condition:
        pass
    Flags.objects.filter(name='thread_parser').delete()
    return redirect('index')


def bind_TG(request):
    try:
        user = UserTG.objects.get(user=request.user)
    except:
        user = None
    if user:
        return redirect('index')
    return render(
        request,
        'bind_TG.html',
        {
            'current_page': 'bind_TG',
        }
    )


class Enter(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/registration.html'
