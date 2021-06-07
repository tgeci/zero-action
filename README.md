



# zero-action
Self made ultra thin open source action camera based on Raspberry Pi Zero W

## Use cases

### Cycling dash camera
What a beautiful tour! Oh damn, forgot to take a picture of the beautiful view at the top of the hill. The problem could be solved with an action cam.
Action / Dash cameras are often expensive and need special accessoires. Therefore, build your own open source action cam with zero-action! :)

### Pet observation camera
Stay tuned - still wip!


## Snapshots
<div>
<img src="https://user-images.githubusercontent.com/4592657/121076586-e000a700-c7d6-11eb-80fd-3c936eff47eb.jpg" height="400">
<img src="https://user-images.githubusercontent.com/4592657/121076572-dc6d2000-c7d6-11eb-97b0-6de671b8c414.jpg" height="400">
</div>
<img src="https://user-images.githubusercontent.com/4592657/121076903-3d94f380-c7d7-11eb-8dda-a1b8992eb14e.png" width="1000">

https://user-images.githubusercontent.com/4592657/121087956-5d331880-c7e5-11eb-9512-8b9d9d243bb9.mp4


## Hardware
The setup itself is quite simple. A power bank supplies the energy-saving Pi Zero with power. Depending on the battery, day trips are easily possible. When the action recorder service is started (via Systemd), recording also begins. 
I built my zero-action with the following component list. So that the Pi with its white housing does not stand out from my dark frame, I have covered it in black foil.

### Component list
| # | Description | Where to buy | Price |
| ----- | ----- | ----- | ----- |
| <img src="https://cdn.shopify.com/s/files/1/0491/8227/7795/products/s111_800x.jpg?v=1620467922" width="200" height="200"> | Powerbank - Anker Power Core 5000 | [Idealo](https://www.idealo.de/preisvergleich/OffersOfProduct/5977548_-powercore-5000-schwarz-anker-tech.html) | ~15 Euro
| <img src="https://assets.probikeshop.fr/images/products2/192/87096/600x600-87096-zefal-double-support-de-pompe-doodad.jpg" width="200" height="200"> | Pump Strap - Zefal | [Idealo](https://www.idealo.de/preisvergleich/Typ/3420581030017.html) | ~ 5 Euro
| <img src="https://www.berrybase.de/media/image/05/46/b3/ID_102914_orig_200x200.jpg" width="200" height="200"> | Pi Zero W Set | [Berrybase](https://www.berrybase.de/raspberry-pi/raspberry-pi-computer/kits/raspberry-pi-zero-w-zusammenstellung-full-starter-kit) | ~ 35 Euro
| <img src="https://www.berrybase.de/media/image/90/bf/7d/ID_63015_orig_200x200.jpg" width="200" height="200"> | Pi Camera Module | [Berrybase](https://www.berrybase.de/raspberry-pi/raspberry-pi-computer/kameras/raspberry-pi-camera-module-8mp-v2.1) | ~ 25 Euro
| <img src="https://user-images.githubusercontent.com/4592657/121082440-62d93000-c7de-11eb-995a-424fb5594476.png" width="200">| Black adhesive foil | [Idealo](https://www.idealo.de/preisvergleich/Typ/4007386039903.html) | ~ 6 Euro

### Ant+ Sensor integration
Stay tuned - in developement.

## Software
### Quickstart
If you just want to get started, here are the necessary commands.


Running on the pi direct:

```
cd app
pip3 install -r requirements.txt
python3 action-recoder.py
```


Running as a daemon:
```
pip3 install -r requirements.txt
cd system
sudo cp action-recorder.service /etc/systemd/system/action-recorder.service
systemctl daemon-reload
systemctl start action-recorder.service
systemctl enable action-recorder.service
```


### API
To use the recorder class, you must first import it into your Python code:
`from Recorder import Recorder`.

Then you create an instance and call the `getDiskFreeSpace()`, the `calculate_possible_length()` and `start_recording()`. The first two set the maximum recording length based on the memory and resolution selected. In the future, the calculation is meant to be based on the connected battery
```
action_recoder = Recorder(1024, 768)
action_recoder.getDiskFreeSpace()
action_recoder.calculate_possible_length()
action_recoder.start_recording()

```
