from find_venues import extract_venues_from_text_file

extract_venues_from_text_file(
    "sample_data/references.txt", year_start=1975, year_end=2022, outputfilename="output.csv", debug_=True
)
