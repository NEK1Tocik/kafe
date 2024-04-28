import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='orders_queue')


def callback(ch, method, properties, body):
    print(f'[x] Received {body.decode()}')
    with open("msg.txt", 'ab') as file:
        file.write(body + '\n'.encode())


channel.basic_consume('orders_queue', callback, auto_ack=True)
channel.start_consuming()
