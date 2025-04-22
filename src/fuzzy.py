from rapidfuzz import fuzz, process

def fuzzy_search(query, file_list, threshold=70, scorer=fuzz.partial_ratio):
    """Perform fuzzy search on a list of files."""
    if not file_list:
        return []
    
    results = process.extract(query, file_list, scorer=scorer)
    return [match[0] for match in results if match[1] >= threshold]