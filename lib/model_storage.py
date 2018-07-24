import pickle

class ModelStorage(object):
  BAYES_MODEL_FILE='./pickle_model.pkl'
  VECTOR_MODEL_FILE='./vector_model.pkl'

  def __init__(self, file_path):
    self.file_path = file_path

  def save(self, model):
    with open(self.file_path, 'wb') as file:
      pickle.dump(model, file)

  def load(self):
    with open(self.file_path, 'rb') as file:
      pickle_model = pickle.load(file)
    return pickle_model

