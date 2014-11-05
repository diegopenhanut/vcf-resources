#!/user/bin/python
import csv
import os

def generateHtml (directory ,title, content):
    fh = open(directory+"/index.html", "w")
    lines_of_text = ["<html>\n<head>\n<title>",
            title,"</title>\n</head>\n<body>",
            content,"\n</body>",
            "</html>"]
    fh.writelines(lines_of_text)
    fh.close()
    return
# older version don't work with "with"
# fix it later
with open('structure.csv', 'rU') as f:
    reader = csv.reader(f)
    fh = open('index.html', 'w')
    fh.writelines("<html>\n<head></head>\n<body>\n")
    for row in reader:
        fh.writelines("<a href='"+row[0]+"'>"+row[0]+"</a><br>\n")
    fh.writelines("</body>\n</html>")
    fh.close()



with open('structure.csv', 'rU') as f:
    reader = csv.reader(f)
    for row in reader:
        if not os.path.exists(row[0]):
            os.mkdir(row[0])
        generateHtml(row[0], row[1], row[2])
        
    
