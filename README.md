# Broadlink RM Pro helper scripts

This is a collection of helper scripts to play with the Broadlink RM Pro API in python

## Record signal

	./record_signal.py payloads/tv_on_off

The above command saves the IR/RF signal in a pickled binary file.

## Emit Signal

	./emit_signal.py payloads/tv_on_off

The above command emits the signal that was saved in the record stage.
