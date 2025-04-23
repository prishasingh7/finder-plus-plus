import os
from pathlib import Path
from datetime import datetime

def expand_path(path):
    # Expand user paths (e.g., ~/) and resolve to absolute paths.
    return Path(os.path.expanduser(path)).resolve()

def get_file_metadata(file_path):
    # Get file metadata (size, modified time, etc.).
    stats = os.stat(file_path)
    return {
        "size": stats.st_size,  # Size in bytes
        "modified": stats.st_mtime,  # Last modified time
        "created": stats.st_ctime,  # Creation time (platform-dependent)
    }

# returning the metadata after the file search is complete
# something like ↳ Size: 152 KB | Modified: 2025-04-19 18:45

def format_size(size_bytes):
    """Convert file size in bytes to KB or MB."""
    if size_bytes < 1024:
        return f"{size_bytes} B"
    elif size_bytes < 1024 * 1024:
        return f"{size_bytes / 1024:.0f} KB"
    else:
        return f"{size_bytes / (1024 * 1024):.2f} MB"

def format_time(timestamp):
    # Convert timestamp to human-readable format.
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d %H:%M")
