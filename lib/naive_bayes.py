
import csv
import random



def loadCsv():
  filename = '/Users/jacobabraham/PycharmProjects/clickBait/data/nb_data.txt'
  dataset = open(filename, 'r')

  lines = csv.reader(open(filename, "r"))
  dataset = list(lines)
  for i in range(len(dataset)):
    dataset[i] = [float(x) for x in dataset[i]]
  return dataset

def splitDataset(dataset, splitRatio):
  trainSize = int(len(dataset) * splitRatio)
  trainSet = []
  copy = list(dataset)
  while len(trainSet) < trainSize:
    index = random.randrange(len(copy))
    trainSet.append(copy.pop(index))
  return [trainSet, copy]



set = loadCsv()
train,split = splitDataset([[1],[3],[5],[7],[9]],0.67)
print(train)