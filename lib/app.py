from lib.data_reader import DataReader
from lib.data_processor import DataProcessor

text_input = input("Enter Title: ")
data = DataReader.read_data("/Users/jacobabraham/PycharmProjects/clickBait/data/bait_data.json")
data_processor = DataProcessor(data)

print('processing data..')

data_processor.train_classifier()
result = data_processor.test_with_data([text_input])

print('===============')
for data in result:
  print(data.sentence + ": " + str(data.is_click_bait))
