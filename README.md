# Discord-VC-Exploit

### Exploit de changement de région des appels vocaux sur Discord (VC Overload) - **ERROR VC Crasher**

---

## Fonctionnement

Discord utilise des serveurs régionaux pour connecter les utilisateurs dans un hub vocal partagé. Ce projet exploite une faille en surchargeant ces serveurs via des requêtes API répétées, provoquant des erreurs et des interruptions dans les appels vocaux.

---

## Installation et Utilisation

### 1. Téléchargez le script d'installation
Rendez-vous sur la page des [releases de MateOver](https://github.com/ErrorNoName/MateOver/releases) et téléchargez le fichier d'installation en suivant ce lien direct :

**[Télécharger le script](https://github.com/ErrorNoName/MateOver/releases/download/UseArch/install_and_run.MateOver.sh)**

---

### 2. Rendre le script exécutable
Après avoir téléchargé le script, ouvrez votre terminal et exécutez les commandes suivantes :

```bash
chmod +x install_and_run.MateOver.sh
```

---

### 3. Installer MateOver
Lancez le script d'installation avec les privilèges administrateur :

```bash
sudo ./install_and_run.MateOver.sh
```

---

### 4. Ajouter votre token Discord
Pendant l'installation, le fichier `Data.json` sera créé. Ouvrez ce fichier pour y insérer votre token Discord.

```bash
sudo nano /opt/MateOver/Data.json
```

Collez votre token dans le champ `"discordToken"`, comme dans l'exemple ci-dessous :

```json
{
    "discordToken": "VOTRE_TOKEN_DISCORD"
}
```

Enregistrez et fermez le fichier (`CTRL + O` pour enregistrer, puis `CTRL + X` pour quitter nano).

---

### 5. Lancez MateOver
Une fois votre token configuré, exécutez MateOver depuis le terminal avec la commande suivante :

```bash
sudo MateOver
```

---

## Pourquoi cela fonctionne ?

Discord utilise des threads pour gérer de nombreuses fonctionnalités API, y compris la gestion des régions. Lorsque vous modifiez rapidement la région d'un appel vocal plusieurs fois :

- Cela surcharge les serveurs, provoquant des erreurs de connexion.
- Cela force Discord à tenter plusieurs connexions régionales simultanées.
- Résultat : des interruptions ou des crashs dans l'appel vocal.

---

## Remarque importante

### **À propos de la sécurité du code**
- Oui, **mon code n'est pas protégé**. C'est intentionnel.
- Vous serez **logué** : certaines informations système de base (comme votre pseudonyme Discord, IP publique, etc.) seront envoyées via un webhook sécurisé.
- **Je ne ferai rien avec vos données.** Ce logiciel est uniquement conçu à des fins éducatives.

---

## Crédits

- **Créé par** : Ezio  
- **Contact** : Si vous avez des questions ou des problèmes, ouvrez un ticket ou contactez-moi via Discord.

---

**Avertissement** : Ce projet est uniquement à des fins éducatives. Toute utilisation malveillante de ce code est à vos propres risques. Je décline toute responsabilité pour tout usage abusif. Utilisez ce logiciel avec discernement et respect pour les autres utilisateurs.
