# zero-action
Self made ultra thin open source action camera based on Raspberry Pi Zero W

## Use cases

### Cycling dash camera
What a nice tour! Arg. Didn't shot a picture of the beatiful hill spot
Action / Dash cameras are often expensive and need special accessoires
Therefore, build your own open source action cam! :)

### Pet observation camera
Stay tuned - still wip!


## Screenshots
![Bildschirmfoto 2021-05-23 um 16 31 44](https://user-images.githubusercontent.com/4592657/119264762-b21b4000-bbe4-11eb-94a1-d962716af62d.png)



## Hardware
### Ant+ Sensor integration
Stay tunen - in developement.

## Sofware
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
