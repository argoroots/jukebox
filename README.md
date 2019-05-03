# Raspberry PI + RFID = Jukebox

Play music with RFID cards. Inspired by [this](https://github.com/hoveeman/music-cards) and [that](https://behindthesciences.com/electronics/raspberry-pi-rfid-tag-reader/).

### Hardware
Connect **Raspberry Pi** and **RDM6300 RFID Reader**.

### Software

Update system and then install all necessary software.
```shell
$ sudo apt-get update
$ sudo apt-get upgrade -y
$ sudo apt-get install -y omxplayer git python-pip python-serial
$ git clone https://github.com/argoroots/jukebox.git
$ pip install pyyaml
```

Start jukebox on boot by adding following line to _/etc/rc.local_.
```shell
python -u /home/pi/jukebox/jukebox.py /home/pi/jukebox/cards.yaml > /home/pi/jukebox/jukebox.log &
```

Disable the login shell over serial by running following command. From first screen select **5 Interfacing Options**, then **P6 Serial** and disable it.
Enable the SPI Interface by running following command. From first screen select **5 Interfacing Options**, then **P4 SPI** and enable it.
```shell
$ sudo raspi-config
```

Check if it's enabled by running following command. It must list _spi_bcm2835_.
```shell
$ lsmod | grep spi
```

### Cards & music
Add card ids and corresponding folder or stream url to _cards.yaml_.
