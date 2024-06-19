import requests
from bs4 import BeautifulSoup
import pandas as pd
import nltk
from nltk.corpus import stopwords
from textblob import TextBlob
import re
import os

nltk.download('punkt')
nltk.download('stopwords')

# Function to extract article text
def extract_article_text(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Try multiple ways to find the title
    title_tag = soup.find('h1')
    if not title_tag:
        title_tag = soup.find('title')  # Fallback to <title> tag if <h1> is not found

    title = title_tag.get_text(strip=True) if title_tag else 'No Title Found'
    
    # Find all paragraphs
    paragraphs = soup.find_all('p')
    if not paragraphs:
        return title, 'No Article Text Found'

    article_text = ' '.join([para.get_text(strip=True) for para in paragraphs])
    
    return title, article_text

# Function to calculate text analysis metrics
def analyze_text(text):
    # Tokenization
    sentences = nltk.sent_tokenize(text)
    words = nltk.word_tokenize(text)
    
    # Word Count
    word_count = len(words)
    
    # Positive and Negative Score
    positive_words = set(['good', 'happy', 'joy', 'excellent', 'positive', 'fortunate', 'correct', 'superior'])
    negative_words = set(['bad', 'sad', 'pain', 'terrible', 'wrong', 'inferior', 'negative'])
    
    positive_score = sum(1 for word in words if word.lower() in positive_words)
    negative_score = sum(1 for word in words if word.lower() in negative_words)
    
    # Polarity and Subjectivity
    blob = TextBlob(text)
    polarity_score = blob.sentiment.polarity
    subjectivity_score = blob.sentiment.subjectivity
    
    # Average Sentence Length
    avg_sentence_length = word_count / len(sentences) if sentences else 0
    
    # Percentage of Complex Words
    def count_syllables(word):
        word = word.lower()
        count = 0
        vowels = "aeiouy"
        if word[0] in vowels:
            count += 1
        for index in range(1, len(word)):
            if word[index] in vowels and word[index - 1] not in vowels:
                count += 1
        if word.endswith("e"):
            count -= 1
        if count == 0:
            count += 1
        return count
    
    complex_word_count = sum(1 for word in words if count_syllables(word) > 2)
    percentage_of_complex_words = (complex_word_count / word_count) * 100 if word_count else 0
    
    # Fog Index
    fog_index = 0.4 * (avg_sentence_length + percentage_of_complex_words)
    
    # Average Number of Words per Sentence
    avg_words_per_sentence = avg_sentence_length
    
    # Syllables per Word
    syllables_per_word = sum(count_syllables(word) for word in words) / word_count if word_count else 0
    
    # Personal Pronouns
    personal_pronouns = len(re.findall(r'\b(I|we|my|ours|us)\b', text, re.I))
    
    # Average Word Length
    avg_word_length = sum(len(word) for word in words) / word_count if word_count else 0
    
    return {
        'Positive Score': positive_score,
        'Negative Score': negative_score,
        'Polarity Score': polarity_score,
        'Subjectivity Score': subjectivity_score,
        'Avg Sentence Length': avg_sentence_length,
        'Percentage of Complex Words': percentage_of_complex_words,
        'Fog Index': fog_index,
        'Avg Number of Words per Sentence': avg_words_per_sentence,
        'Complex Word Count': complex_word_count,
        'Word Count': word_count,
        'Syllable per Word': syllables_per_word,
        'Personal Pronouns': personal_pronouns,
        'Avg Word Length': avg_word_length,
    }

# Read input URLs
input_df = pd.read_excel('Input.xlsx')

results = []

for index, row in input_df.iterrows():
    url_id = row['URL_ID']
    url = row['URL']
    
    # Extract article text
    title, article_text = extract_article_text(url)
    
    # Save article text to file
    with open(f'{url_id}.txt', 'w', encoding='utf-8') as file:
        file.write(title + '\n' + article_text)
    
    # Analyze text
    analysis_results = analyze_text(article_text)
    
    # Append results to list
    results.append({
        'URL_ID': url_id,
        'URL': url,
        'Title': title,
        **analysis_results
    })

# Create DataFrame from results and save to Excel
output_df = pd.DataFrame(results)
output_df.to_excel('Output Data Structure.xlsx', index=False)
