import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu44SE8kuVaYSUUA6tYR-wUPAw1WABZbQ0EyEwrQZ96t4C6yldKQR2Aw8vJ0lvDPNoek8rt9D-hyOBLngL5tZ4SsXYHu1biHV0viR71rCcc-KsdXN4Nrz7x5FF_jDv_x5t8hrySWHkt0mAKZ04mEuK6CTw3gPGh7Ojq6zT3bRqcXSxo6gVNsh8VQIyUj9oOXqNWdPU_yCSlxNTIV6TvDaphk23SLOSALUDj8AqVSixl17LAWgCthjzrs8o0JiDuorIAaR7Xpxr_3xIqIftzzjjYI3sqajxoLDnouk9WQ9g93vZ6kQKnjND3GTHHEQcxh5P1-hlN43lkPxZCh3kMSizTU='

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