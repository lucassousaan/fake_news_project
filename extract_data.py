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

with open("dataset/true-news-data.csv", 'rt', encoding='utf8') as fileTrue:
    readerTrue = csv.reader(fileTrue)
    counterTrue = 0
    for rowTrue in readerTrue:
        if counterTrue > 0:
            writerCsv.writerow([rowTrue[0], rowTrue[1], rowTrue[2], "verdadeira"])
        counterTrue += 1
        if counterTrue == 101:
            break
    fileTrue.close()
    