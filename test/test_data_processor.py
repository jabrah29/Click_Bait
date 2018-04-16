import unittest
import pandas as pd
from lib.data import  Data
from pandas.util.testing import assert_frame_equal
from lib.data_processor import DataProcessor
from lib.data_reader import DataReader

class TestDataProcessor(unittest.TestCase):


  def read_from_file(self,path):
    return DataReader.read_data(path)

  def setUp(self):
    data = self.read_from_file("/Users/jacobabraham/PycharmProjects/clickBait/data/bait_data.json")
    self.data_processor = DataProcessor(data)


  def test_train_classifier(self):
    self.data_processor.train_classifier()
    self.assertTrue(self.data_processor.classifier is not None)


  def test_with_data(self):
    test_data = self.read_from_file("/Users/jacobabraham/PycharmProjects/clickBait/test_data/testing_data.json")

    click_bait_data = Data("23 Life Lessons Cosmo Kramer Taught Us",1)
    non_click_bait_data = Data("President Trump signs abortion bill into law",0)
    self.data_processor.train_classifier()
    results = self.data_processor.test_with_data(test_data['article_title'])
    self.assertTrue(click_bait_data.__eq__(results[0]))
    self.assertTrue(non_click_bait_data.__eq__(results[1]))






