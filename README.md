# Hello_World.mp3

A coded karaoke song about learning to code. The beat is written in Python on TunePad, and the lyrics are written in Python in IDLE so they print on screen in time with the beat, ready for people to sing along.

Listen to the beat on TunePad [here](https://tunepad.com/project/132172).

## Table of Contents
* [General Information](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)

## General Information
- Hello_World.mp3 is a rap with a sung chorus about the Creative Coding subject at UTS. The lyrics cover moments from the semester: the Guthrie Theatre in Week 1, sending Morse code with phone flashlights, decoding hex into ASCII, and the JSON data types from Week 7.
- **The problem:** coding basics can feel like maths that belongs to other people, and new terms like *loop*, *string* and *function* are hard to remember.
- **The purpose:** to make the basics stick for beginners. Research shows that putting information into music helps people remember it (Derks-Dijkman et al., 2024; Yuan et al., 2024), the same way songs like *Conjunction Junction* stay with you from primary school.
- **Why I made it:** I'm a communications student who started this subject thinking coding was all maths. I wanted to make something for the Week 1 version of me, and to show future students they're going to love this stuff.
- The song is karaoke rather than a recording, so the code itself invites people to join in.

## Technologies Used
- Python - version 3.14.7
- IDLE (Python's built-in editor) - included with Python 3.14.7
- `time` module (Python standard library)
- TunePad (browser-based, uses Python to make music)

## Features
- **Lyrics in time with the beat:** the code uses the same tempo as the TunePad project (125 BPM), so each line appears when it should be sung.
- **Different speeds for rap and chorus:** rap lines get 4 beats each, while the sung chorus and outro get 8 beats each.
- **Karaoke-style highlighting:** every line prints in capitals with music notes on each side, so you always know which line you're up to.
- **My own function:** one reusable `sing()` function plays every section of the song.
- **A hidden message:** "six-eight, six-one, seven-six, six-five" is hex. Decoded into ASCII it spells *have*, which leads straight into "Have fun!"
- **A coded beat:** five TunePad tracks (kicks, snares, shaker, bass and keyboard), each exactly 8 beats long, built with loops, lists and a list of lists for the chords (C, G, A minor, F).

## Screenshots
![The lyrics printing in IDLE](./images/karaoke_idle.png)
![The beat in TunePad](./images/tunepad_beat.png)

## Setup
There are no extra packages to install. `time` is part of Python's standard library.

1. Download and install Python 3 from [python.org](https://www.python.org/downloads/). IDLE is included.
2. Download `Lyrics_Hello_World_MP3.py` from this repository.
3. Open the TunePad project in your web browser: https://tunepad.com/project/132172

## Usage
1. Open `Lyrics_Hello_World_MP3.py` in IDLE.
2. Have the TunePad project open and ready to play.
3. Press **play** in TunePad and **Run → Run Module** (or F5) in IDLE at the same moment.
4. Sing along as each line appears!

The full song runs for about 1 minute 48 seconds (224 beats at 0.48 seconds each).

**How the timing works:**
```python
BPM = 125            # same tempo as TunePad project
BEAT = 60 / BPM      # seconds per beat (0.48 seconds)
```

**The `sing()` function** goes through a list of lyrics, prints each line in karaoke style, then waits the right number of beats before the next one:
```python
def sing(lines, beats_per_line):
    for line in lines:
        print("♪ " + line.upper() + " ♪")
        time.sleep(beats_per_line * BEAT)
```

**Building the song** is just calling `sing()` with each section in order:
```python
sing(verse1, 4)    # rap verse: 4 beats per line
sing(chorus, 8)    # sung chorus: 8 beats per line
sing(verse2, 4)
sing(bridge, 4)
sing(chorus, 8)
sing(outro, 8)     # slower ending
```

**Use it for your own song:** make a new list of lines and call `sing()` with it, changing `BPM` to match your beat:
```python
my_song = ["First line", "Second line"]
sing(my_song, 4)
```

## Project Status
Project is: _complete_ as a prototype for 52685 Creative Coding (A2). I'd like to keep developing it (see below).

## Room for Improvement
Room for improvement:
- The lyrics and beat have to be started at exactly the same moment, by hand. Because the code only waits with `time.sleep()`, a small gap at the start makes the lyrics drift out of sync.
- IDLE can't show colours, so lines are highlighted with capitals and music notes rather than colour.

To do:
- Store each line's timing in a list beside its lyric, so the song stays in sync and new songs are easy to add (suggested by Addison).
- Show the whole verse with an arrow next to the current line, using a loop inside a loop and an if/else.
- Try word-by-word highlighting.
- Add pause and restart controls.
- Let listeners pick their own song (inspired by Marcus's project).

## Acknowledgements
- This project was inspired by *Adaptation* (polkadotplace, 2006) and *Schoolhouse Rock: Conjunction Junction* (The Emmy Frequency, 2010), songs that taught me something and never left my head.
- The beat structure was based on [Hip Hop Production for Beginners](https://www.youtube.com/watch?v=o9YTH50ijcA) (Davis, 2024) and [How to Code Your Own Fire Beats with Python & TunePad](https://www.youtube.com/watch?v=IA61u8HFtvQ) (Black Girls Code, 2026).
- Chords as lists of MIDI numbers: Horn, West & Roberts (2022), *Introduction to Digital Music with Python Programming*.
- IDLE and Python help: [Getting Started with Python IDLE](https://realpython.com/python-idle/) (Neary, n.d.), [How to Use Python time.sleep()](https://hostman.com/tutorials/how-to-use-python-time-sleep/) (Hostman Team, 2025) and [The Python Tutorial](https://docs.python.org/3/tutorial/) (Python Software Foundation, n.d.).
- Hex checked with [HEX to ASCII Converter](https://lastminuteengineers.com/hex-to-ascii-converter/) (Prabhu, 2026).
- README structure based on Łyczywek (2018) and the [README cheatsheet](https://github.com/ritaly/README-cheatsheet) (ritaly, 2018).
- Many thanks to my tutor Andrew Stapleton for the feedback that changed the whole project, to Marcus and Addison for their peer feedback, and to my dad for listening.

Full references are in my written reflection and project journal.

## Contact
Created by Cate Gyzen for 52685 Creative Coding, University of Technology Sydney, Spring 2026.
