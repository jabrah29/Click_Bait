import unittest
from lib.data_reader import DataReader
from lib import TEST_BAIT_DATA_PATH


class TestDataReader(unittest.TestCase):


  def test_read_data(self):
    data = DataReader.read_data(TEST_BAIT_DATA_PATH)
    self.assertEqual(2, data['article_title'].count())
