import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBuz-1nSJzyQl5slwqNVIiv7BDL9AyH-ICkNfAUUEOYcPXTz8yhvnFrGc_YcnArJvaH66uGj8VMcim-DLUXUU6qq5QxXfcDmoVvuXZb0m2G6rnTLrzuFc368Fp9yo9DP83AAzhmGTkoI_F-9CU5O47ZikaUZ9P9lh4yGzLXEHe-i_SVuqDEGZC_PIolVCIGgnC5OUKOzLr_ejkDePBX5QES3MHmvMj4kk759twua1KvBBdWbrnirbL-qufGTfxjfFVGDNjR3XYo0S-ScMW3QtK0tqzcaFMtZUOGRyqBwRhwbeF3f2fYrgRAlk2nN0qg3uEKxaTh3rB3yewbsTtTEY5BIc='

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