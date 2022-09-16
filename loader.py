import csv
# with open('respostas.csv', newline='') as csvfile:
#     spamreader = csv.reader(csvfile, delimiter=' ', quotechar=',')
#         for row in spamreader:
#             print(', '.join(row))
with open('respostas.csv') as csvfile:
    dialect = csv.Sniffer().sniff(csvfile.read(1024))
    # teste= csv.Sniffer().has_header(csvfile.read(1024))
    # print(teste)
    csvfile.seek(0)
    reader = csv.reader(csvfile, dialect)
    for row in reader:  
        print(row[3])
