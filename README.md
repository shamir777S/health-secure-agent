Health Secure Agent

 Description
Agent automatisé de chiffrement des données de santé.

 Objectif
Protéger les fichiers sensibles afin qu’ils restent illisibles en cas de cyberattaque ou d’exfiltration.

 Fonctionnement
- Génère une clé de chiffrement
- Parcourt un dossier
- Chiffre tous les fichiers
- Stocke les fichiers chiffrés séparément

 Installation
pip install cryptography

 Exécution
python agent_encrypt.py

Résultat
Les fichiers sont transformés en `.encrypted` et deviennent illisibles.

Contexte
Projet réalisé dans le cadre de la cybersécurité des systèmes de santé et conformité RGPD.
