import sys

from music3 import MyMidi

my_midi = MyMidi(sys.argv[1])
my_midi.play({sys.argv[2]: 12, sys.argv[3]: 13})
