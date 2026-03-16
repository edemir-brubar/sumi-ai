# sumi-ai/config.py

# Dicionário de Servidores para Automação Universal
SERVIDORES_IMAP = {
    "gmail.com": "imap.gmail.com",
    "outlook.com": "outlook.office365.com",
    "hotmail.com": "outlook.office365.com",
    "yahoo.com": "imap.mail.yahoo.com",
    "icloud.com": "imap.mail.me.com",
    "brubarbrasil.com": "imap.secureserver.net" 
}

# Perfis de Teste Familiar (Sócio e Primeiras Clientes)
USUARIOS = {
    "gislene": {
        "nome": "Gislene",
        "email": "gislene@brubarbrasil.com",
        "perfil": "Sócia Brubar Brasil",
        "prioridades": ["Avalor", "Mercer", "Financeiro"]
    },
    "bruna": {
        "nome": "Bruna",
        "email": "bruna@usp.br",
        "perfil": "Marketing USP/Pecege"
    },
    "barbara": {
        "nome": "Bárbara",
        "email": "barbara@fgv.com",
        "perfil": "Vestibulanda FGV"
    }
}

# Configurações do SUMI
HORARIOS_DISPARO = ["08:00", "13:00", "20:00"]
