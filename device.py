import zmq
import logging


class ZMQDevice():
    def __init__(self):
        self.context = zmq.Context(1)
        # Socket facing clients
        self.frontend = self.setup_frontend()
        # Socket facing services
        self.backend = self.setup_backend()

    def setup_frontend(self):
        frontend = self.context.socket(zmq.SUB)
        frontend.bind("tcp://*:5559")
        frontend.setsockopt(zmq.SUBSCRIBE, "")
        return frontend

    def setup_backend(self):
        backend = self.context.socket(zmq.PUB)
        backend.bind("tcp://*:5560")
        return backend

    def stop(self):
        self.frontend.close()
        self.backend.close()
        self.context.close()

    def start(self):
        zmq.device(zmq.FORWARDER, self.frontend, self.backend)


if __name__ == "__main__":
    device = ZMQDevice()
    try:
        device.start()
    except Exception:
        logging.exception("Got exception while starting device")
    finally:
        device.stop()
