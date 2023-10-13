import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Download the stopwords dataset if not already present
nltk.download('stopwords')
nltk.download('punkt')

# Define the text
text = "I love programming in Python!"

# Tokenize the text
tokens = word_tokenize(text)

# Get the list of English stopwords
stop_words = set(stopwords.words('english'))

# Filter out the stopwords
filtered_tokens = [word for word in tokens if word.lower() not in stop_words]

# Join the tokens back into a string
filtered_text = ' '.join(filtered_tokens)

print(filtered_text)
