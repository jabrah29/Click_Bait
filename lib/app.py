from lib.data_reader import DataReader
from lib.data_processor import DataProcessor
from lib import BAIT_DATA_PATH
class App:

  def run(self):
    text_input = input("Enter Title: ")
    data = DataReader.read_data(BAIT_DATA_PATH)
    data_processor = DataProcessor(data)

    data_processor.train_classifier()
    result = data_processor.test_with_data(text_input)

    print('===============')
    for data in result:
      print(data.sentence + ": " + str(data.is_click_bait))



app = App()
app.run()