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

I also had added this to the retro_env file.

```
def loadRom(self, game):
        # This successfully loads a rom, however it doesn't jump to the "start" state as defined in the json file.
        metadata = {}
        rom = retro.data.get_romfile_path(game, retro.data.Integrations.STABLE)
        metadata_path = retro.data.get_file_path(game, 'metadata.json', retro.data.Integrations.STABLE)

        try:
            with open(metadata_path) as f:
                metadata = json.load(f)
            if 'default_player_state' in metadata and self.players <= len(metadata['default_player_state']):
                self.statename = metadata['default_player_state'][self.players - 1]
            elif 'default_state' in metadata:
                self.statename = metadata['default_state']
            else:
                self.statename = None
        except (IOError, json.JSONDecodeError):
            pass

        self.gamename = game
        if self.statename:
            self.load_state(self.statename, retro.data.Integrations.STABLE)

        self.em.loadRom(rom)

        #self.em.configure_data(self.data)
        #self.em.step()

        self.reset()
        obs, rew, done, info = self.step([0,0,0,0,0,0,0,0,0,0,0,0])
```
        

## Running
```python3 play.py```

## TODO 
Pull controller mapping to an external file
Pull list of "games" to external file
Make a "helper" that will allow creating save states easier (so you can setup a new game quicker)
