import pandas as pd
import openpyxl

from data.knusl import KnuSL  

df = pd.read_csv('data/sonheungmin.csv')

def analyze_sentiment(word): #to analyze word one by one 
    word = word.strip()
    root, polarity = KnuSL.data_list(word)
    return root, polarity if polarity != 'None' else 'Unknown'  

# Apply sentiment analysis to the entire column
df[['word_root', 'polarity']] = df['word'].astype(str).apply(analyze_sentiment).tolist()  
# Convert words to strings in case there are non-string values in your data.

# Filter and display unknown words
unknown_words = df[df['polarity'] == 'Unknown']['word'].tolist()
if unknown_words:
    print("\nWords not found in KnuSL:")
    for word in unknown_words:
        print(word)

# Display results
print(df[['word', 'word_root', 'polarity']])

df.to_excel('sentiment_results.xlsx', index=False)
