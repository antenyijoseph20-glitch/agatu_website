from werkzeug.security import generate_password_hash

raw_password = "YourSecretPassword123"
hashed = generate_password_hash(raw_password)
print("Hashed password:", hashed)