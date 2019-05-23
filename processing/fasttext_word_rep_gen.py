from gensim.models.fasttext import FastText as ft

MODEL = "../model/cc.fr.300.bin"
MODEL2 = "../model/fr.bin"

WORDS = ["Ah non, c'est de la merde", 'Trop biiiieeenn', 'Excellent putain !']
tokens = ['enedis', 'energie', 'heureux', 'machine', 'propre', 'merde']

#classifier = load_model(MODEL)

model = ft.load_fasttext_format(MODEL2)

oov_vector = model[tokens]
print(oov_vector)