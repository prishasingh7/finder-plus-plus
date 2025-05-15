import unittest
from fuzzy import fuzzy_search  # Importing the function to test

class TestFuzzySearch(unittest.TestCase):
    """Unit tests for the fuzzy_search function."""

    def setUp(self):
        """Set up a sample file list for testing."""
        self.file_list = [
            "public.pdf",
            "Achievements.pdf",
            "logo.png",
            "AMRITA.pdf",
            "Zoom"
        ]

    def test_exact_match(self):
        """Test if the search finds an exact match."""
        result = fuzzy_search("public.pdf", self.file_list)
        self.assertIn("public.pdf", result)

    def test_partial_match(self):
        """Test if fuzzy search finds a partial match."""
        result = fuzzy_search("public", self.file_list, threshold=50)
        self.assertIn("public.pdf", result)

    def test_no_match(self):
        """Test if the search correctly returns an empty list when no match is found."""
        result = fuzzy_search("random_file.txt", self.file_list)
        self.assertEqual(result, [])

    def test_case_insensitivity(self):
        """Test if the search is case insensitive."""
        result = fuzzy_search("achievements.pdf", self.file_list)
        self.assertIn("Achievements.pdf", result)

    def test_fuzzy_search_short_word(self):
        """Test fuzzy matching for a short filename."""
        result = fuzzy_search("Zoom", self.file_list, threshold=50)
        self.assertIn("Zoom", result)

if __name__ == "__main__":
    unittest.main()
