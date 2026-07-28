##### **Morse Beeper**

**Author:** [GitHub profile](https://github.com/brbuh)
[**License**](LICENSE)
[Morse code table](Morze_code_table.md)
[(Russian version)](README_RU.md)

###### **OVERVIEW**

Morse Beeper is a simple Python script designed for practicing or listening to Morse code timing and audio signals. It captures keyboard inputs in real time and emits beeps corresponding to Morse dashes ("—") and dots ("·") using Windows sound synthesis.



###### **FEATURES**

* Real-time keypress listening using global hotkeys.
* Multiple speed modes based on Words Per Minute (WPM):

  * Mode 1: Very Slow (\~5 WPM)
  * Mode 2: Standard (\~12 WPM)
  * Mode 3: Fast (\~20 WPM)
* Support for dual key layouts (e.g., standard layout and Cyrillic/alternative layout mapping for 'j' / 'k' and '-' / '.').
* Simple escape key exit mechanism.



###### **REQUIREMENTS**

* Windows Operating System (uses `winsound`)
* Python 3.x
* `keyboard` package (Install via: `pip install keyboard`)
* *Note: Running scripts with `keyboard` hotkeys on Windows may require Administrator privileges.*



###### **USAGE**

1. Run the script:
[Morze\_Beeper.py](Morze_Beeper.py)
2. Select a speed mode by entering 1, 2, or 3 when prompted. If an invalid choice is entered, it defaults to Standard Mode (12 WPM).
3. Controls:

   * Press 'j' or '-' to play a DASH ("—") tone.
   * Press 'k' or '.' to play a DOT ("·") tone.
   * Press 'ESC' to exit the application.

