#!/usr/bin/env python
# -*- coding: utf-8 -*-

import glob
import os
import subprocess
import sys
import time
import yaml

import RPi.GPIO as GPIO
import MFRC522


GPIO.setwarnings(False)
GPIO.cleanup()


card = None
song = 0
player = None
playlist = []

cards = yaml.load(open('cards.yaml'))


def read_rfid():
    reader = MFRC522.MFRC522()

    (status, TagType) = reader.MFRC522_Request(reader.PICC_REQIDL)
    if status != reader.MI_OK:
        return None

    (status, uid) = reader.MFRC522_Anticoll()
    if status != reader.MI_OK:
        return None

    n = 0
    for i in range(0, 5):
        n = n * 256 + uid[i]
    return n


print('Ready to play')
while(1):
    try:
        rfid = read_rfid()

        if not rfid and card:
            player.stdin.write('q')
            card = None
            print('Stop')

        if rfid and rfid != card:
            card = rfid
            song = 0
            playlist = []

            for infile in glob.glob(cards[rfid]):
                playlist.append(infile)
            playlist.sort()

            mp3_path = playlist[song]
            print('Play: ' + mp3_path)
            player = subprocess.Popen(['omxplayer', mp3_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if card and player.poll() == 0:
            song = song + 1
            if song > len(playlist):
                song = 0

            mp3_path = playlist[song]
            print('Play: ' + mp3_path)
            player = subprocess.Popen(['omxplayer', mp3_path], stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)


    except Exception as err:
        print(str(err))

    time.sleep(1)
