import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

from pugnlp.segmentation import generate_sentences_from_files

nltk.download('vader_lexicon')

df = pd.DataFrame.from_records(generate_sentences_from_files('/home/hobs/Dropbox/notes/journal', ['md', 'txt']))
df.to_csv('/home/hobs/Dropbox/notes/journal/sentences.csv.gz')
df.size = df.size.astype(int)
df.len = df.sentence.str.len().astype(int)
df.words = df.sentence.str.split()
df.num_words = pd.Series([len(list(x)) for x in df.words], index=df.words.index)

sia = SentimentIntensityAnalyzer()
sia.polarity_scores(df.sentence.iloc[0])
sentiment = pd.DataFrame([sia.polarity_scores(s) for s in df.sentence], index=df.sentence.index)
df = pd.concat((df, sentiment), axis=1)
df.created = pd.datetools.parse_time_string(df.created)
df.modified = pd.datetools.parse_time_string(df.modified)
df.index = pd.DatetimeIndex(df.modified)
df.to_csv('/home/hobs/Dropbox/notes/journal/journal_sentiment_dated.csv.gz')
