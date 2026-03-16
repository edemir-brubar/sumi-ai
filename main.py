# sumi-ai/main.py (VERSÃO UNIVERSAL IMAP)
import imaplib
import email

def conectar_email_universal(servidor, usuario, senha):
    try:
        print(f"SUMI: Tentando conexão universal com {servidor}...")
        mail = imaplib.IMAP4_SSL(servidor)
        mail.login(usuario, senha)
        print("SUMI: Conectado com sucesso!")
        return mail
    except Exception as e:
        print(f"Erro na conexão: {e}")
        return None

def buscar_ultimos_emails(mail):
    # O SUMI seleciona a caixa de entrada
    mail.select("inbox")
    # Busca e-mails não lidos ou recentes
    result, data = mail.search(None, 'ALL')
    ids = data[0].split()
    print(f"SUMI: {len(ids)} e-mails encontrados para resumir.")
    return ids

if __name__ == "__main__":
    # Exemplo de como o SUMI funcionará para qualquer operadora
    # usuario_exemplo = {"servidor": "imap.hostgator.com.br", "email": "contato@empresa.com"}
    print("SUMI AI: Pronto para processar qualquer operadora via IMAP.")
