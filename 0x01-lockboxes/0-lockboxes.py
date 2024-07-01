#!/usr/bin/python3
from typing import List

def canUnlockAll(boxes: List[List[int]]) -> bool:
    n = len(boxes)
    unlocked = set()
    stack = [0]  # Start with the first box
    
    while stack:
        box = stack.pop()
        if box not in unlocked:
            unlocked.add(box)
            for key in boxes[box]:
                if key < n:  # Ensure the key corresponds to a valid box
                    stack.append(key)
    
    return len(unlocked) == n
