import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBuzwxVnkMUO2_0YyV8w3RuEQ7ETot-jdFfACj2czCJL-8zGMIdlWD5K2LnWCOQ0BhlG2N8M65AX4gTwkH3fhQ5ylGjOZfK8fCBngpMKJCNtHGZ5EokN0_4rn3faqKtqHz4LupZSIcw53OEqKljitnYiNC8g_Q8vRAoLBex7Fbd92LqbggZwcgof0EPn1qVodRLsQ1PPSQvvhZWUvjw6sg1NJ1-Wy73GM2sjRFMEOI9uLNsY6LGba-3tb7BhxGWoJASGmxF-9rHoWvyRPIxZlEv83XG_TjQkxg7KlB0x2osxQjw765aeI03pzptGyuJ1iOMB6ChwTWaKKhPAov62CWmj8='

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