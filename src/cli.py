import argparse
from src.main import search_files

def main():
    parser = argparse.ArgumentParser(description="File Finder++")
    parser.add_argument("query", type=str, help="File name to search for")
    parser.add_argument("--path", type=str, default=".", help="Directory to search in")
    parser.add_argument("--fuzzy", action="store_true", help="Enable fuzzy search")
    parser.add_argument("--threshold", type=int, default=70, help="Fuzzy match threshold (0-100)")
    args = parser.parse_args()

    matches = search_files(args.path, args.query, args.fuzzy, args.threshold)
    for match in matches:
        print(f"Found: {match}")

if __name__ == "__main__":
    main()