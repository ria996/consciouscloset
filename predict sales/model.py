import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import pickle

dataset = pd.read_csv('sales.csv')

dataset['Material'].fillna("Cotton", inplace=True)

dataset['price WITH code'].fillna("$0.00", inplace=True)

dataset['OG price'].fillna("$0.00", inplace=True)

X = dataset.iloc[:, :4]

def convert_item_to_int(word):
    word_dict = {'Jeans':1, 'Dress':2, 'Jacket':3, 'Shirt':4, 'Crop top':5, 'Hoodie':6, 'Sweatshirt':7}
    return word_dict[word]

X['Item type'] = X['Item type'].apply(lambda x : convert_item_to_int(x))

def convert_color_to_int(word):
    word_dict = {'Blue':1, 'Red':2, 'White':3, 'Green':4, 'Pink':5, 'Tan':6, 'Black':7, 'Gray':8, 'Beige':9, 'Brown':10, 'Purple':11, 'Yellow':12}
    return word_dict[word]

X['Color'] = X['Color'].apply(lambda x : convert_color_to_int(x))

def convert_size_to_int(word):
    word_dict = {'S':1, 'M':2, 'XS':3, 'XL':4, 'L':5}
    return word_dict[word]

X['Size'] = X['Size'].apply(lambda x : convert_size_to_int(x))

def convert_material_to_int(word):
    word_dict = {'Cotton':1, 'Polyester':2, 'Nylon':3, 'Denim':4, 'Rayon':5, 'Viscose':6, 'Modal':7}
    return word_dict[word]

X['Material'] = X['Material'].apply(lambda x : convert_material_to_int(x))
print(X)

y = dataset.iloc[:, 7]

def convert_company_to_int(word):
    word_dict = {'ThredUP':1, 'Poshmark':2, 'Vinted':3}
    return word_dict[word]

y = y.apply(lambda Y : convert_company_to_int(Y))
print(y)

from sklearn.neighbors import NearestNeighbors
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import MinMaxScaler
classifier = KNeighborsClassifier()

classifier.fit(X, y) #trains the model based on X and y, y is target

pickle.dump(classifier, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[1, 1, 2, 4]]))