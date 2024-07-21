import pandas as pd

df = pd.read_csv('sonheungmin.csv')

senti_words = pd.read_json('SentiWord_info.json')
polarity = pd.read_txt('pos_pol_word.txt')

lexicon = senti_words.merge(polarity, on='word_root')

def calculate_sentiment(tokens):
    score = 0
    for token in tokens:
        if token in lexicon['word'].values:
            score += lexicon.loc[lexicon['word'] == token, 'polarity'].iloc[0]
    return score

df['sentiment_score'] = df['tokenized'].apply(calculate_sentiment)

print(df['sentiment_score'].describe())

