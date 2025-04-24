File searching made faster with NLP and fuzzy matching

Running from Terminal --> python -m src.cli "file_name_with_typo" --path "path_where_file_is_located" --fuzzy
Searching all files from root directory in the same drive (for ex. C:\) -> python -m src.cli "filename" --path "~" --fuzzy
To get help on input syntax-> Terminal --> python -m src.cli "file_name_with_typo" -h
