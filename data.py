ROOMS = {
    "forest": {
        "description": "You stand among towering pines. A path leads north and east.",
        "exits": {"north": "cave", "east": "village", "south": "clearing"},
        "items": ["map"]
    },
    "cave": {
        "description": "The cave is cold and damp. Shadows dance on the walls.",
        "exits": {"south": "forest", "east": "underground_lake"},
        "items": ["sword"]
    },
    "village": {
        "description": "The village is eerily quiet. You hear a stream to the west.",
        "exits": {"west": "forest", "north": "watchtower", "south": "bridge"},
        "items": ["key"]
    },
    "clearing": {
        "description": "A peaceful clearing with wildflowers. Ancient stones form a circle here.",
        "exits": {"north": "forest", "east": "bridge"},
        "items": ["potion", "ancient_rune"]
    },
    "bridge": {
        "description": "An old wooden bridge spans a rushing river. The boards creak under your feet.",
        "exits": {"north": "village", "west": "clearing", "south": "ruins"},
        "items": ["rope"]
    },
    "watchtower": {
        "description": "A tall stone tower with a view of the entire realm. Wind whistles through the windows.",
        "exits": {"south": "village"},
        "items": ["telescope", "banner"]
    },
    "underground_lake": {
        "description": "A hidden underground lake with crystal-clear water. Glowing crystals light the cavern.",
        "exits": {"west": "cave", "south": "ruins"},
        "items": ["crystal", "gold_coin"]
    },
    "ruins": {
        "description": "Ancient ruins covered in moss and vines. You sense powerful magic once dwelled here.",
        "exits": {"north": "bridge", "west": "underground_lake"},
        "items": ["spell_book", "gem"]
    }
}