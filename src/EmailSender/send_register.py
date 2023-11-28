import pika
import json

def send_register(email, nome, plano, valor, endereco, data_instalacao, hora_instalacao):
    credentials = pika.PlainCredentials('rabbitmq', 'rabbitmq')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue='email_sender')

    message = {
        'email': str(email),
        'nome': str(nome),
        'plano': str(plano),
        'valor': str(valor),
        'endereco': str(endereco),
        'data_instalacao': str(data_instalacao),
        'hora_instalacao': str(hora_instalacao)
    }

    channel.basic_publish(exchange='', routing_key='email_sender', body=json.dumps(message))
    print("Email enviado para o mensageiro")
    connection.close()