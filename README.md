 Health Secure Agent

 Description
Agent automatisé de chiffrement des données de santé.

 Objectif
Garantir la confidentialité des données sensibles même en cas de cyberattaque (ex : ransomware, exfiltration).

Fonctionnement
- Génération automatique d’une clé de chiffrement
- Parcours des fichiers d’un dossier
- Chiffrement des données
- Stockage sécurisé des fichiers chiffrés

Installation
pip install -r requirements.txt

 Utilisation
python agent_encrypt.py

 Exemple
Un fichier patient.txt devient :
patient.txt.encrypted

Sécurité
- Données illisibles sans clé
- Protection contre fuite de données
- Compatible RGPD (confidentialité)

 Contexte
Projet réalisé dans le cadre de :
- Cyber-résilience des systèmes de santé
- Conformité RGPD
- Finance Agentique

