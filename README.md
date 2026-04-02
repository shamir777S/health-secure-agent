# Health Secure Agent

## Description
Ce projet implémente un système agentique de protection des données de santé basé sur l’intelligence artificielle.

Il combine :
- un agent IA de décision
- un agent de chiffrement

## Objectif
Garantir que les données sensibles restent illisibles même en cas de cyberattaque ou d’exfiltration.

---

## Architecture du système

Le système repose sur deux agents :

### 1. Agent IA (Decision Agent)
- Analyse le contenu des fichiers
- Identifie les données sensibles (santé, patient, financier)
- Décide si le fichier doit être chiffré

### 2. Agent de chiffrement
- Chiffre les fichiers sensibles
- Génère une clé de chiffrement
- Rend les données illisibles sans clé

---

## Déploiement

### Prérequis
- Python 3
- Accès à une API Groq

### Installation

git clone https://github.com/shamir777S/health-secure-agent.git
cd health-secure-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

---

### Résultat

Le système analyse automatiquement les fichiers :
	•	Si le fichier contient des données sensibles → il est chiffré
	•	Le fichier devient illisible sans la clé

Exemple :
patient.txt → patient.txt.encrypted

---

### Sécurité et conformité

Ce système permet :
	•	Protection des données de santé
	•	Réduction du risque d’exfiltration
	•	Respect de la confidentialité (RGPD)
	•	Amélioration de la cyber-résilience

---

### Auditabilité
	•	Code open source
	•	Processus transparent
	•	Décisions traçables (analyse IA + chiffrement)

---

### Limites
	•	Projet démonstratif
	•	Gestion des clés simplifiée
	•	Dépendance à une API IA
