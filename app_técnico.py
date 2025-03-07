# Antes de executar o script você precisa alimentar a planinha "emails.xlsx" antes!
# O caminho do seu anexo deve está correto.
# Criar uma senha no gmail para usar no app e colocar a senha na linha 64 "server.login" para efetuar login.


import pandas as pd
import yagmail
import keyring
from jinja2 import Template
import os


# Função para ler arquivo Excel
def read_excel_file(file_path):
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        print(f"Erro ao ler o arquivo Excel: {e}")
        return None

# Função para enviar e-mail
def send_email(to, subject, body, attachment, smtp_user, smtp_password, nome):
    try:
        yag = yagmail.SMTP(smtp_user, smtp_password)
        yag.send(to, subject, body, attachments=[attachment])
        print(f"E-mail enviado com sucesso para a empresa \033[1m{nome}\033[0m, referente ao cargo de \033[1m{subject}\033[0m.")
        print(f"Destinatário: \033[1m{to}\033[0m.")
        #print(f"E-mail enviado com sucesso para a empresa {nome}, referente ao cargo de {subject}. E-mail enviado para {to} em {data_envio} às {hora_envio}.")
    except yagmail.SMTPException as e:
        print(f"Erro ao enviar o e-mail para empresa {nome}: Cargo: {subject}: E-mail{to}: {e}")
    except Exception as e:
        print(f"Erro desconhecido: {e}")
    finally:
        yag.close()

# Função para gerar corpo do e-mail
def generate_email_body(row):
    template = Template("""
Olá,
Espero que você se encontre bem.

Gostaria de aproveitar esta oportunidade para compartilhar um pouco sobre minha jornada na área da Tecnologia da Informação.
Serei grato pela oportunidade de fazer parte desta equipe excepcional e contribuir para o sucesso da empresa.                  
Agradeço pela atenção e espero poder compartilhar mais sobre minha experiência pessoalmente em breve.

                        
Atenciosamente,

Seu nome
Whatsapp (00)99999-9999
""")
    return template.render(nome=row['nome'], cargo=row['cargo'])

# Função principal
def main():
    # Armazenar credenciais do SMTP
    smtp_user = 'seu_email@gmail.com'  # Substitua com seu usuário SMTP
    smtp_password = keyring.get_password('smtp', smtp_user)

    # Definir parâmetros
    file_path = './emails.xlsx'
    attachment = 'Curriculo.pdf'

    # Ler os arquivos do Excel
    emails = read_excel_file(file_path)

    # Enviar os e-mails
    if emails is not None:
        for index, row in emails.iterrows():
            to = row['email']
            nome = row['nome']
            subject = row['cargo']
            body = generate_email_body(row)
            send_email(to, subject, body, attachment, smtp_user, smtp_password, nome)


    # Mensagem após o envio
    print(F"Todos os e-mails foram enviados com sucesso!")

if __name__ == '__main__':
    main()
