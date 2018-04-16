import pandas as pd

class DataReader(object):

  @staticmethod
  def read_data(path):
    data = pd.read_json(path)
    data = data.drop('author', axis =1)
    data = data.drop('response_count', axis=1)
    return data