import os



def get_data_path(file_name):
  fileDir = os.path.abspath('../data')
  return os.path.join(fileDir, file_name)

def get_test_data_path(file_name):
  fileDir = os.path.abspath('../test_data')
  return os.path.join(fileDir, file_name)



BAIT_DATA_PATH = get_data_path("bait_data.json")
TEST_BAIT_DATA_PATH = get_test_data_path("test_bait_data.json")


