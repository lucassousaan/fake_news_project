import csv

csvFile = open('results/dataset_label.csv', 'w', newline='')
writerCsv = csv.writer(csvFile)

with open("dataset/fake-news-data.csv", 'rt', encoding='utf8') as fileFake:
    readerFake = csv.reader(fileFake)
    counterFake = 0
    for rowFake in readerFake:
        if counterFake == 0:
            writerCsv.writerow([rowFake[0], rowFake[1], rowFake[2], "label"])
        else:
            writerCsv.writerow([rowFake[0], rowFake[1], rowFake[2], "falsa"])
        counterFake += 1
        if counterFake == 101:
            break
    fileFake.close()

with open("dataset/true-news-data.csv", 'rt', encoding='utf8') as fileFake:
    readerFake = csv.reader(fileFake)
    counterFake = 0
    for rowFake in readerFake:
        if counterFake > 0:
            writerCsv.writerow([rowFake[0], rowFake[1], rowFake[2], "verdadeira"])
        counterFake += 1
        if counterFake == 101:
            break
    fileFake.close()




    

# with open("dataset/true-news-data.csv", 'r') as fileTrue:
#     readerTrue = csv.reader(fileTrue)
#     counterTrue = 0
#     for rowTrue in readerTrue:
#         print(rowTrue)
#         counterTrue += 1
#         if counterTrue == 3:
#             break
#     fileTrue.close()

    