import pika, sys, os, time, datetime

def main():
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost'))
    channel = connection.channel()

    channel.exchange_declare(exchange='direct_logs', exchange_type='direct')

    result = channel.queue_declare(queue='', exclusive=True)
    queue_name = result.method.queue

    severities = sys.argv[1:]

    if not severities:
        sys.stderr.write(f"Usage: {sys.argv[0]} [info] [warning] [error]\n")

    for severity in severities:
        channel.queue_bind(queue=queue_name, exchange='direct_logs', routing_key=severity)

    print(' [*] Waiting for logs. To exit press CTRL+C')

    def callback(ch, method, properties, body):
        print(f" [x] {method.routing_key} : {body} -- {datetime.datetime.now()}")

    channel.basic_consume(
        queue=queue_name, on_message_callback=callback, auto_ack=True)

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
