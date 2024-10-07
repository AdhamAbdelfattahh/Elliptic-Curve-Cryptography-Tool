from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.backends import default_backend

def generate_key_pair():
    """Generate an ECC private and public key pair."""
    private_key = ec.generate_private_key(ec.SECP256R1(), default_backend())
    public_key = private_key.public_key()
    return private_key, public_key

def serialize_key(key):
    """Serialize the given key to bytes."""
    return key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ).decode()

def main():
    private_key, public_key = generate_key_pair()
    serialized_public_key = serialize_key(public_key)

    print(f"Private Key: {private_key.private_numbers()}")
    print(f"Public Key: {serialized_public_key}")

if __name__ == "__main__":
    main()
