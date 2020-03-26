import nltk
def content_fraction(text):
    stopwords = nltk.corpus.stopwords.words('english')
    content = [w for w in text if w.lower() not in stopwords]
    return content
print(content_fraction(['This', 'car', 'is', 'so', 'beautiful', '.', 'Therefore',
 ',', 'it', 'is', 'expensive']))

# bowA = "the quick brown fox jumps over the lazy dog and".split(' ')
# bowB = "never jump over the lazy dog quickly".split(' ')
# bowAB = [w for w in bowA if w.lower() not in bowB]
# print(bowAB)