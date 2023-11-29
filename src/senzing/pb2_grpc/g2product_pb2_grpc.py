# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

# pylint: disable=R0205,R0902,R0903,R0913,E1101

import grpc

from . import g2product_pb2 as g2product__pb2


class G2ProductStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Destroy = channel.unary_unary(
            "/g2product.G2Product/Destroy",
            request_serializer=g2product__pb2.DestroyRequest.SerializeToString,
            response_deserializer=g2product__pb2.DestroyResponse.FromString,
        )
        self.Init = channel.unary_unary(
            "/g2product.G2Product/Init",
            request_serializer=g2product__pb2.InitRequest.SerializeToString,
            response_deserializer=g2product__pb2.InitResponse.FromString,
        )
        self.License = channel.unary_unary(
            "/g2product.G2Product/License",
            request_serializer=g2product__pb2.LicenseRequest.SerializeToString,
            response_deserializer=g2product__pb2.LicenseResponse.FromString,
        )
        self.Version = channel.unary_unary(
            "/g2product.G2Product/Version",
            request_serializer=g2product__pb2.VersionRequest.SerializeToString,
            response_deserializer=g2product__pb2.VersionResponse.FromString,
        )


class G2ProductServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Destroy(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Init(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def License(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Version(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_G2ProductServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Destroy": grpc.unary_unary_rpc_method_handler(
            servicer.Destroy,
            request_deserializer=g2product__pb2.DestroyRequest.FromString,
            response_serializer=g2product__pb2.DestroyResponse.SerializeToString,
        ),
        "Init": grpc.unary_unary_rpc_method_handler(
            servicer.Init,
            request_deserializer=g2product__pb2.InitRequest.FromString,
            response_serializer=g2product__pb2.InitResponse.SerializeToString,
        ),
        "License": grpc.unary_unary_rpc_method_handler(
            servicer.License,
            request_deserializer=g2product__pb2.LicenseRequest.FromString,
            response_serializer=g2product__pb2.LicenseResponse.SerializeToString,
        ),
        "Version": grpc.unary_unary_rpc_method_handler(
            servicer.Version,
            request_deserializer=g2product__pb2.VersionRequest.FromString,
            response_serializer=g2product__pb2.VersionResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "g2product.G2Product", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class G2Product(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Destroy(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/g2product.G2Product/Destroy",
            g2product__pb2.DestroyRequest.SerializeToString,
            g2product__pb2.DestroyResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Init(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/g2product.G2Product/Init",
            g2product__pb2.InitRequest.SerializeToString,
            g2product__pb2.InitResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def License(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/g2product.G2Product/License",
            g2product__pb2.LicenseRequest.SerializeToString,
            g2product__pb2.LicenseResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def Version(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/g2product.G2Product/Version",
            g2product__pb2.VersionRequest.SerializeToString,
            g2product__pb2.VersionResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
