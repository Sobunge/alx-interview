#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be opened.
    :param boxes: List of lists where each sublist
                  represents a box and the integers
                  in each sublist represent the keys contained in that box.
    :return: True if all boxes can be opened, else False.
    """
    if not boxes:
        return False

    n = len(boxes)
    opened = [False] * n
    opened[0] = True  # The first box is always opened
    keys = [0]  # Start with the key to the first box

    while keys:
        current_key = keys.pop()
        for key in boxes[current_key]:
            if key < n and not opened[key]:
                opened[key] = True
                keys.append(key)

    return all(opened)


# Example usage
if __name__ == "__main__":
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # False
