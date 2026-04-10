import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBuyFGaNWyoUld6Fcmu5DJIVzeQf9FxiwlxobEJXMgSd8NhDxHpxqLAtRn7_JM0oDuiUKuJxxofmlx8OSThY77lgkIA4JnB78VtMokMrJmHZ4IF2TtVgpyszjp_5Cq-Y5u6wBLvsh_IYHEIs_xvKpv--r_yWUvrQjBuTw1LAzWeHe-yHKmBX2mXx2kQL0mnsDvO9zcYbwBX6O1BrNQE7mcdNexPgFRq8uSgrcIm-D-I66wzplDm_91D9ahS8JyF36ZUi00LzqRdgfLgWZFBD3rNz4qlwB6jE0oEWPIhIhdQaUrQJVXf2JNzqQ6WgOy7G4X2ACbkkkFdfo_heEXpnn28W8='

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