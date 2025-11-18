from passlib.context import CryptContext

# Force bcrypt to use portable backend (fixes GitHub Actions failure)
pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto",
    bcrypt__ident="2b"   # stable and works in Linux runners
)

def hash_password(password: str) -> str:
    # bcrypt max input is 72 bytes; Passlib handles trimming safely
    return pwd_context.hash(password)

def verify_password(plain: str, hashed: str) -> bool:
    return pwd_context.verify(plain, hashed)
