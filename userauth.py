import bcrypt

# Hashed master password for "mypasswords"
MASTER_PASSWORD_HASH = b"$2b$12$51UGFYdwfqfxbfMBscUVNuIA.PPH5aeyiRyfhE3bT645VGoDZ/ltG"

def check_master_password(password: str) -> bool:
    return bcrypt.checkpw(password.encode(), MASTER_PASSWORD_HASH)
