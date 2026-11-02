# Creative Coding Karaoke showing my lyrics in time with TunePad beat

import time   # library that lets the program pause

BPM = 125            # same tempo as TunePad project
BEAT = 60 / BPM      # seconds per beat (0.48 seconds)

chorus = [
    "It's all just numbers, ones and zeros,",
    "Week two we panicked, now look at us, heroes!",
    "Code, data, algorithm, one, two, three,",
    "Crack the conundrum, set the message free.",
    "Six-eight, six-one, seven-six, six-five...",
    "Have fun! The code's alive!",
]
verse1 = [
    "Week one, nine a.m., Guthrie Theatre,",
    "Download Python, open IDLE, sleep, I'll see ya later.",
    "Sparklers spelling letters, Morse with a dot and a dash,",
    "Then a string of hex: six-eight, six-one... crack it fast.",
]
verse2 = [
    "Week seven, new module, data's the name,",
    "Colab notebooks open, data types in the frame.",
    "Wyre wants a JSON, every key in double quotes,",
    "The id's an integer, the text's a string of notes,",
    "is_sponsored: true, that's a boolean, see,",
    "linked_socials in a list: TikTok, Insta, X, one-two-three.",
]

bridge = [
    "Imagine, create, play, share, reflect,",
    "Spin it round again, that's the spiral, correct!",
    "Start simple, fiddle around, don't be afraid,",
    "Things go wrong? Stick with it, that's how it's made.",
    "Build it, take it apart, rebuild, repeat,",
    "Copy for ideas, but reference it, keep it neat.",
]

outro = [
    "Week thirteen. Found my old concept map.",
    "My tutor called it. I'd love to redo that.",
    "Function? A recipe you call by its name.",
    "Loop? Do it again, and again, the same.",
    "Binary? Ones and zeros, on and off.",
    "Week-two me... you're gonna love this stuff.",
    "Six-eight, six-one, seven-six, six-five...",
    "Have fun.",
]
def sing(lines, beats_per_line):
    for line in lines:
        print("♪ " + line.upper() + " ♪")
        time.sleep(beats_per_line * BEAT)

sing(verse1, 4)    # rap verse: 4 beats per line
sing(chorus, 8)    # sung chorus: 8 beats per line
sing(verse2, 4)
sing(bridge, 4)
sing(chorus, 8)
sing(outro, 8)     # slower ending
