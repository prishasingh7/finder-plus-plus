import argparse
import time
from main import search_files
from utils import get_file_metadata, format_size, format_time

def main():
    parser = argparse.ArgumentParser(description="File Finder++")
    parser.add_argument("query", type=str, help="File name to search for")
    parser.add_argument("--path", type=str, default=".", help="Directory to search in")
    parser.add_argument("--fuzzy", action="store_true", help="Enable fuzzy search")
    parser.add_argument("--threshold", type=int, default=70, help="Fuzzy match threshold (0-100)")
    args = parser.parse_args()

    start_time = time.time()  # ⏱Start timing

    matches = search_files(args.path, args.query, args.fuzzy, args.threshold)

    end_time = time.time()  # ⏱End timing

    for match in matches:
        print(f"Found: {match}")
        meta = get_file_metadata(match)
        print(f"   ↳ Size: {format_size(meta['size'])} | Modified: {format_time(meta['modified'])}")

    elapsed = end_time - start_time
    print(f"\n⏱️  Search completed in {elapsed:.3f}s")
    

if __name__ == "__main__":
    main()
