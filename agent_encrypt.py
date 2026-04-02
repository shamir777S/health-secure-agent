from pathlib import Path
from cryptography.fernet import Fernet


class HealthEncryptionAgent:
    def __init__(self, key_file: str = "keys/secret.key"):
        self.key_file = Path(key_file)
        self.key_file.parent.mkdir(parents=True, exist_ok=True)
        self.key = self._load_or_create_key()
        self.cipher = Fernet(self.key)

    def _load_or_create_key(self) -> bytes:
        if self.key_file.exists():
            return self.key_file.read_bytes()
        key = Fernet.generate_key()
        self.key_file.write_bytes(key)
        return key

    def encrypt_file(self, source_path: Path, output_dir: Path):
        data = source_path.read_bytes()
        encrypted_data = self.cipher.encrypt(data)

        output_dir.mkdir(parents=True, exist_ok=True)
        encrypted_path = output_dir / f"{source_path.name}.encrypted"
        encrypted_path.write_bytes(encrypted_data)

        print(f"[OK] {encrypted_path}")

    def encrypt_folder(self, source_folder: str, output_folder: str):
        source_dir = Path(source_folder)
        output_dir = Path(output_folder)

        for path in source_dir.rglob("*"):
            if path.is_file():
                self.encrypt_file(path, output_dir)


if __name__ == "__main__":
    agent = HealthEncryptionAgent()
    agent.encrypt_folder("sample_data", "encrypted_output")
