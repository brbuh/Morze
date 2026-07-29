import keyboard
import winsound
import subprocess

print("=== Morse Beeper v2.0 by brbuh ===")

print('Press "-" or "j" to play "—", press "k" or "." to play "·", press space for pause.')


wpm_modes_long = {
    1: 720,
    2: 300,
    3: 180
}

wpm_modes_short = {
    1: 240,
    2: 100,
    3: 60
}

try:
    choice = int(input('Select mode: 1 - very slow (5 WPM), 2 - standard (12 WPM), 3 - fast (20 WPM): '))
except ValueError:
    choice = None

if choice not in (1, 2, 3):
    print('It seems you made a typo. We have selected the standard mode for you.')


print("To exit, press Esc, to clear the screen press 'c'")


long = wpm_modes_long.get(choice, 300)
short = wpm_modes_short.get(choice, 100)


output = []

def output_print(symbol):
    clear(False)
    output.append(symbol)
    print(*output)
     

def clear(erase_output = True):
    subprocess.run('cls', shell=True)
    if erase_output:
        global output
        output = []

def long_beep():
    winsound.Beep(650, long)
    output_print('—')

def short_beep():
    winsound.Beep(650, short)   
    output_print('·')

def space():
    output_print(' ')



keyboard.add_hotkey('j', long_beep)
keyboard.add_hotkey('-', long_beep)

keyboard.add_hotkey('k', short_beep)
keyboard.add_hotkey('.', short_beep)

keyboard.add_hotkey(' ', space)

keyboard.add_hotkey('c', clear)


keyboard.wait('esc')