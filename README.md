# Movie Review Sentiment Analysis

This project is a Streamlit application for analyzing the sentiment of movie reviews. The app uses a pre-trained neural network model to predict whether a given review is positive or negative.

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)

## Overview

The Movie Review Sentiment Analysis app takes a movie review as input and predicts the sentiment of the review (positive or negative) along with a confidence score. It uses a pre-trained model trained on the IMDb dataset.

## Features

- Text input for movie reviews
- Sentiment prediction (Positive/Negative)
- Confidence score for the prediction

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps

1. **Clone the repository:**

   ```sh
   git clone https://github.com/Zaheerkhn/Movie-Reviews-Sentiment-Analysis
   cd movie-review-sentiment-analysis
2. **Install required packages:**

- Create and activate a virtual environment (optional but recommended):
   ```sh
  python -m venv venv
  source venv/bin/activate   # On Windows use `venv\Scripts\activate`
- Install the dependencies:
   ```sh
  pip install -r requirements.txt

3. Download the pre-trained model:

- Ensure you have the pre-trained model model.h5 in the Artifacts directory. You can download it or move it to the appropriate directory.


## Usage
1. Run the Streamlit app:
    
      ```sh
      streamlit run app.py

2. Open the app:

- Open the URL provided by Streamlit (usually http://localhost:8501) in your web browser.

3. Input a movie review:

- Enter your movie review in the text area and click the "Predict" button to get the sentiment prediction and confidence score.


## Contributing
- Contributions are welcome! If you have any ideas, suggestions, or bug reports, feel free to open an issue or submit a pull request.


