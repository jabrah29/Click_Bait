import unittest
from lib.data_reader import DataReader


class TestDataReader(unittest.TestCase):

  CSV_PATH = "/Users/jacobabraham/PycharmProjects/clickBait/test_data/test_bait_data.json"
  def test_read_data(self):
    data = DataReader.read_data(self.CSV_PATH)
    self.assertEqual(2, data['article_title'].count())
