import imaplib
import email
import requests

# CONFIGURAÇÕES DA Z-API
ZAPI_ID = "3F09099802FE61804E5A8EBFEE47BD0C"
ZAPI_TOKEN = "626D4A80D423DC2D474917FA"
MEU_WHATSAPP = "5519992732112" 

def enviar_zap_sumi(texto):
    url = f"https://api.z-api.io/instances/{ZAPI_ID}/token/{ZAPI_TOKEN}/send-text"
    payload = {"phone": MEU_WHATSAPP, "message": texto}
    try:
        response = requests.post(url, json=payload)
        if response.status_code in [200, 201]:
            print("SUMI: Mensagem enviada!")
        else:
            print(f"Erro Z-API: {response.status_code}")
    except Exception as e:
        print(f"Erro: {e}")

if __name__ == "__main__":
    # Mensagem de teste para confirmar que o código rodou
    enviar_zap_sumi("🦅 SUMI ONLINE! Agora o código está corrigido e pronto para rodar.")
