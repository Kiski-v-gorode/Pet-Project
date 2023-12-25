import pika, sys, os, time

def main():
    def callback(ch, method, properties, body):
        print(f" [x] Received {body.decode()} ")
        time.sleep(body.count(b'.'))
        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    connection_params = pika.ConnectionParameters(host='localhost', port=5672)
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()

    # channel.queue_declare(queue='hello')
    channel.queue_declare(queue='task_queue', durable=True)

    channel.basic_qos(prefetch_count=1)
    # channel.basic_consume(queue='hello', on_message_callback=callback)
    channel.basic_consume(queue='task_queue', on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()

    except KeyboardInterrupt:
        print(' Interrupted')
        try:
            sys.exit(0)

        except SystemExit:
            os._exit(0)