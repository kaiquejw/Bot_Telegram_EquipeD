import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBuyDm2HL0RGQqeKJYeZfRwy_Ihhs10IFuOVnSVffj8zsgUdtHZMHvqu7UxuiYdGHYzKtqsoxcndhYR6p0Z6FPLbOLS7CC6Ojt7AJyEUknlTJkQS8mQRV0hvqW_nuEamwMhVDYImuqS9D7gwJvI_3xkvccjLSV5fa1rAuw2Qcx7LwP1KxofKtiXs7oA1X5c7lNXfx9KgeWp75EJoRP0fCV1FelWOEkX0HkjwFydiq5SoIkwBn9DVXHLue_0ORRSNQzK6UcvNrJBYBwSTERJ5_bJpslLN00OPTsXcUUuVgJauoELweJhCutLOr1QoMHSBZ00sv7Sp1RHQSYMlN1F7dGnQU='

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