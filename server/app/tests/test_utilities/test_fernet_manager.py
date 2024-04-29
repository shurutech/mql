from app.utilities.fernet_manager import FernetManager
import pytest

@pytest.fixture
def fernet_manager() -> FernetManager:
    return FernetManager("password")

def test_generate_key(fernet_manager: FernetManager):
    assert fernet_manager.generate_key() == b'0uyIMz__qpFLfU9f-t3RuMKqPs_9Juf3in5zeMEOOp0='

def test_encrypt_decrypt(fernet_manager: FernetManager):
    data = "Hello, World!"
    encrypted_data = fernet_manager.encrypt(data)
    assert fernet_manager.decrypt(encrypted_data) == data