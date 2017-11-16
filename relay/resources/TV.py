import time
import zmqpub
from flask_restful import Resource, reqparse


class TV(Resource):
    def __init__(self):
        self.socket = zmqpub.setup()
        time.sleep(1)

    def put(self):
        self.socket.send("tv_on_off")
        return {'state': 'on'}

    def delete(self):
        self.socket.send("tv_on_off")
        return {'state': 'off'}


class TVMode(Resource):
    def __init__(self):
        self.socket = zmqpub.setup()
        time.sleep(1)

    def patch(self):
        parser = reqparse.RequestParser()
        parser.add_argument('state', type=str, help='Mode for TV')
        args = parser.parse_args()
        final_state = args['state']
        if final_state == "right":
            self.socket.send("tv_source_button;tv_right_button;tv_ok_button")
        if final_state == "left":
            self.socket.send("tv_source_button;tv_left_button;tv_ok_button")

        return {'error': ''}

    def delete(self):
        self.socket.send("tv_on_off")
        return {'state': 'off'}
