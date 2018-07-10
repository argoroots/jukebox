#!/usr/bin/env python

import glob
import serial
import subprocess
import sys
import time
import yaml

import RPi.GPIO as GPIO


GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()


class Jukebox:
    def __init__(self, cards_file='cards.yaml'):
        self.player = None
        self.cards = yaml.load(open(cards_file))
        self.card = None
        self.playlist = []
        self.song = 0

        print('Loaded %s cards' % len(self.cards))


    def read_rfid(self):
        PortRF = serial.Serial('/dev/ttyAMA0', 9600)
        read_byte = PortRF.read()

        print(read_byte)

        ID = ''
        if read_byte == '\x02':
            for Counter in range(12):
                read_byte=PortRF.read()
                ID = ID + str(read_byte)
            print(ID)
            return ID


    def load_card(self, rfid):
        if self.card == rfid:
            return

        if rfid not in self.cards:
            print('Unknown card %s' % rfid)
            return

        self.card = rfid
        self.song = 0
        self.playlist = []
        card_path = self.cards[self.card]

        print('Card %s' % self.card)

        if card_path.startswith('http'):
            self.playlist.append(card_path)
        else:
            for infile in glob.glob(card_path.encode('utf-8')):
                self.playlist.append(infile)

            if len(self.playlist) == 0:
                print('No files to play')
                return

        self.playlist.sort()

        return True


    def play_file(self, song=None):
        if song == None:
            self.song = self.song + 1
            if self.song > len(self.playlist):
                self.song = 0
        else:
            self.song = song

        mp3_path = self.playlist[self.song]
        print('Play %s' % mp3_path)
        self.player = subprocess.Popen(['omxplayer', mp3_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    def stop_player(self):
        if not self.card:
            return

        self.card = None
        self.player.stdin.write('q')

        print('Stop')


    def start(self):
        while(1):
            try:
                rfid = self.read_rfid()

                if rfid:
                    if self.load_card(rfid):
                        self.play_file(0)
                    if self.player.poll() == 0:
                        self.play_file()
                else:
                    self.stop_player()

                time.sleep(1)
            except Exception as err:
                print(str(err))


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Give cards Yaml file as first argument')
        sys.exit(1)

    Jukebox(sys.argv[1]).start()
