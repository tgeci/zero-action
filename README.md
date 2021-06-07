# zero-action
Self made ultra thin open source action camera based on Raspberry Pi Zero W

## Use cases

### Cycling dash camera
What a beautiful tour! Oh damn, forgot to take a picture of the beautiful view at the top of the hill. The problem could be solved with an action cam.
Action / Dash cameras are often expensive and need special accessoires. Therefore, build your own open source action cam with zero-action! :)

### Pet observation camera
Stay tuned - still wip!


## Snapshots
![IMG_2141](https://user-images.githubusercontent.com/4592657/121076572-dc6d2000-c7d6-11eb-97b0-6de671b8c414.jpg)
![IMG_2140](https://user-images.githubusercontent.com/4592657/121076586-e000a700-c7d6-11eb-80fd-3c936eff47eb.jpg)

![Bildschirmfoto 2021-05-23 um 16 31 44](https://user-images.githubusercontent.com/4592657/119264762-b21b4000-bbe4-11eb-94a1-d962716af62d.png)



## Hardware
### List of required components
| # | Description | Where to buy | Price |
| ----- | ----- | ----- | ----- |
| ![Bildschirmfoto 2021-05-24 um 15 08 30](https://user-images.githubusercontent.com/4592657/119352444-fd475880-bca1-11eb-8b36-45f6d04b27b6.png) | Powerbank - Anker Power Core 5000 | [Idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/5977548_-powercore-5000-schwarz-anker-tech.html) | ~15 Euro
| ![Bildschirmfoto 2021-05-24 um 15 08 21](https://user-images.githubusercontent.com/4592657/119352471-046e6680-bca2-11eb-94fe-750039f334d0.png)| Pump Strap - Zefal | [Idealo](https://www.idealo.de/preisvergleich/Typ/3420581030017.html) | ~ 5 Euro
|![Bildschirmfoto 2021-05-24 um 15 07 00](https://user-images.githubusercontent.com/4592657/119352261-bf4a3480-bca1-11eb-81ea-0e7c9b602692.png)| Pi Zero W Set | [Berrybase](https://www.berrybase.de/raspberry-pi/raspberry-pi-computer/kits/raspberry-pi-zero-w-zusammenstellung-full-starter-kit) | ~ 35 Euro
| ![Bildschirmfoto 2021-05-24 um 15 12 51](https://user-images.githubusercontent.com/4592657/119352917-88c0e980-bca2-11eb-8d39-bc42b5fd12b2.png) | Pi Camera Module | [Berrybase](https://www.berrybase.de/raspberry-pi/raspberry-pi-computer/kameras/raspberry-pi-camera-module-8mp-v2.1) | ~ 25 Euro

### Ant+ Sensor integration
Stay tuned - in developement.

## Software
Running on the pi direct:

`cd app`

`pip3 install -r requirements.txt`

`python3 action-recoder.py`


Running as a daemon:
`pip3 install -r requirements.txt`

`cd system`

`sudo cp action-recorder.service /etc/systemd/system/action-recorder.service`

`systemctl daemon-reload`

`systemctl start action-recorder.service`

`systemctl enable action-recorder.service`
