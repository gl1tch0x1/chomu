import yaml
import os

def load_config(config_path='config.yaml'):
    if not os.path.exists(config_path):
        return {}
    with open(config_path) as f:
        return yaml.safe_load(f)

def save_config(config, config_path='config.yaml'):
    with open(config_path, 'w') as f:
        yaml.safe_dump(config, f)
