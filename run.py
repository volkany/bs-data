#!/usr/bin/env python
"""
Generate data JSON from APK CSV source.
"""

from cr import *
from box import Box
import yaml

if __name__ == '__main__':
    config_path = './config.yml'

    with open(config_path) as f:
        config = Box(yaml.load(f))

    for cls in [AllianceBadges, Cards, Rarities, ChestOrder, ClanChest, Regions, Arenas, TreasureChests, CardStats]:
        app = cls(config=config)
        app.run()


