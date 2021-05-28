# HackRandomizer
This is a Super Metroid Hack Randomeizer, eeverytime Samus's HP changes the game will swap to the next hack in the list (wrapping around once it reaches the end)

I initially tried using pygame to read the controller, but it caused massive slowdowns.

Additionally if the timing seems off, you can try adjusting the sleep in the main while loop.

## Setup:

Install python3, pip3

Then pip install the following

```pip3 -e https://github.com/TwitchAIRacingLeague/retro```

Finally clone this repo and install the requirements

```pip3 install -r requirements.txt```

You may have to tweak the controller inputs to make it work for your controller.

## Running
```python3 play.py```

## TODO 
Pull controller mapping to an external file
Pull list of "games" to external file
Make a "helper" that will allow creating save states easier (so you can setup a new game quicker)