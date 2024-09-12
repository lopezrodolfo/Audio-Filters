# Audio Filters

A Python module providing various audio filtering functions for sound objects.

## Author

Rodolfo Lopez

## Date

Fall 2019

## Features

- Remove vocals
- Fade in
- Fade out
- Fade (both in and out)
- Left-to-right panning

## Requirements

- Python 3.x
- `sound.py` module (for loading and manipulating sound objects)
- Additional dependencies: numpy, scipy, sounddevice, matplotlib

## Installation

1. Clone this repository or download the source code.
2. Install the required dependencies:

```
pip install numpy scipy sounddevice matplotlib
```

## Usage

1. Place your WAV files in the same directory as the `audio_filters.py` script.

2. Run the script directly to access the interactive testing menu:

```
python audio_filters.py
```

3. Follow the prompts to select a function and a WAV file to apply the filter to.

4. After applying the filter, you can choose to play the original or filtered sound, display waveforms, or exit the program.

## Functions

- `remove_vocals(original_sound)`: Removes vocals from the sound
- `fade_in(original_sound, fade_length)`: Applies a fade-in effect
- `fade_out(original_sound, fade_length)`: Applies a fade-out effect
- `fade(original_sound, fade_length)`: Applies both fade-in and fade-out effects
- `left_to_right(original_sound, pan_length)`: Applies a left-to-right panning effect

## Example

To apply a fade-in effect to a WAV file:

1. Run `python audio_filters.py`
2. Select option 2 for "fade_in"
3. Enter the name of your WAV file (e.g., "example.wav")
4. Enter the fade length in samples (e.g., 44100 for a 1-second fade at 44.1kHz)
5. Use the menu options to play or display the original and filtered sounds

## Acknowledgements

Dr. Sat Garcia and Dr. Dan Zingaro wrote `sound.py` and I implemented the functions in `audio_filters.py`
