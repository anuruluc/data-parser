# utils.py

import logging
import os
import re
import datetime

def configure_logger(name, level=logging.INFO):
    """Configure a logger."""
    logger = logging.getLogger(name)
    logger.setLevel(level)
    handler = logging.StreamHandler()
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    return logger

def get_project_root():
    """Get the project root directory."""
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def parse_date(date_str):
    """Parse a date string."""
    date_formats = ['%Y-%m-%d', '%Y-%m-%d %H:%M:%S', '%Y-%m-%d %H:%M:%S.%f']
    for date_format in date_formats:
        try:
            return datetime.datetime.strptime(date_str, date_format)
        except ValueError:
            pass
    raise ValueError('Invalid date format')

def slugify(string):
    """Convert a string to a slug."""
    return re.sub(r'\W+', '-', string).strip('-').lower()

def load_json(filename):
    """Load a JSON file."""
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except Exception as e:
        raise ValueError(f'Failed to load {filename}: {e}')

def save_json(data, filename):
    """Save data to a JSON file."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def get_files(directory, pattern):
    """Get files in a directory matching a pattern."""
    return [f for f in os.listdir(directory) if re.match(pattern, f)]