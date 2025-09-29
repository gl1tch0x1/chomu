import os
import sys
from chomu.core.logger import logger
from chomu.utils.common import is_root

def main():
    if not is_root():
        logger.error("This tool must be run as root. Use sudo.")
        sys.exit(1)
    # ...existing CLI logic...

if __name__ == "__main__":
    main()
