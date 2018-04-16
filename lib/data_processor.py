from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from lib.data import Data
import pickle


class DataProcessor(object):

  pick = None

  def __init__(self, data_frame):
    self.data_frame = data_frame

  def train_classifier(self):
    titles = self.data_frame['article_title']
    clickbait = self.data_frame['clickbait']
    self.count_vectorizer = CountVectorizer()
    count = self.count_vectorizer.fit_transform(titles.values)

    self.classifier = MultinomialNB()
    targets = clickbait.values
    self.classifier.fit(count,targets)



  def test_with_data(self,test_data):
    example_counts = self.count_vectorizer.transform(test_data)
    predictions = self.classifier.predict(example_counts)
    return self.__process__predictions(test_data,predictions)


  ##Private Methods##

  def __process__predictions(self, test_data,predictions):
    results = []
    for i,prediction in enumerate(predictions):
      results.append(Data(test_data[0],prediction))
    return results

  def __normalized__number_or_text(self, word):
    if word.isnumeric():
      return '###'
    else:
      return word