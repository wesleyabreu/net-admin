import pika, sys, os
from send_email import *

def main():
    
    credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
    connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost', credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='email_sender')

    def callback(ch, method, properties, body):
        print(f" [x] Recebido {body}")
        send_email(body)

    channel.basic_consume(queue='email_sender', on_message_callback=callback, auto_ack=True)

    print(' [*] Esperando por mensagens. Para sair pressione CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)