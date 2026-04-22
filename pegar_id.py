import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu3ydEPf9y6k3VTQez11OfaYQ-Hvn9SNQR3r3Wuix8bdOuLUXuiqLRoXd7voYzD7omXXZTqrhg3otjfZgfGwnFf8E2hvC5-rk5Kzr8aR7mbYNVSL01UvdvtJo3zqNUB3EJSzBglPLRZzp9Opc0eW3uXzBBvEBHAhiO7pafqwglJpURvvw4NE2kz8k4ut-e_BKQD5JDAs4J7_zOh3thqvgZe9tS8P5uTm25ZeSrUO7Wwl85-dj8De9asaVUwOFdnwXmg9Qj700EcKs1ATy32y8doLhUO1Go9eZBlYUoruKmX3c2Q-CJdduUyQ65Lxq-0x8mQd9wPwnMNxkRk0t9MbeiCE='

async def main():
    print("Conectando...")
    client = TelegramClient(StringSession(SESSION), API_ID, API_HASH)
    await client.connect()
    
    print("\n👇 AQUI ESTÃO SEUS ÚLTIMOS GRUPOS/CONVERSAS 👇\n")
    print(f"{'NOME DO GRUPO':<30} | {'ID PARA O GITHUB'}")
    print("-" * 50)
    
    # Pega as últimas 15 conversas
    async for dialog in client.iter_dialogs(limit=15):
        print(f"{dialog.name:<30} | {dialog.id}")
        
    print("\n👆 Copie o ID (número negativo) do grupo 'Teste' e coloque no GitHub.\n")

if __name__ == '__main__':
    asyncio.run(main())