import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBuwVZdmwcVI2PYPgVzeQLrevkQ0zZDHXyKtaROIr5A9K0SGxaOjNa081Hjy9FFdr2AjrkCUdqBXP1SWXhHEamrLRsllzAzJw_RL6PoiNo3kxcD7rzx27-xzPKwXiGdPWW57DtN9zO9qjWZhpKV40U7hBnZfo4S6fErFTOpBGslsggmIklCEqAgR39Dit6m7NQCmK8xMAFdy1f_JU7_n7Cq_B2B3Kx-jU8HtdThySMRiAg4dA9EiZ-iCk7IQj7OOMszWy_rEfcQlj9c2Lpw_R1y9zi7Akc_fAaIO3f3zZy3QQlQn8nfSY94QhRqq8trLm-Mv5qGKYUeenuALSDdr-6X5w='

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