import os
import subprocess
import requests

# Substitua com o URL do seu webhook
DISCORD_WEBHOOK = "https://discordapp.com/api/webhooks/1311300240154038272/pEFRt1B8uOJbQbWyxXG1-4dMliaZoqJuaBbZwLJRf-kZDBk_Djce8WR-RupeHuFwJ13t"

def get_last_commit():
    # Obtém a mensagem do último commit
    result = subprocess.run(
        ["git", "log", "-1", "--pretty=%B"],
        capture_output=True,
        text=True
    )
    return result.stdout.strip()

def send_to_discord(message):
    data = {"content": f"Novo Commit: {message}"}
    response = requests.post(DISCORD_WEBHOOK, json=data)
    if response.status_code == 204:
        print("Notificação enviada com sucesso!")
    else:
        print("Erro ao enviar notificação para o Discord.")

if __name__ == "__main__":
    commit_message = get_last_commit()
    send_to_discord(commit_message)
