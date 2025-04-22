import os
from pathlib import Path

def expand_path(path):
    """Expand user paths (e.g., ~/) and resolve to absolute paths."""
    return Path(os.path.expanduser(path)).resolve()

def get_file_metadata(file_path):
    """Get file metadata (size, modified time, etc.)."""
    stats = os.stat(file_path)
    return {
        "size": stats.st_size,  # Size in bytes
        "modified": stats.st_mtime,  # Last modified time
        "created": stats.st_ctime,  # Creation time (platform-dependent)
    }