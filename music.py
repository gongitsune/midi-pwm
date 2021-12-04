import time

import mido
import pigpio
from mido.messages.messages import Message


class MyMidi:
    # { elpased, track[msg_list] }
    all_msg: "dict[int, list[list[Message]]]" = {}

    def __init__(self, path: str) -> None:
        self.midi = mido.MidiFile(path)
        self.track_size = len(self.midi.tracks)
        self.analysis()

    def add_msg(self, elapsed: int, track: int, msg: Message):
        self.all_msg.setdefault(elapsed, [[] for _ in range(self.track_size)])
        self.all_msg[elapsed][track].append(msg)

    def is_note_msg(self, msg: Message):
        return msg.type == "note_on" or msg.type == "note_off"

    def analysis(self):
        for (track_num, track) in enumerate(self.midi.tracks):
            elapsed = 0
            for msg in track:
                if not self.is_note_msg(msg):
                    continue

                elapsed += msg.time
                self.add_msg(elapsed, track_num, msg)

    def play(self, play_tracks: "dict[int, int]"):
        """Play Midi.

        Args:
            play_tracks (dict[int, int]): { track: pin }
        """
        # Setup pigpio
        pi = pigpio.pi()
        for pin in play_tracks.values():
            pi.set_mode(pin, pigpio.OUTPUT)

        # Play
        try:
            elapsed = 0
            for my_track in sorted(self.all_msg.items()):
                # Wait
                time.sleep((my_track[0] - elapsed) * 0.0021 * 0.4)
                elapsed = my_track[0]

                for (track_num, msgs) in enumerate(my_track[1]):
                    if not msgs:
                        continue
                    elif track_num in play_tracks.keys():
                        for msg in msgs:
                            duty = 50 if msg.type == "note_on" else 0
                            pi.hardware_PWM(
                                play_tracks[track_num],
                                round(pow(2, (msg.note - 69) / 12) * 440),
                                duty * 10000,
                            )
        finally:
            for pin in play_tracks.values():
                pi.set_mode(pin, pigpio.INPUT)
            pi.stop()


if __name__ == "__main__":
    music = MyMidi("./sound/awa_double.mid")

    music.play({2: 12, 3: 13})
