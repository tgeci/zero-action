# zero-action
Self made ultra thin open source action camera based on Raspberry Pi Zero W

## Use case
As a passionate cyclist I often thought afterwards: What a nice tour! Didn't shot a picture of the beatiful hill spot
Action Cams in the trade are often expensive and need special accessories. 

Therefore, I thought build you with open source your own action cam! :-)

## Demo

## Hardware

## Sofware
Running on the pi direct:
`cd app`

`python3 action-recoder.py`

Running as a daemon:
`cd system`

`sudo cp action-recorder.service /etc/systemd/system/action-recorder.service`

`systemctl start action-recorder.service`

`systemctl enable action-recorder.service`
