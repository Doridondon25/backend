from os import getenv


# List of all required environment variables
required_vars = [
    "TYPE",
    "PROJECT_ID",
    "PRIVATE_KEY_ID",
    "PRIVATE_KEY",
    "CLIENT_EMAIL",
    "CLIENT_ID",
    "AUTH_URI",
    "TOKEN_URI",
    "AUTH_PROVIDER_x509_CERT_URL",
    "CLIENT_x509_CERT_URL",
    "UNIVERSE_DOMAIN"
]

# Check and print each variable
print("Checking environment variables:")
for var in required_vars:
    value = getenv(var)
    if value is None:
        print(f"❌ {var} is not set")
    else:
        print(f"✅ {var} is set")

# Create the dictionary
fbk_dict = {
    "type": getenv("TYPE"),
    "project_id": getenv("PROJECT_ID"),
    "private_key_id": getenv("PRIVATE_KEY_ID"),
    "private_key": getenv("PRIVATE_KEY"),
    "client_email": getenv("CLIENT_EMAIL"),
    "client_id": getenv("CLIENT_ID"),
    "auth_uri": getenv("AUTH_URI"),
    "token_uri": getenv("TOKEN_URI"),
    "auth_provider_x509_cert_url": getenv("AUTH_PROVIDER_x509_CERT_URL"),
    "client_x509_cert_url": getenv("CLIENT_x509_CERT_URL"),
    "universe_domain": getenv("UNIVERSE_DOMAIN")
}