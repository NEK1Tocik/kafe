import pika
import json
from .airflow_api_cust import OrderProcessor
from .models import BasketItem, Order, OrderItem
from django.conf import settings


def send_order(user):
    pizza_set = BasketItem.objects.filter(user=user)
    order_id = 1
    try:
        while True:
            Order.objects.get(order_id=order_id)
            order_id += 1
    except:
        pass
    order = Order.objects.create(user=user, order_id=order_id)
    for pizza in pizza_set:
        OrderItem.objects.create(order=order, pizza=pizza.pizza)
    processor = OrderProcessor(settings.ORDER_PROCESSOR_DAG)
    processor.run_dag()


    '''
    pizza_test = OrderProcessor(settings.TEST_DAG)
    pizza_test.run_dag()
    return
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='orders_queue')
    order_dict = {'order': []}
    for item in order:
        order_dict['order'].append(
            {
                'user': item.user.username,
                'pizza': item.pizza.name
            }
        )
    body = json.dumps(order_dict, indent=4, ensure_ascii=False)

    channel.basic_publish('', 'orders_queue', body)
    connection.close()'''


if __name__ == '__main_':
    class Order_item:
        class pizza:
            name = None

        class user:
            username = None

        def __init__(self, pizza, user):
            self.user.username = user
            self.pizza.name = pizza


    order_item = Order_item('vkusnaya s govnoi', 'pidor gnoiniy')

    send_order([order_item])

if __name__ == '__name__':
    test_tt = OrderProcessor('pizza_dag')
    test_tt.run_dag()
