import unittest
import pandas as pd
from lib.data import  Data
from lib.data_processor import DataProcessor
from lib.data_reader import DataReader
from lib import BAIT_DATA_PATH,TEST_BAIT_DATA_PATH
from unittest.mock import MagicMock


class TestDataProcessor(unittest.TestCase):


  def setUp(self):
    data = DataReader.read_data(BAIT_DATA_PATH)
    self.data_processor = DataProcessor(data)


  def test_train_classifier(self):
    self.data_processor.train_classifier()
    self.assertTrue(self.data_processor.bayes_storage is not None)


  def test_with_data(self):
    test_data = DataReader.read_data(TEST_BAIT_DATA_PATH)

    click_bait_data = Data("23 Life Lessons Cosmo Kramer Taught Us",1)
    non_click_bait_data = Data("President Trump signs abortion bill into law",0)
    self.data_processor.train_classifier()
    results = self.data_processor.test_with_data(",".join(test_data['article_title']))
    self.assertTrue(click_bait_data.__eq__(results[0]))
    self.assertTrue(non_click_bait_data.__eq__(results[1]))






