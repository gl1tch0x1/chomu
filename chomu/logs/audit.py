import logging
import os
from datetime import datetime

LOG_DIR = os.path.join(os.path.dirname(__file__), '../../logs')
if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

logging.basicConfig(
    filename=os.path.join(LOG_DIR, 'audit.log'),
    level=logging.INFO,
    format='%(asctime)s %(levelname)s %(message)s'
)

def log_action(user, action, target=None, status='SUCCESS', details=None):
    msg = f"User: {user} | Action: {action} | Target: {target} | Status: {status}"
    if details:
        msg += f" | Details: {details}"
    logging.info(msg)
