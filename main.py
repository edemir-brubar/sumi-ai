import imaplib
import email
import requests

# CONFIGURAÇÕES DA Z-API VINCULADAS AO SEU NÚMERO
ZAPI_ID = "3F09099802FE61804E5A8EBFEE47BD0C"
ZAPI_TOKEN = "626D4A80D423DC2D474917FA"
MEU_WHATSAPP = "5519992732112" 

def enviar_zap_sumi(texto):
    """Envia o resumo executivo via Z-API para o WhatsApp do SUMI"""
    url = f"https://api.z-api.io/instances/{ZAPI_ID}/token/{ZAPI_TOKEN}/send-text"
    payload = {"phone": MEU_WHATSAPP, "message": texto}
    try:
        response = requests.post(url, json=payload)
        if response.status_code in [200, 201]:
            print("SUMI: Mensagem enviada com sucesso!")
        else:
            print(f"SUMI: Erro Z-API ({response.status_code}): {response.text}")
    except Exception as e:
        print(f"Erro ao conectar com Z-API: {e}")

def conectar_email_universal(servidor, usuario, senha):
    try:
        print(f"SUMI: Conectando ao e-mail {usuario}...")
        mail = imaplib.IMAP4_SSL(servidor)
        mail.login(usuario, senha)
        return mail
    except Exception as e:
        print(f"Erro na conexão IMAP: {e}")
        return None

if __name__ == "__main__":
    print("SUMI AI: Sistema Iniciado.")
    
    # MENSAGEM DE ATIVAÇÃO
    msg_ativacao = (
        "🦅 *SUMI Intelligence: ATIVADO*\n\n"
        "O sistema agora está vinculado a este número. "
        "A partir de agora, seus e-mails serão processados e resumidos aqui."
    )
    enviar_zap_sumi(msg_ativacao)
