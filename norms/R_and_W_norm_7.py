import csv

with open("csv_norm_7", mode="w+", newline="", encoding="utf-8") as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['John', 'Smith', '-', 85])
    writer.writerow(['Emily', 'johnson', '-', 90])
    writer.writerow(['Michael', 'Brown', '-', 78])

    csvfile.seek(0)
    reader = csv.reader(csvfile)
    # for row in reader:
    #     for i in row:






# with open("csv_norm_7", mode="w", newline="", encoding="utf-8") as csvfile:
#     writer = csv.writer(csvfile)













