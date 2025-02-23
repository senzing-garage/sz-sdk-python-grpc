import os

import grpc

# -----------------------------------------------------------------------------
# Helpers
# -----------------------------------------------------------------------------


def get_grpc_channel() -> grpc.Channel:
    ca_certificate_path = os.environ.get("SENZING_TOOLS_CA_CERTIFICATE_PATH")
    if ca_certificate_path:
        with open(ca_certificate_path, "rb") as file:
            server_cert = file.read()

        client_cert = None
        client_certificate_path = os.environ.get("SENZING_TOOLS_XXX")
        if client_certificate_path:
            with open(client_certificate_path, "rb") as file:
                client_cert = file.read()

        client_key = None
        client_key_path = os.environ.get("SENZING_TOOLS_XXX")
        if client_key_path:
            with open(client_key_path, "rb") as file:
                client_key = file.read()

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
