"""
Module: audio_filters

This module provides audio filtering functions for sound objects.

Author: Rodolfo Lopez (rodolfolopez@sandiego.edu)
"""

import sound


def remove_vocals(original_sound):
    """
    Creates a new sound object that is the same as the given sound, but with
    the vocals having been removed.

    Parameters:
    original_sound (type: Sound) - The original Sound object

    Returns:
    removed_vocals_snd (type: Sound) - Same sound as the original, but with vocals removed
    """

    removed_vocals_snd = original_sound.copy()
    for _, smpl in enumerate(removed_vocals_snd):
        new_value = (smpl.left - smpl.right) // 2
        smpl.left = new_value
        smpl.right = new_value

    return removed_vocals_snd


def fade_in(original_sound, fade_length):
    """
    Creates a new sound object with a fade-in effect applied to the given sound.

    Parameters:
    original_sound (type: Sound) - The original Sound object
    fade_length (type: int) - The number of samples over which to apply the fade-in effect

    Returns:
    faded_in_snd (type: Sound) - Same sound as the original, but with a fade-in effect applied
    """

    faded_in_snd = original_sound.copy()
    for i in range(fade_length):
        smpl = faded_in_snd[i]
        mult = i / fade_length
        smpl.left = int(mult * smpl.left)
        smpl.right = int(mult * smpl.right)

    return faded_in_snd


def fade_out(original_sound, fade_length):
    """
    Creates a new sound object with a fade-out effect applied to the given sound.

    Parameters:
    original_sound (type: Sound) - The original Sound object
    fade_length (type: int) - The number of samples over which to apply the fade-out effect

    Returns:
    fade_out_snd (type: Sound) - Same sound as the original, but with a fade-out effect applied
    """

    fade_out_snd = original_sound.copy()
    for i in range(fade_length):
        smpl = fade_out_snd[-1 - i]
        mult = i / fade_length
        smpl.left = int(mult * smpl.left)
        smpl.right = int(mult * smpl.right)

    return fade_out_snd


def fade(original_sound, fade_length):
    """
    Creates a new sound object with both fade-in and fade-out effects applied to the given sound.

    Parameters:
    original_sound (type: Sound) - The original Sound object
    fade_length (type: int) - The number of samples over which to apply both the fade-in and fade-out effects

    Returns:
    fade_snd (type: Sound) - Same sound as the original, but with both fade-in and fade-out effects applied
    """

    faded_in_snd = fade_in(original_sound, fade_length)
    fade_snd = fade_out(faded_in_snd, fade_length)

    return fade_snd


def left_to_right(original_sound, pan_length):
    """
    Creates a new sound object with a left-to-right panning effect applied to the given sound.

    Parameters:
    original_sound (type: Sound) - The original Sound object
    pan_length (type: int) - The number of samples over which to apply the left-to-right panning effect

    Returns:
    left_to_right_snd (type: Sound) - Same sound as the original, but with a left-to-right panning effect applied
    """

    left_to_right_snd = original_sound.copy()
    for i in range(pan_length):
        smpl = left_to_right_snd[i]
        right_mult = i / pan_length
        left_mult = 1 - right_mult
        smpl.left = int(left_mult * smpl.left)
        smpl.right = int(right_mult * smpl.right)

    return left_to_right_snd


# Your final submission should NOT contain any global code.
# In other words, all your code should be contained in the functions defined
# above.


# WARNING: DO NOT MODIFY ANYTHING AFTER THIS LINE!!!


def main():
    import os.path

    options = {
        1: ("remove_vocals", None),
        2: ("fade_in", "fade_length"),
        3: ("fade_out", "fade_length"),
        4: ("fade", "fade_length"),
        5: ("left_to_right", "pan_length"),
    }

    print("The following functions are available.\n")
    print("(1) remove_vocals")
    print("(2) fade_in")
    print("(3) fade_out")
    print("(4) fade")
    print("(5) left_to_right")

    selection = int(input("\nEnter the number of the function to test: "))

    if selection not in range(1, 6):
        print("Invalid selection. Please run the tester again.")
        return

    wav_file = input("Enter the name of the wav file to test with: ")

    # Make sure the file exists so we don't get an error trying to open a
    # file that isn't there.
    if not os.path.isfile(wav_file):
        print("\nTest Failed: The file you typed does not exist. Try again.")
        return

    # create a sound object then call the selected function
    original_sound = sound.load_sound(wav_file)
    test_function_name = options[selection][0]
    print(test_function_name)
    test_function = globals()[test_function_name]

    # Have user enter value for the parameter if one exists
    has_parameter = options[selection][1] is not None

    while has_parameter:
        param_name = options[selection][1]
        param_value = int(input("Enter a value for %s: " % param_name))

        # TODO: check that it is not greater than sound's length?
        if param_value < 1:
            print("Invalid selection.", param_name, "must be a positive integer.")
        else:
            break

    if has_parameter:
        filtered_sound = test_function(original_sound, param_value)
    else:
        filtered_sound = test_function(original_sound)

    # Check that the function gave back a sound
    if filtered_sound is None:
        print(
            "\nTest Failed:",
            test_function_name,
            "does not return a sound. Did you forget the return statement?",
        )
        return

    # Allow the user to play or display the original or filtered sounds
    while True:
        print("\nThe following options are available:\n")
        print("(1) Play original sound.")
        print("(2) Play filtered sound.")
        print("(3) Display original sound waveforms.")
        print("(4) Display filtered sound waveforms.")
        print("(5) Exit this program.")

        selection = int(input("\nEnter your selection: "))
        if selection not in range(1, 6):
            print("Invalid selection. Enter a number between 1 and 5.")
        elif selection == 1:
            original_sound.play()
            sound.wait_until_played()
        elif selection == 2:
            filtered_sound.play()
            sound.wait_until_played()
        elif selection == 3:
            original_sound.display()
        elif selection == 4:
            filtered_sound.display()
        elif selection == 5:
            break


if __name__ == "__main__":
    main()
