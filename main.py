
"""
This file is responsible for:
-Setting up the initial variables, like screen size and the tileset
-Creating the entities
-Drawing the screen and everything on it
-Reacting to the player's input
"""

#!/user/bin/env python3
import sys
import os
os.environ["path"] = os.path.dirname(sys.executable) + ";" + os.environ["path"]
import glob
import tcod

#call the functions we wrote
from engine import Engine
from entity import Entity
from game_map import GameMap
from input_handlers import EventHandler


def main() -> None:
    #defining the variables of the screen
    screen_width = 80
    screen_height = 50

    map_width = 80
    map_height = 45

    tileset = tcod.tileset.load_tilesheet(
        #here we tell tcod what font to use
        "dejavu10x10_gs_tc.png", 32, 8, tcod.tileset.CHARMAP_TCOD
    )

    #event_handler is an instance of an EventHandler class.
    #we use it to receive events and process them
    event_handler = EventHandler()

    player = Entity(int(screen_width / 2), int(screen_height / 2), "@", (255, 255, 255))
    npc = Entity(int(screen_width / 2 - 5), int(screen_height / 2), "@", (255, 255, 0))
    entities = {npc, player}

    game_map = GameMap(map_width, map_height)
    engine = Engine(entities=entities, event_handler=event_handler, game_map=game_map, player=player)

    #this part creates the screen
    with tcod.context.new_terminal(
        screen_width,
        screen_width,
        tileset=tileset,
        title="Yet Another Roguelike Tutorial",
        vsync=True,
    ) as context:

        #this is the console that we are drawing to. We set the width & height
        root_console = tcod.Console(screen_width, screen_height, order="F")

        #this is our game loop
        while True:
            #this line tells the program to put the '@' on the screen in the proper place
            engine.render(console=root_console, context=context)

            events = tcod.event.wait()

            engine.handle_events(events)

if __name__ == "__main__":
    main()
