#!/usr/bin/python3
def validUTF8(data):
    # Number of bytes in the current UTF-8 character
    n_bytes = 0

    # Masks to check the most significant bits
    mask1 = 1 << 7
    mask2 = 1 << 6

    # Iterate over each integer in the data list
    for num in data:
        # Get the binary representation of the integer and keep only the 8 least significant bits
        bin_rep = format(num, '#010b')[-8:]

        # If this is the start of a new UTF-8 character
        if n_bytes == 0:
            # Determine the number of bytes in the character
            for i in range(8):
                if (num & (mask1 >> i)) == 0:
                    break
                n_bytes += 1

            # 1-byte character
            if n_bytes == 0:
                continue

            # Invalid scenarios according to UTF-8 rules
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # If this is a continuation byte, it must start with '10'
            if not (num & mask1 and not (num & mask2)):
                return False

        # Decrement the number of bytes left for the current character
        n_bytes -= 1

    # All characters must be completely processed
    return n_bytes == 0

# Example usage:
data = [197, 130, 1] # Valid UTF-8 encoding
print(validUTF8(data)) # Output: True

data = [235, 140, 4] # Invalid UTF-8 encoding
print(validUTF8(data)) # Output: False
