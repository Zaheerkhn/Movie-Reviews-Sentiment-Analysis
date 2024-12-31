import streamlit as st
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.datasets import imdb

# Load the word index and model
word_index = imdb.get_word_index()
model = load_model('model.h5')
# model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

dummy_data = pad_sequences([[0]], maxlen=500)  # Adjust based on input shape
model.evaluate(dummy_data, [[0]], verbose=0)

# Preprocess input function
def preprocess_input(review):
    words = review.lower().split()
    encoded_review = [word_index.get(word, 2) + 3 for word in words]
    padding_review = pad_sequences([encoded_review], maxlen=500)
    return padding_review


# Prediction function
def predict(review):
    x = preprocess_input(review)
    y = model.predict(x)
    sentiment = 'Positive' if y[0][0] > 0.5 else 'Negative'
    return sentiment, y[0][0]

# Streamlit app
st.title('Movie Review Sentiment Analysis')

review = st.text_area('Enter your movie review here:')
if st.button('Predict'):
    sentiment, score = predict(review)
    st.write(f'Sentiment: {sentiment}')
    st.write(f'Score: {score}')
