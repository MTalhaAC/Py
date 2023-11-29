import collections

class CustomCollections:
  def __init__(self, collection):
    self.collection = collection
  
  def getCount(self):
    counts = collections.Counter(self.collection)
    return counts