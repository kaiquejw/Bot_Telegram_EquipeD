import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBu3fDyslfKhCmKnq4kTARHR6oitSQ-tli-RgDbtgyTMhO_NuyWi78znvpORFA52gW-LuebjGbT_cC3utvM_taU7uH_ksLUClP_GzYes-NxNUDPlAPQ0JwavT6tyJKDW9PaSddp7f7wCU5MJBfFAPRQ9fn6BTUel33hhqwQDAa06s8xzdnk6KJgwYqzTu5UG8yfKvOdYWIfNrx9UAO8hvrOsEV6flwfA0_IGBL8OHQlnJL74oabJUm7RCNHLh7lFhL65WnyAiObCD6S8FqT3VEWsgih8xvhq5RhYJf8Wbuixq9xJMwsxql0tkpd4SWPEXEFj2uhmN5VmauH6AfVy2FXoA='

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