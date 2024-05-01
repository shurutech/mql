from app.utilities.fernet_manager import FernetManager
import pytest

@pytest.fixture
def fernet_manager() -> FernetManager:
    return FernetManager("password")

def test_generate_key(fernet_manager: FernetManager):
    key = fernet_manager.generate_key()
    assert key is not None
    assert isinstance(key, bytes)
    assert len(key) == 44

def test_encrypt_decrypt(fernet_manager: FernetManager):
    data = "Hello, World!"
    encrypted_data = fernet_manager.encrypt(data)
    assert fernet_manager.decrypt(encrypted_data) == data