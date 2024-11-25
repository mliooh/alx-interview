#!/usr/bin/python3
"""
Module contains canUnlockAll function
"""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened"""
    if boxes is None or len(boxes) == 0:
        return False
    keys = [0]
    for key in keys:
        for box in boxes[key]:
            if box not in keys and box < len(boxes):
                keys.append(box)
    if len(keys) == len(boxes):
        return True
    return False