import re
import nltk
from nltk.corpus import stopwords
data = {}

# Load data
data['sample'] = open('./sample.txt', 'r').read()

stopwords_list = stopwords.words('english')
stopwords_list = stopwords_list + ['apple']


for k in data.keys():
  # Convert to lower case
  data[k] = data[k].lower()
  # Remove punctuations
  data[k] = re.sub(r'[-./?!,":;()\']',' ', data[k])
  # Remove numbers
  data[k] = re.sub('[-|0-9]', ' ', data[k])
  data[k] = data[k].split()
  # Remove stopwords
  data[k] = [w for w in data[k] if not w in stopwords_list]


print data['sample']