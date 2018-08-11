from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from lib.model_storage import ModelStorage
from lib.data import Data


class DataProcessor(object):

  pick = None

  def __init__(self, data_frame):
    self.data_frame = data_frame
    self.vector_storage = ModelStorage(ModelStorage.VECTOR_MODEL_FILE)
    self.bayes_storage = ModelStorage(ModelStorage.BAYES_MODEL_FILE)

  def train_classifier(self):
    clickbait = self.data_frame['clickbait']
    vectorized_data =self.__vectorize__data()
    classifier = MultinomialNB()
    classifier.fit(vectorized_data,clickbait.values)
    self.bayes_storage.save(classifier)



  def test_with_data(self,test_data):
    self.__vectorize__data()
    split_data =[test_data]
    mn_bayes = self.__load__from__file()
    count_transformed_data = self.count_vectorizer.transform(split_data)
    predictions = mn_bayes.predict(count_transformed_data)
    return self.__process__predictions(test_data,predictions)


  ##Private Methods##

  def __process__predictions(self, test_data,predictions):
    return Data(test_data, predictions[0])

  def __split_to_list(self, data):
    return data.split(',')

  def __vectorize__data(self):
    titles = self.data_frame['article_title']
    self.count_vectorizer = CountVectorizer()
    return self.count_vectorizer.fit_transform(titles.values)

  def __load__from__file(self):
    return self.bayes_storage.load()
