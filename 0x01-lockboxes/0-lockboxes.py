#!/usr/bin/python3
"""determines if all the boxes can be opened"""


def canUnlockAll(boxes):
    '''function that creates lockboxes'''

    if type(boxes) != list or len(boxes) == 0:
        return False

    boxLength = len(boxes)

    freeKeys = [0]
    usedKeys = set()

    while freeKeys:
        unlockedBoxesIndex = freeKeys.pop()
        usedKeys.add(unlockedBoxesIndex)

        unlockedBoxes = boxes[unlockedBoxesIndex]

        if type(unlockedBoxes) != list:
            return False

        for key in unlockedBoxes:
            if (key < boxLength) and (key not in freeKeys) and \
                    (key not in usedKeys):
                freeKeys.append(key)

    return len(usedKeys) == boxLength
