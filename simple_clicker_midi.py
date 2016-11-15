#!/usr/bin/env python3

"""
 Nick Mooney
 nmooney@cs.washington.edu

 Dead simple clicker -> MIDI control
 Sends a "note on" message for note 60 + n, where n =
 the button number pressed. Holds that node until the
 next button is pressed. "?" turns off the last note
 without triggering a new one.
"""

import serial
import serial.tools.list_ports
import sys
import re
import subprocess
import rtmidi
import time

INPUT_LENGTH = 60
INCOMING_RE = r"^incoming: (.{12}) --> (.)"

class ClickerMIDI:
    def __init__(self, midiout):
        self.midiout = midiout
        self.last_note = 0
        
    def midi_play(self, note):
        note_on = [0x90, 60 + note, 112]
        note_off = [0x80, 60 + last_note, 0]
        self.midiout.send_message(note_on)
        time.sleep(0.01)
        if self.last_note != note:
            self.midiout.send_message(note_off)
        self.last_note = note

    def stop():
        note_off = [0x80, 60 + self.last_note, 0]
        self.midiout.send_message(note_off)

    def dispatch(self, button, address):
        print("The button pressed was: %s" % button)
        if button != "?":
            self.midi_play(int(button))
        else:
            stop() 

    def check(self, line):
        result = re.match(INCOMING_RE, line)
        if result:
            groups = result.groups()
            print(groups)
            data, button = groups
            address = data[:6]
            if button.isdigit() or button == "?":
                self.dispatch(button, address)
            

if __name__ == "__main__":
    ports = serial.tools.list_ports.grep("FT232")
    try:
        port_info = next(ports)
    except StopIteration:
        print("The Arduino isn't plugged in!");
        sys.exit()

    midiout = rtmidi.MidiOut()
    if not midiout.get_ports():
        print("The synthesizer isn't plugged in!");
        sys.exit()
    midiout.open_port(0)

    port = serial.Serial(port_info[0], baudrate = 115200, timeout = .25)
    clicker = ClickerMIDI(midiout)
    while True:
        if port.inWaiting():
            from_board = port.read(INPUT_LENGTH)
            lines = from_board.split(b"\n")
            for line in lines:
                clicker.check(line.decode("utf-8"))
