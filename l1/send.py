import pika


connection_params = pika.ConnectionParameters(host='localhost', port=5672)
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='', routing_key='hello', body='Hello World!')
print(" [x] Sent 'Hello World!'")
connection.close()
