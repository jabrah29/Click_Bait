import pickle

class ModelStorage(object):
  pickle_file='./pickle_model.pkl'

  def save(self, model):
    with open(self.pickle_file, 'wb') as file:
      pickle.dump(model, file)

  def load(self):
    with open(self.pickle_file, 'rb') as file:
      pickle_model = pickle.load(file)
    return pickle_model

