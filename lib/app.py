from lib.data_reader import DataReader
from lib.data_processor import DataProcessor
from lib import BAIT_DATA_PATH
import time

class App:

  def run(self):
    text_input = input("Enter Title: ")
    start_time = time.time()

    data = DataReader.read_data(BAIT_DATA_PATH)
    data_processor = DataProcessor(data)

    #data_processor.train_classifier()
    result = data_processor.test_with_data(text_input)

    print('===============')
    print(result.sentence + ": " + str(result.is_click_bait))

    print("--- %s seconds ---" % (time.time() - start_time))


app = App()
app.run()