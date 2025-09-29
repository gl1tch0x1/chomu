import os

def is_ssh_root_login_enabled(config_path='/etc/ssh/sshd_config'):
    if not os.path.exists(config_path):
        return False, 'Config not found'
    with open(config_path) as f:
        for line in f:
            if line.strip().startswith('PermitRootLogin'):
                if 'yes' in line:
                    return True, 'PermitRootLogin yes found'
    return False, 'PermitRootLogin not enabled'

def suggest_hardening():
    enabled, reason = is_ssh_root_login_enabled()
    if enabled:
        return 'Warning: SSH root login is enabled. It is recommended to disable PermitRootLogin.'
    return 'SSH root login is disabled. Good!'
