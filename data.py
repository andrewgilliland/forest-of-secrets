ROOMS = {
    "forest": {
        "description": "You stand among towering pines. A path leads north and east.",
        "exits": {"north": "cave", "east": "village"},
        "items": ["map"]
    },
    "cave": {
        "description": "The cave is cold and damp. Shadows dance on the walls.",
        "exits": {"south": "forest"},
        "items": ["sword"]
    },
    "village": {
        "description": "The village is eerily quiet. You hear a stream to the west.",
        "exits": {"west": "forest"},
        "items": []
    }
}