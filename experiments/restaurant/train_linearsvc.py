from os.path import dirname, join
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
from load_data import load_dataset
from model import TfidfModel

data_train = join(dirname(dirname(dirname(__file__))), "data", "vlsp2018", "corpus", "restaurant", "train.xlsx")
data_dev = join(dirname(dirname(dirname(__file__))), "data", "vlsp2018", "corpus", "restaurant", "dev.xlsx")

X_train, y_train = load_dataset(data_train)
X_dev, y_dev = load_dataset(data_dev)

model = TfidfModel("Count Trigram", CountVectorizer(ngram_range=(1, 3)))
model.load_data(X_train, y_train)
model.fit_transform()
model.train()
model.evaluate(X_dev, y_dev)
model.export(folder="exported/linearsvc")
