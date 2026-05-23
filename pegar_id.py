import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu5lEAAhIF7unpG6lMYO9Y609U2WrGUriaWQJ4Vs_o25Iu5QiuWdZiE8qq-geE5017Jf3EuvmoyNbMQ4mXAd5krmyOEHArWtm6C1kfWWp5f6vf239UR4zBHcF3847mSukS26HpP9O0duVS-psToccbNs2alUeVEagA_uc3zcF-Rz4x6Iy_IY_ZbufzziKyYRVO5HH85sv7-yPyVUwXDeBl53JALg25QQOSiXxa0muRyu80CY_CzCNTnAibF6pSm0ukiEHVvYu4dVVgSC82Ld_OXh6Mh5mO5foEEUvwYW88dNXyskY8d6eSQxtetuIixI2LTpU2XaZb6CxDOkSFmqaXJA='

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