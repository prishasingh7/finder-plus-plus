import os
import argparse
from pathlib import Path
from src.fuzzy import fuzzy_search

def search_files(directory, query, use_fuzzy=False, threshold=70):
    """Search for files in a directory, optionally using fuzzy matching."""
    print(f"Searching in: {directory}")  # Debugging line
    results = []
    file_list = []

    # Collect all files in the directory
    for root, _, files in os.walk(os.path.expanduser(directory)):
        for file in files:
            file_list.append(os.path.join(root, file))

    if use_fuzzy:
        # Use fuzzy search if enabled
        results = fuzzy_search(query, file_list, threshold)
    else:
        # Use exact match search
        results = [file for file in file_list if query.lower() in file.lower()]

    if not results:
        print("No files found.")
    return results

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="File Finder++")
    parser.add_argument("query", type=str, help="File name to search for")
    parser.add_argument("--path", type=str, default=".", help="Directory to search in")
    parser.add_argument("--fuzzy", action="store_true", help="Enable fuzzy search")
    parser.add_argument("--threshold", type=int, default=70, help="Fuzzy match threshold (0-100)")
    args = parser.parse_args()

    matches = search_files(args.path, args.query, args.fuzzy, args.threshold)
    for match in matches:
        print(f"Found: {match}")
