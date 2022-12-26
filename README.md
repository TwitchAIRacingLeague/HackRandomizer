# HackRandomizer
This is a Super Metroid Hack Randomizer, eeverytime Samus's HP changes the game will swap to the next hack in the list (wrapping around once it reaches the end)

I initially tried using pygame to read the controller, but it caused massive slowdowns.

Additionally if the timing seems off, you can try adjusting the sleep in the main while loop.

**NOTE** This is a proof of concept and not a "great" final version, I wanted to show it was possible, I have no idea if it will work on your system, or work well on your system. I'll help what I can if you are having trouble getting setup.

Twitch AI Racing League Discord
https://discord.gg/EexprFHQr8

My Discord:
https://discord.gg/JWU8D7V5cR

## Setup:

Install python3, pip3

Then clone the repo `https://github.com/TwitchAIRacingLeague/retro`

`git checkout HackRandomizer`

pip install the following

```pip3 install -e retro```

Finally clone this repo and install the requirements

```pip3 install -r requirements.txt```

You may have to tweak the controller inputs to make it work for your controller.

## Running
```python3 play.py```

## TODO 
Pull controller mapping to an external file
Pull list of "games" to external file
Make a "helper" that will allow creating save states easier (so you can setup a new game quicker)
