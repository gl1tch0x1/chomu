import os
import sys

def is_root():
    return os.geteuid() == 0

def safe_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nExiting gracefully.")
        sys.exit(0)
