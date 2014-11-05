import csv
import os

def generateHtml (directory ,title, content):
    fh = open(directory+"/index.html", "w")
    lines_of_text = ["<html>\n<head>\n<title>",
            title,"</title>\n</head>\n",
            content,"\n",
            "</html>"]
    fh.writelines(lines_of_text)
    fh.close()
    return

with open('structure.csv', 'rb') as f:
    reader = csv.reader(f)
    for row in reader:
        os.mkdir(row[0])
        generateHtml(row[0], row[1], row[2])
        
    
