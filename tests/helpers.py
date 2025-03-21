import os

import grpc
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import rsa

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------


def get_grpc_channel() -> grpc.Channel:
    ca_certificate_file = os.environ.get("SENZING_TOOLS_SERVER_CA_CERTIFICATE_FILE")
    if ca_certificate_file:

        # Server-side TLS.

        with open(ca_certificate_file, "rb") as file:
            server_cert = file.read()

        client_cert = None
        client_certificate_file = os.environ.get("SENZING_TOOLS_CLIENT_CERTIFICATE_FILE")
        if client_certificate_file:
            with open(client_certificate_file, "rb") as file:
                client_cert = file.read()

        client_key = None
        client_key_file = os.environ.get("SENZING_TOOLS_CLIENT_KEY_FILE")
        if client_key_file:
            with open(client_key_file, "rb") as file:
                client_key = file.read()

            client_key_passphrase = os.environ.get("SENZING_TOOLS_CLIENT_KEY_PASSPHRASE")
            if client_key_passphrase:
                pem_private_key = serialization.load_pem_private_key(
                    client_key, password=bytes(client_key_passphrase, "utf-8")
                )
                if isinstance(pem_private_key, rsa.RSAPrivateKey):
                    client_key = pem_private_key.private_bytes(
                        encoding=serialization.Encoding.PEM,
                        format=serialization.PrivateFormat.PKCS8,
                        encryption_algorithm=serialization.NoEncryption(),
                    )
                else:
                    raise TypeError

                # bob = serialization.
                # client_key = client_key_bob.private_bytes_raw()  # type: ignore[union-attr]

        # Create client credentials.

        client_credentials = grpc.ssl_channel_credentials(
            root_certificates=server_cert,
            private_key=client_key,
            certificate_chain=client_cert,
        )

        # Create a secure channel
        result = grpc.secure_channel("0.0.0.0:8261", client_credentials)

    else:
        result = grpc.insecure_channel("localhost:8261")

    return result
