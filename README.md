# PDF Scraping
Final product of the project.

## Getting Started
1. Download the sample file.
2. Run all commands from Commands_to_run.txt
3. Import all the PDFs in Documents folder inside Sample folder
4. Run main.py
5. All informations will be appended in Book-v2.csv

## Logic
This script use `poppler-utils` to convert a PDF into an image and then uses `tesseract-ocr` and arabic `tesdata` to extract the text. We run the ocr 2 times as the arabic ocr can't accurately extract numeric values. Finally we use python`s csv library  to append the csv and also write name of extracted pdfs into a text file for future reference to reduce redundancy.

