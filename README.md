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
```

Start command: python main.py (midi file path) (first track num) (second track num)

Example
```bash
python main.py example_song.mid 1 2
```

# Note
Don't forget to run the pigpiod.
Make sure pigpiod runs at boot time if needed.

Use the hardware pwm on the raspberrypi. The pins used are gpio 12, 13.

# License
"midi-pwm" is under [MIT license](https://en.wikipedia.org/wiki/MIT_License).
