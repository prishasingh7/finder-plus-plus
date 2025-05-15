from rapidfuzz import fuzz, process

def fuzzy_search(query, file_list, threshold=70, scorer=fuzz.partial_ratio):
    """Perform fuzzy search on a list of files (case-insensitive)."""
    if not file_list:
        return []

    # Lowercase all filenames and query for case-insensitive comparison
    lowered_file_map = {f.lower(): f for f in file_list}
    lowered_files = list(lowered_file_map.keys())
    lowered_query = query.lower()

    results = process.extract(lowered_query, lowered_files, scorer=scorer)
    return [lowered_file_map[match[0]] for match in results if match[1] >= threshold]