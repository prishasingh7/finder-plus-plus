File searching made faster with NLP and fuzzy matching

Running from Terminal --> python -m src.cli "file_name_with_typo" --path "path_where_file_is_located" --fuzzy
Searching all files from root directory in the same drive (for ex. C:\) -> python -m src.cli "filename" --path "~" --fuzzy
To get help on input syntax-> Terminal --> python -m src.cli "file_name_with_typo" -h

Upcoming features:
Metadata filtering
NLP based queries
SQLite based temporary query caching


## License (Research Paper)

The research paper "Study of Intelligent File Search Systems Using Natural Language Processing and Machine Learning Techniques" is licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International License (CC BY-NC-ND 4.0).

You may share the paper with proper attribution. Commercial use, modifications, and derivative works are prohibited without explicit permission.

[Learn more about CC BY-NC-ND 4.0](https://creativecommons.org/licenses/by-nc-nd/4.0/)



