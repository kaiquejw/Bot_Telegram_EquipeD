import asyncio
from telethon import TelegramClient
from telethon.sessions import StringSession

# --- PREENCHA SEUS DADOS AQUI ---
API_ID = 31891041  # Seu API ID
API_HASH = 'df20f87a534f0a73f437cb33985d1c95'
SESSION = '1AZWarzcBuzXx1YG2LJgrOm3QnzUft16_zrdrwaaGik_D67qjnEcAalipoGdLkr0n7gwrOCbIdXws97iey3qqx2msITBjyPK2EOVrQZ8FiAwAEvwDrd7CYBwgxO7XR_OxrzgXM8VAf2wPO1649-BbZd08c_PY9_Z5OYJLbvIU7M-qsgNORRHsjkohAqreWTDBcTIItCoOd8lOC6CqNTYJcWH_6RUfcWB-YiPWrWjIKs_ziCpwY1KM4XSkeCWdAim9V2ZZU67Imes7EoOJrx9JSYtCxHsCuiK3O8xKoyKc4WR6UC-isyPZyUd9F-FcZ9e0YWgHFFRjIlbcULBaqNPyCDXmZD3doBY='

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