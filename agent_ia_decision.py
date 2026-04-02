from agno.agent import Agent
from agno.models.groq import Groq
from agent_encrypt import HealthEncryptionAgent
from pathlib import Path

#  Agent de chiffrement
encrypt_agent = HealthEncryptionAgent()

#  Agent IA décisionnel
decision_agent = Agent(
    name="Health Data Security Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    description="""
Tu es un agent IA de cybersécurité hospitalière.

Ta mission :
- Identifier les données sensibles (patients, médical, financier)
- Décider si le fichier doit être chiffré
- Répondre uniquement par OUI ou NON
"""
)

def process_file(file_path):
    content = file_path.read_text()

    decision = decision_agent.run(
        f"Ce fichier contient : {content}. Doit-il être chiffré ?"
    )

    print(f"\nAnalyse IA : {decision}")

    if "OUI" in decision.upper():
        print("🔐 Chiffrement en cours...")
        encrypt_agent.encrypt_file(file_path, Path("encrypted"))
    else:
        print("✅ Fichier non sensible")

# TEST
if __name__ == "__main__":
    test_file = Path("sample_data/patient.txt")
    process_file(test_file)
