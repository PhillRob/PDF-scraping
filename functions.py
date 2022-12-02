import os
import googletrans
import time
import csv

# change it to folder where the pdfs are
location_documents = r'/Users/philipp/Projects/PycharmProjects/PDF-scraping/pdf_input'
home_locations = r'/Users/philipp/Projects/PycharmProjects/PDF-scraping'  # change to home of the script, or where the script is.
trans = googletrans.Translator()
dirs = []


def get_trans(a):  # Take a text and detect a language and  translate it into english
	b = trans.translate(a, dest='en')
	return b.text


def run_command(name_pdf):
	os.chdir(f"{home_locations}")
	os.system(fr"pdftoppm -jpeg {location_documents}/{name_pdf} new12")  # convert PDF to image for OCR
	time.sleep(1)
	os.system(r"tesseract new12-1.jpg temp -l ara --dpi 300")  # use OCR to extract arabic text.
	time.sleep(1)
	os.system(r"tesseract new12-1.jpg temp_en -l eng --dpi 300")  # use OCR to extract numeric text.


def append_csv(rown):  # append the provided value into the csv
	os.chdir(f'{home_locations}')
	with open('output.csv', "a+") as file_csv:
		writer = csv.writer(file_csv)
		writer.writerows(rown)

	file_csv.close()


def check_dir(fl_name):  # check if the given pdf is already extracted, translated and appended.
	os.chdir(f"{location_documents}")
	with open('list.txt', "r") as tx:
		for line in tx:
			dirs.append(line[:-1])
		if fl_name in dirs:
			print(f"{fl_name} found in the directory")
			return True
		else:
			run_command(fl_name)
			tx.close()
			return False


def append_txt(name):  # append name of extracted pdf into a text file for future reference.
	os.chdir(f"{location_documents}")
	with open("list.txt", "a") as txe:
		txe.write(f"\n{name}")

def change_name():  # check if there is a space in pdf name and eliminate the space, as spaces broke the script.
    os.chdir(location_documents)
    ls = os.listdir()
    for item in ls:
        check = os.path.splitext(item)
        if check[1] == ".pdf":
            if " " in item:
                item2 = item.split(" ")
                os.rename(item, item2[-1])

