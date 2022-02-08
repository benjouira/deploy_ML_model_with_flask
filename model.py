import pickle
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer




# load my model 
filename = 'SA_model.sav'
model_with_polarity = pickle.load(open(filename, 'rb'))

# preper comment
df = pd.read_csv('../code/clean_indeed_reviews.csv' ,delimiter='~')

# ! An error when I try ‘CountVectorizer().fit(x).transform(cmt)’
# The problem is that my model was trained after a preprocessing that identified 7046 unique words, 
# and the preprocessing of my input data have identified 7045 words, 
# and I supposed to send the data to the model with the same number of columns. 
# Besides that, one of the 7045 words identified for the inference may also don't be 
# expected by the model as well wich is the '' nan value ! I decide first to change it 
# with the word 'good’ and it work ! 

x = df.new_review.fillna('good')
# x = df.new_review

def predict_function (comment):
    cmt = pd.Series(comment)
    res = CountVectorizer().fit(x).transform(cmt)
    return model_with_polarity.predict(res)
    
print ( predict_function("this product is great"))

# there was a mistake someware and the model always return 1 :(
# but in the kernal it give the true result for the same sentence