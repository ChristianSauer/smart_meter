# Installation

## Setup

1. Create ssd image with Raspberry Pi Imager
1. put `ssd` file into boot partition
1. put `wpa_supplicant.conf` from this project into boot partition 

## Connect

1. Boot up PI
1. Connect as pi@ip and `raspberry` as password
1. Create app folder:

```sh
sudo mkdir /opt/smart_meter
sudo chown pi /opt/smart_meter
```

1. Copy code from this folder to the remote folder, e.g. via VS code ssh

1. make python3 default:

see <https://raspberry-valley.azurewebsites.net/Python-Default-Version/>

```sh
sudo update-alternatives --list python
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python python /usr/bin/python3.7 2
python --version
```

1. install poetry
1. poetry install

1. setup ravendb

For RavenDb:

1. explain dbs to build (debug and readings), expirs!

1. setup service

```shell script
sudo cp smartmeter.service /etc/systemd/system/smartmeter.service
sudo systemctl start smartmeter.service
sudo systemctl enable smartmeter.service
```
