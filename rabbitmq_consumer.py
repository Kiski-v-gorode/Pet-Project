import pika, sys, os

def main():
    def callback(ch, method, properties, body):
        print(f" [x] Received {body} ")

    connection_params = pika.ConnectionParameters(host='localhost', port=5672)
    connection = pika.BlockingConnection(connection_params)
    channel = connection.channel()
    channel.queue_declare(queue='hello')

    channel.basic_consume(queue='hello', auto_ack=True, on_message_callback=callback)
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