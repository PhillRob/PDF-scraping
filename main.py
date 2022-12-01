import os
import re
import googletrans
import functions

location_documents = r"/Users/philipp/Projects/PycharmProjects/PDF-scraping/pdf_input"# change this to location of folder where pdfs are. (i.e usually inside /Documents)
ls2 = []
os.chdir("pdf_input/")
l = os.listdir()
for ls in l:
    a = os.path.splitext(ls)
    if a[1] == ".pdf":
        a = "".join(a)
        ls2.append(a)
# find all pdfs inside the folder.
for items in ls2:
    try:
        if functions.check_dir(items) == False: #check if the pdf file is already translated and appended to csv
            #call check_dir function in functions.py
            i = 1
            with open("txt23.txt", "r") as f: # check for known arabic string format of the pdf.
                for line in f:
                    if "نوع الخدمة" in line:
                        line = line.split()
                        seven = line[3]
                        three = " ".join(line[6::])
                    if "اسم الشارع" in line:
                        line1 = line.split()
                        eight = " ".join(line1[2::])
                    if "درجة الأهمية" in line:
                        line2 = line.split()
                        nine = line2[2]
                    if "اسم المقاول" in line:
                        ten = line
                    if  "تشوه بصري" in line:
                        line3 = line.split()
                        twelve = " ".join(line3[1::])
                    if "الزيارة الميدانية" in line:
                        eleven = line
                    if "ملاحظات المهندس المشرف /" in line:
                        thirteen = line.split()
                        thirteen = " ".join(thirteen[5::])
                        if len(thirteen) == 0:
                            thirteen = "الموقع تابع لكم حسب الاختصاص"
                    if "المراقب الميداتي" in line:
                        fourteen = line.split()
                        fourteen = " ".join(fourteen[3::])
                    if "التاري" in line:
                        line = line.split(":")
                        line = line[0].split(" ")
                        zero = []
                        for e in line:
                            if e != "التاريخ":
                                zero.append(e)
                            else:
                                break
                        zero1 = " ".join(zero)
                    i+=1
                four = "هبوط ترنش خدمات"
            f.close()
            with open("txt23_eng.txt", "r") as t: # extract numbers and numeric values using regular expression.
                cont = t.read()
                patt1 = re.compile(r"\d{2}-\d{2}-\d{4}")
                matches = patt1.finditer(cont)
                i = 0
                for item in matches:
                    if i != 0:
                        break
                    one = item.group(0)
                    i+=1
                patt2 = re.compile(r"\b\d{12} ")
                matches1 = patt2.finditer(cont)
                for item in matches1:
                    two = item.group(0)
                patt3 = re.compile(r"(\d{2}-\d{2}-\d{4}) (\d{6})")
                matches3 = patt3.finditer(cont)
                for item in matches3:
                    six = item.group(2)
                patt4 = re.compile(r"N:(\d{2}\.\d*) [_ ]*E:(\d{2}.\d*)")
                matches4 = patt4.finditer(cont)
                for item in matches4:
                    five_a = item.group(2)
                    five_b = item.group(1)
                patt5 = re.compile(r"900\d{4}")
                matches5 = patt5.finditer(cont)
                for item in matches5:
                    fifteen = item.group(0)
            t.close()
            # lst_to_append1 = [
            #     ['AR', zero1, one, two, three, four, 'وصف الموقع', five_a, five_b, six, seven, eight,
            #     nine, ten, eleven, twelve, thirteen, fourteen, fifteen]
            # ] #append the arabic text in csv.

            lst_to_append = [
                ['Content', zero1, functions.get_trans(zero1), one, two, three, functions.get_trans(three)
                    , four, functions.get_trans(four), 'وصف الموقع', 'site location', five_a, five_b, six,
                 seven, functions.get_trans(seven), eight, functions.get_trans(eight), nine,
                 functions.get_trans(nine),
                 ten, functions.get_trans(ten), eleven, functions.get_trans(eleven), twelve,
                 functions.get_trans(twelve),
                 thirteen, functions.get_trans(thirteen), fourteen, functions.get_trans(fourteen), fifteen]
            ]  # append the translated text in csv.

            # lst2 = [
            #     ['','','','','','','','','','','','','','','','','','']

            # ]
            # functions.append_csv(lst2)
            # functions.append_csv(lst_to_append1)
            functions.append_csv(lst_to_append)
            functions.append_txt(items)
            os.chdir(f"{location_documents}")
    except:
        print(f"Problem in PDF {items}.")
