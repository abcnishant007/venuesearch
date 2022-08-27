import pdfplumber
from smartprint import smartprint as sprint
import csv


def extract_references_from_pdf(pdf_file, page_number_range):
    """

    :param pdf_file:
    :param page_number_range: format [firstpage, lastpage]
    Warning: The venues must follow "In:"
    :return:
    """
    with pdfplumber.open(pdf_file) as pdf:
        for page_number in range(page_number_range[0], page_number_range[1]):
            references = pdf.pages[page_number]
            italics_text = references.filter(
                lambda obj: not (obj["object_type"] == "char" and "Italics" in obj["fontname"])
            )
            sprint(italics_text.extract_text().split("2018"))  # [1].split(["In:"][1]))
            break


def extract_venues_from_text_file(text_file_references, year_start, year_end, outputfilename="output.csv", debug_=True):
    """

    :param text_file_references:
    :param year_start:
    :param year_end:
    :param outputfilename:
    :param debug_:
    :return:
    """
    journal_list = []
    with open(text_file_references) as f:
        for row in f:
            if "In:" in row or "In " in row:
                # special (but straightforward) case of handling "In:"
                journal_list.append(row.strip().split("In")[1])

            else:
                for year in [str(x) for x in range(year_start, year_end)]:
                    if year in row[:-8]:  # so that we don't read page numbers as years
                        wordlist = row.strip().split(year)[1].split(".")[2:]
                        journal_list.append(" ".join(wordlist))
                        break

            if debug_:
                sprint(row)
                sprint(journal_list[-1])
                print("****************************")

    if not debug_:
        sprint(journal_list)

    with open(outputfilename, "w") as f:
        csvwriter = csv.writer(f)

        list.sort(journal_list)

        for journal in journal_list:
            csvwriter.writerow([journal])


if __name__ == "__main__":
    extract_venues_from_text_file(
        "sample_data/references.txt", year_start=1975, year_end=2022, outputfilename="output.csv", debug_=True
    )
