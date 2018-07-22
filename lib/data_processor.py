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
    fit_vectorized_data = self.__vectorized__data(titles)

    self.classifier = MultinomialNB()
    targets = clickbait.values
    self.classifier.fit(fit_vectorized_data,targets)



  def test_with_data(self,test_data):
    split_data = self.__split_to_list(test_data)
    count_transformed_data = self.count_vectorizer.transform(split_data)
    predictions = self.classifier.predict(count_transformed_data)
    return self.__process__predictions(test_data,predictions)


  ##Private Methods##

  def __process__predictions(self, test_data,predictions):
    results = []
    for prediction in enumerate(predictions):
      results.append(Data(test_data,prediction))
    return results

  def __split_to_list(self, data):
    return data.split(',')

  def __normalized__number_or_text(self, word):
    if word.isnumeric():
      return '###'
    else:
      return word

  def __vectorized__data(self, titles):
    self.count_vectorizer = CountVectorizer()
    return self.count_vectorizer.fit_transform(titles.values)