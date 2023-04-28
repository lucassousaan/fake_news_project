import csv
import random

csvFileTest = open('results/dataset_label_shuffled.csv', 'w', newline='')
writerCsvTest = csv.writer(csvFileTest)

list1 = list(csv.reader(open('results/dataset_label.csv')))

headerList = list1.pop(0)
random.shuffle(list1)
list1 = [headerList]+list1
writerCsvTest.writerows(list1)