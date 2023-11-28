import json
import smtplib
import ssl

def send_email(json_data):

    dados = json.loads(json_data)

    # Configurações do servidor SMTP
    smtp_host = 'smtp.gmail.com'
    smtp_port = 465
    smtp_user = ''
    smtp_password = ''

    # Construir e configurar o e-mail
    email = str(dados['email'])
    nome = str(dados['nome'])
    plano = str(dados['plano'])
    valor = str(dados['valor'])
    endereco = str(dados['endereco'])
    data_instalacao = str(dados['data_instalacao'])
    hora_instalacao = str(dados['hora_instalacao'])

    mensagem = f"Olá, {nome}!\n\nSeu plano {plano} foi ativado com sucesso!\n\nValor: {valor}\n\n" \
               f"Data de instalação: {data_instalacao}\n\nHora de instalação: {hora_instalacao}\n\n" \
               f"Endereço de instalação: {endereco}\n\nObrigado por escolher a nossa internet!\n\n"

    # Iniciar conexão SMTP e enviar o e-mail
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL(smtp_host, smtp_port, context=context) as smtp:
        smtp.login(smtp_user, smtp_password)
        smtp.sendmail(smtp_user, email, mensagem.encode('utf-8'))
        print("E-mail enviado com sucesso!")