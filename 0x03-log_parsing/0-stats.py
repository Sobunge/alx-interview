#!/usr/bin/python3
import sys
import signal

total_size = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}
line_count = 0

def print_stats():
    """Prints the accumulated statistics."""
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

def handle_interrupt(sig, frame):
    """Handles the keyboard interrupt signal."""
    print_stats()
    sys.exit(0)

signal.signal(signal.SIGINT, handle_interrupt)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()
        if len(parts) != 10:
            continue

        ip_address = parts[0]
        date = parts[3] + parts[4]
        request = parts[5] + parts[6] + parts[7]
        status_code = parts[8]
        file_size = parts[9]

        if not request.startswith('"GET /projects/260 HTTP/1.1"'):
            continue

        try:
            status_code = int(status_code)
            file_size = int(file_size)
        except ValueError:
            continue

        total_size += file_size
        if status_code in status_counts:
            status_counts[status_code] += 1

        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    handle_interrupt(None, None)

print_stats()
