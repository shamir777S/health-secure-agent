from pathlib import Path
from dotenv import load_dotenv
from agno.agent import Agent
from agno.models.groq import Groq
from agent_encrypt import HealthEncryptionAgent

load_dotenv()

encrypt_agent = HealthEncryptionAgent()

decision_agent = Agent(
    name="Health Data Security Agent",
    model=Groq(id="llama-3.3-70b-versatile"),
    description="""
Tu es un agent IA de cybersécurité hospitalière.

Ta mission :
- identifier les données sensibles de santé ou financières
- décider si un fichier doit être chiffré
- répondre uniquement par OUI ou NON
""",
)

def process_file(file_path: Path):
    content = file_path.read_text(encoding="utf-8")

    run_output = decision_agent.run(
        f"Ce fichier contient : {content}\nDoit-il être chiffré ? Réponds uniquement par OUI ou NON."
    )

    decision_text = str(run_output.content).strip()
    print(f"\nAnalyse IA : {decision_text}")

    if "OUI" in decision_text.upper():
        print("🔐 Chiffrement en cours...")
        encrypt_agent.encrypt_file(file_path, Path("encrypted"))
    else:
        print("✅ Fichier non sensible")

if __name__ == "__main__":
    test_file = Path("sample_data/patient.txt")
    process_file(test_file)
