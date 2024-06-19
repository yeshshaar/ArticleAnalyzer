
# ArticleAnalyzer

ArticleAnalyzer is a Python-based tool for extracting and analyzing text from web articles. It scrapes article content from given URLs, performs text analysis, and outputs the results in a structured format.

## Features
- Extracts article title and text from URLs.
- Computes various text analysis metrics:
  - Positive Score
  - Negative Score
  - Polarity Score
  - Subjectivity Score
  - Average Sentence Length
  - Percentage of Complex Words
  - Fog Index
  - Average Number of Words per Sentence
  - Complex Word Count
  - Word Count
  - Syllable per Word
  - Personal Pronouns
  - Average Word Length

## Requirements
- Python 3.x
- `requests`
- `beautifulsoup4`
- `nltk`
- `textblob`
- `pandas`
- `openpyxl`

## Installation
1. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ArticleAnalyzer.git
   cd ArticleAnalyzer
   ```

2. Install the required dependencies:
   ```sh
   pip install -r requirements.txt
   ```

3. Ensure `nltk` resources are downloaded:
   ```python
   import nltk
   nltk.download('punkt')
   nltk.download('stopwords')
   ```

## Usage
1. Place the `Input.xlsx` file in the same directory as the script. The file should contain a list of URLs to be analyzed.
2. Run the script:
   ```sh
   python script.py
   ```
3. The script will generate text files for each article and an `Output Data Structure.xlsx` file with the analysis results.

## Project Structure
```
ArticleAnalyzer/
│
├── script.py
├── Input.xlsx
├── Output Data Structure.xlsx
├── README.md
├── requirements.txt
```

## Script Overview
- **script.py**: Main script that performs data extraction and analysis.
- **Input.xlsx**: Input file containing URLs to be analyzed.
- **Output Data Structure.xlsx**: Output file containing the analysis results.
- **README.md**: This readme file.
- **requirements.txt**: Lists all Python dependencies.

## How to Run the Script
1. Ensure all dependencies are installed:
   ```sh
   pip install -r requirements.txt
   ```
2. Place `Input.xlsx` in the same directory as the script.
3. Run the script:
   ```sh
   python script.py
   ```
4. The script will generate text files for each article and an `Output Data Structure.xlsx` file with the analysis results.




## Acknowledgments
- Thanks to the developers of `BeautifulSoup`, `nltk`, `TextBlob`, `pandas`, and `openpyxl` for their amazing libraries.

```

### requirements.txt:
```plaintext
requests
beautifulsoup4
nltk
textblob
pandas
openpyxl
```
