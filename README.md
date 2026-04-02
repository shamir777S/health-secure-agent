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

```bash
git clone https://github.com/shamir777S/health-secure-agent.git
cd health-secure-agent
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
