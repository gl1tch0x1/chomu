import os
import sys

def check_root():
    if os.geteuid() != 0:
        print("ERROR: This tool must be run as root. Use sudo.")
        sys.exit(1)

def format_memory_kb_to_mb(kb_value):
    try:
        mb_value = kb_value / 1024
        return f"{mb_value:.1f} MB"
    except Exception:
        return "N/A"

def confirm_action(prompt):
    try:
        ans = input(f"{prompt} [y/N]: ").strip().lower()
        return ans in ['y', 'yes']
    except KeyboardInterrupt:
        print("\nAction cancelled by user.")
        return False

def safe_input(prompt):
    try:
        return input(prompt)
    except KeyboardInterrupt:
        print("\nExiting gracefully.")
        sys.exit(0)
