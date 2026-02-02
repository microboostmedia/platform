import os
import json

def load_config(path):
    """Load configuration from a JSON file."""
    with open(path, 'r') as f:
        return json.load(f)


def save_config(config, path):
    """Save configuration to a JSON file."""
    with open(path, 'w') as f:
        json.dump(config, f, indent=4)


def ensure_directories(dirs):
    """Ensure that a list of directories exists, creating them if necessary."""
    for directory in dirs:
        if not os.path.exists(directory):
            os.makedirs(directory)