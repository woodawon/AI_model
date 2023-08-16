from eunjeon import Mecab

mecab = Mecab()

words = ['유튜브','는','수행','도','단계','해결','업데이트']

for word2 in words:
        if len(word2) < 2:
            words.remove(word2)
            
print(words)
