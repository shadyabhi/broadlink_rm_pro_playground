import zmq


def setup():
    """
    This function does ZeroMQ setup and returns
    the socket that will be used to send messages
    """
    context = zmq.Context()
    socket = context.socket(zmq.PUB)
    socket.connect("tcp://localhost:5559")
    socket.setsockopt(zmq.IMMEDIATE, 1)
    return socket
