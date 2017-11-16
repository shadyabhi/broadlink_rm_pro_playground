import zmq
import emitsignal
import time


class Subscriber():
    def __init__(self):
        self.device_url = "tcp://localhost:5560"
        self.context = zmq.Context()
        self.subscriber = self.context.socket(zmq.SUB)
        self.subscriber.connect(self.device_url)
        topicfilter = ""
        self.subscriber.setsockopt(zmq.SUBSCRIBE, topicfilter)

    def start(self):
        while True:
            payload = self.subscriber.recv()
            print "Received payload: ", payload
            self.emitsignals(payload)

    def emitsignals(self, payload):
        for signal in payload.split(';'):
            emitsignal.emit_signal(signal)
            time.sleep(0.5)


if __name__ == "__main__":
    sub = Subscriber()
    sub.start()
