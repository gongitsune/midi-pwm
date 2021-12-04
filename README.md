# midi-pwm
MIDI performance with PWM using Raspberrypi zero.

# Requirement
* Raspberrypi
* Python 3.x
* mido
* pigpio

# Installation
```bash
sudo apt install pigpio

pip install mido
pip install pigpio
```

# Usage
```bash
sudo pigpiod
git clone https://github.com/gongitsune/midi-pwm.git

cd midi-pwm
python main.py (midi file path) (...play tracks number)
```

# Note
Don't forget to run the pigpiod.
Make sure pigpiod runs at boot time if needed.

# License
"midi-pwm" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
