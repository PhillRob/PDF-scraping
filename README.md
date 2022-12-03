# PDF Scraping
The script extracts arabic text from a PDF (with a certain format) translates it using google translate and adds the content of every PDF as a row to a `csv` file. 

## Getting Started
1. Create a local copy of this repo
2. Run `pip install -r requirements.txt` to install packages. This is tested for MacOs
3. Add PDF's to the `pdf_input` folder 
4. Run `main.py`
5. All information will be appended in output.csv

## Logic
This script use `poppler-utils` to convert a PDF into an image and then uses `tesseract`to extract the text via OCR. We first extract the latin charcaters and numbers and then run OCR a second time for the arabic. Finally, we use python's csv library  to append the data to csv and also write name of extracted pdfs into a text file. The script verifies the text file at the start to see if we have already proccessed the files. 

