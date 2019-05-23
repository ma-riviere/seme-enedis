from gensim.models import FastText

WORDS = ["Ah non, c'est de la merde", 'Trop biiiieeenn', 'Excellent putain !']

model = FastText(WORDS, size=100, window=5, min_count=5, workers=4, sg=1)

