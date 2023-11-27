# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

# pylint: disable=R0205,R0902,R0903,R0913


import grpc

import g2config_pb2 as g2config__pb2


class G2ConfigStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddDataSource = channel.unary_unary(
            "/g2config.G2Config/AddDataSource",
            request_serializer=g2config__pb2.AddDataSourceRequest.SerializeToString,
            response_deserializer=g2config__pb2.AddDataSourceResponse.FromString,
        )
        self.Close = channel.unary_unary(
            "/g2config.G2Config/Close",
            request_serializer=g2config__pb2.CloseRequest.SerializeToString,
            response_deserializer=g2config__pb2.CloseResponse.FromString,
        )
        self.Create = channel.unary_unary(
            "/g2config.G2Config/Create",
            request_serializer=g2config__pb2.CreateRequest.SerializeToString,
            response_deserializer=g2config__pb2.CreateResponse.FromString,
        )
        self.DeleteDataSource = channel.unary_unary(
            "/g2config.G2Config/DeleteDataSource",
            request_serializer=g2config__pb2.DeleteDataSourceRequest.SerializeToString,
            response_deserializer=g2config__pb2.DeleteDataSourceResponse.FromString,
        )
        self.Destroy = channel.unary_unary(
            "/g2config.G2Config/Destroy",
            request_serializer=g2config__pb2.DestroyRequest.SerializeToString,
            response_deserializer=g2config__pb2.DestroyResponse.FromString,
        )
        self.Init = channel.unary_unary(
            "/g2config.G2Config/Init",
            request_serializer=g2config__pb2.InitRequest.SerializeToString,
            response_deserializer=g2config__pb2.InitResponse.FromString,
        )
        self.ListDataSources = channel.unary_unary(
            "/g2config.G2Config/ListDataSources",
            request_serializer=g2config__pb2.ListDataSourcesRequest.SerializeToString,
            response_deserializer=g2config__pb2.ListDataSourcesResponse.FromString,
        )
        self.Load = channel.unary_unary(
            "/g2config.G2Config/Load",
            request_serializer=g2config__pb2.LoadRequest.SerializeToString,
            response_deserializer=g2config__pb2.LoadResponse.FromString,
        )
        self.Save = channel.unary_unary(
            "/g2config.G2Config/Save",
            request_serializer=g2config__pb2.SaveRequest.SerializeToString,
            response_deserializer=g2config__pb2.SaveResponse.FromString,
        )


class G2ConfigServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddDataSource(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Close(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Create(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def DeleteDataSource(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

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

    def ListDataSources(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Load(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def Save(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_G2ConfigServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "AddDataSource": grpc.unary_unary_rpc_method_handler(
            servicer.AddDataSource,
            request_deserializer=g2config__pb2.AddDataSourceRequest.FromString,
            response_serializer=g2config__pb2.AddDataSourceResponse.SerializeToString,
        ),
        "Close": grpc.unary_unary_rpc_method_handler(
            servicer.Close,
            request_deserializer=g2config__pb2.CloseRequest.FromString,
            response_serializer=g2config__pb2.CloseResponse.SerializeToString,
        ),
        "Create": grpc.unary_unary_rpc_method_handler(
            servicer.Create,
            request_deserializer=g2config__pb2.CreateRequest.FromString,
            response_serializer=g2config__pb2.CreateResponse.SerializeToString,
        ),
        "DeleteDataSource": grpc.unary_unary_rpc_method_handler(
            servicer.DeleteDataSource,
            request_deserializer=g2config__pb2.DeleteDataSourceRequest.FromString,
            response_serializer=g2config__pb2.DeleteDataSourceResponse.SerializeToString,
        ),
        "Destroy": grpc.unary_unary_rpc_method_handler(
            servicer.Destroy,
            request_deserializer=g2config__pb2.DestroyRequest.FromString,
            response_serializer=g2config__pb2.DestroyResponse.SerializeToString,
        ),
        "Init": grpc.unary_unary_rpc_method_handler(
            servicer.Init,
            request_deserializer=g2config__pb2.InitRequest.FromString,
            response_serializer=g2config__pb2.InitResponse.SerializeToString,
        ),
        "ListDataSources": grpc.unary_unary_rpc_method_handler(
            servicer.ListDataSources,
            request_deserializer=g2config__pb2.ListDataSourcesRequest.FromString,
            response_serializer=g2config__pb2.ListDataSourcesResponse.SerializeToString,
        ),
        "Load": grpc.unary_unary_rpc_method_handler(
            servicer.Load,
            request_deserializer=g2config__pb2.LoadRequest.FromString,
            response_serializer=g2config__pb2.LoadResponse.SerializeToString,
        ),
        "Save": grpc.unary_unary_rpc_method_handler(
            servicer.Save,
            request_deserializer=g2config__pb2.SaveRequest.FromString,
            response_serializer=g2config__pb2.SaveResponse.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "g2config.G2Config", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class G2Config(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddDataSource(
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
            "/g2config.G2Config/AddDataSource",
            g2config__pb2.AddDataSourceRequest.SerializeToString,
            g2config__pb2.AddDataSourceResponse.FromString,
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
    def Close(
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
            "/g2config.G2Config/Close",
            g2config__pb2.CloseRequest.SerializeToString,
            g2config__pb2.CloseResponse.FromString,
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
    def Create(
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
            "/g2config.G2Config/Create",
            g2config__pb2.CreateRequest.SerializeToString,
            g2config__pb2.CreateResponse.FromString,
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
    def DeleteDataSource(
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
            "/g2config.G2Config/DeleteDataSource",
            g2config__pb2.DeleteDataSourceRequest.SerializeToString,
            g2config__pb2.DeleteDataSourceResponse.FromString,
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
            "/g2config.G2Config/Destroy",
            g2config__pb2.DestroyRequest.SerializeToString,
            g2config__pb2.DestroyResponse.FromString,
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
            "/g2config.G2Config/Init",
            g2config__pb2.InitRequest.SerializeToString,
            g2config__pb2.InitResponse.FromString,
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
    def ListDataSources(
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
            "/g2config.G2Config/ListDataSources",
            g2config__pb2.ListDataSourcesRequest.SerializeToString,
            g2config__pb2.ListDataSourcesResponse.FromString,
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
    def Load(
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
            "/g2config.G2Config/Load",
            g2config__pb2.LoadRequest.SerializeToString,
            g2config__pb2.LoadResponse.FromString,
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
    def Save(
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
            "/g2config.G2Config/Save",
            g2config__pb2.SaveRequest.SerializeToString,
            g2config__pb2.SaveResponse.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
