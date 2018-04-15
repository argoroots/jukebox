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
sudo apt-get upgrade
sudo apt-get install -y omxplayer git python-pip
git clone https://github.com/argoroots/jukebox.git
```
