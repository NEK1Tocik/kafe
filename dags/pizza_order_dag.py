import datetime
import time
from airflow import DAG

from airflow.decorators import task
from airflow.operators.python import PythonOperator


dag = DAG("pizza_order_dag", start_date=datetime.datetime.now())

with dag:
    @task(task_id='check_order_task')
    def check_order():
        import os
        import sys
        #sys.path.append('C:\\Users\\admin\\Documents\\python\\pythonProject2\\shpak')
        sys.path.append('/opt/airflow')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shpak.settings')
        import django
        django.setup()
        from pizza.models import Order, UserTG, OrderItem, Flags
        orders = Order.objects.filter(unprocessed=True)
        if len(orders) == 0:
            return
        current_order = orders[0]
        print('[X] - all right')
        return current_order.order_id
    order = check_order()

    @task(task_id='confirm_order_task')
    def confirm_order(order_id):
        import os
        import sys
        import telebot
        #sys.path.append('C:\\Users\\admin\\Documents\\python\\pythonProject2\\shpak')
        sys.path.append('/opt/airflow')
        os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'shpak.settings')
        import django
        django.setup()
        from pizza.models import Order, UserTG, OrderItem, Flags
        bot = telebot.TeleBot(
            "6187649922:AAE6QwdrWIgva_SFWT_qsCsqrsNCsj_A0VU",
            parse_mode=None
        )
        #bot.send_message(chat_id='435723655', text=f'получили ордер с айди {order_id}')
        order = Order.objects.get(order_id=order_id)
        user = order.user
        #bot.send_message(chat_id='435723655', text=f'user: {user.username}')
        try:
            #bot.send_message(chat_id='435723655', text='пробуем получить айди чата')
            chat_id = UserTG.objects.get(user=user).TG_id
        except:
            return False
        message = f'{order.order_id}' + '\nподтвердите ваш заказ:\n'
        order_set = OrderItem.objects.filter(order=order.id)
        #bot.send_message(chat_id='435723655', text=f'{order_set[0].pizza.description}')
        if len(order_set) == 0:
            #bot.send_message(chat_id='435723655', text='пустой заказ')
            return False
        for order_item in order_set:
            message += f'{order_item.pizza.name}' + '\n'
        bot.send_message(chat_id=str(chat_id), text=message)
        time.sleep(60)
        try:
            confirm_flag = Flags.objects.get(name=f'{str(order.order_id)}')
        except:
            return False
        if confirm_flag.condition:
            confirm_flag.delete()
            order.delete()
            bot.send_message(chat_id=str(chat_id), text='подтверждён и удалён')
            return True
        else:
            confirm_flag.delete()
            return False
    confirm = confirm_order(order)

order>>confirm
