# Raspberry PI + RFID = Jukebox

Inspired by [this](https://github.com/hoveeman/music-cards) and [that](https://pimylifeup.com/raspberry-pi-rfid-rc522/).

### Prerequisites
**Raspberry Pi** and **RC522 RFID Reader** connected as:
  - **SDA** connects to **Pin 24**
  - **SCK** connects to **Pin 23**
  - **MOSI** connects to **Pin 19**
  - **MISO** connects to **Pin 21**
  - **GND** connects to **Pin 6**
  - **RST** connects to **Pin 22**
  - **3.3v** connects to **Pin 1**

### Setup
```
sudo apt-get update
sudo apt-get upgrade -y
sudo apt-get install -y omxplayer git python-pip
git clone https://github.com/argoroots/jukebox.git
cd jukebox
pip install -r requirements.txt
```

### Configuration
Enable the SPI Interface by running command:
```
sudo raspi-config
```
From first screen select **5 Interfacing Options**, then **P4 SPI** and enable it.

Check if it's enambed by running following command. It must list _spi_bcm2835_.
```
lsmod | grep spi
```

Start jukebox on system start by adding following line to the file _/etc/rc.local_:
```
_python /home/pi/jukebox/jukebox.py /home/pi/jukebox/cards.yaml_
```
