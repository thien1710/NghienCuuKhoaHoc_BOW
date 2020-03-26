import nltk
sentence = "the little yellow dog barked at the cat and next to the house"
grammar = ('''
    NP: {<DT>?<JJ>*<NN>} # NP
    ''')
chunkParser = nltk.RegexpParser(grammar)
tagged = nltk.pos_tag(nltk.word_tokenize(sentence))
print(tagged)
tree = chunkParser.parse(tagged)
for subtree in tree.subtrees():
    print(subtree)