import os
import re
import math
from eunjeon import Mecab
from tensorflow.keras.preprocessing.text import Tokenizer

os.chdir(r'C:\텍스트 분류(감정)\AI_model')
f = open('train.txt', 'r', encoding='utf8')
text = f.read()
mecab = Mecab()

tokenizer = Tokenizer()

# 불용어 지정
stopwords = ['.', ',', '?', '!', '', '"', '는', '그리고', '게다가', '더욱이', '아울러', '뿐만 아니라', '동시에', '어쩌면', '실은', '이처럼', '이는', '바로', '바야흐로', '그나저나', '또는', '이같이',
'아니면', '그러자', '하물며', '더구나', '아무튼','다시 말하면', '곧', '혹은', '정년', '그러면', '아무쪼록', '하물며', '과연', '설마', '결코', '모름지기', '응당'
, '어찌', '아마', '그러나', '그렇지만', '그럼에도', '그럼에도 불구하고', '그렇기는 해도', '단','하지만', '그런데', '다 보니', '그렇다 보니', '그렇기 때문에', '기 때문에'
,'그래서','반면에','반대로','오히려','도리어','그러므로','으므로','따라서','그러니까','그리하여','그렇게','그렇다면','특히','가령','또한'
'이때', '때문에','얼추','그러니','급기야','이에','왜냐하면','여 년','다른 한편','한편','여기서','말하자면','다만 바꿔 말하면','즉','덧붙여','덧붙이자면'
, '구체적으로', '예를 들어', '예를 들 수 있다.', '예컨대', '예를 들자면', '이야기입니다.', '뜻입니다.', '말입니다', '끝으로 마지막으로', '결국', '마침내'
, '더더군다나', '어쨋든', '여하튼', '가부간', '어쨋든지', '어찌하였든', '이런 이야기들 왜 하나 싶을 테고', '야기를 한참 했네요', '이제 다시 이야기 시작합니다.'
, '이번 내용은 꽤 긴데요.', '그래도 고지가 머지 않았으니 조금만 참고 이어가보죠.', '이제 마지막 이야기', '입니다.',
'발언을 인용하면서 이만 줄입니다.', '이번 챕터는 여기서 줄이죠', '해야 한다는점을 상기하면서 이만 줄이도록 하겠습니다.', '내친김에','어찌보면','모쪼록',
'이라 함은', '기염을 토했죠.', '맞습니다.', '네', '일단', '우선', '먼저', '앞서', '그럼 당연히', '조금만 더 이어가 보죠', '이렇듯', '비롯', '비로소', '그렇담', '행여',
'혹여','급기야','그나마도 고작','이래로','오롯이','당연한 말이지만','대게','그도그럴 것이','어쩌다 보니','요컨대','아이러니하게도','이제부터','올릴','쓸','분명',
'대충요약하자면', '통상', '결론적으로', '상당히', '시절이 하 수상하다', '얘깁니다.', '그런점에서 그런 뒤', '이런 면에서'
, '따위', '와 같은 사람들', '부류의 사람들', '왜냐하면', '중의하나', '오직', '오로지', '에 한하다', '하기만 하면', '도착하다', '까지 미치다',
'도달하다', '정도에 이르다', '할 지경이다', '결과에 이르다', '관해서는', '여러분', '하고 있다', '한 후', '혼자', '자기', '자기집',
'자기집', '우에 종합한것과같이', '총적으로 보면', '총적으로 말하면', '총적으로', '대로 하다', '으로서', '참','그만이다', '할 따름이다.'
'쿵', '탕탕', '쾅쾅', '둥둥', '봐', '봐라', '아이야', '아니', '와아', '응', '아이', '참나', '년', '월', '일', '령', '영', '일', '이', '삼', '사', '오', '육', '륙', '칠',
'팔', '구', '이천육', '이천칠', '이천팔', '이천구', '하나', '둘', '셋', '넷', '다섯', '여섯', '일곱', '여덟', '아홉', '령', '영'
'아', '휴' ,'아이구', '아이쿠', '아이고', '어', '나', '우', '저희', '따라', '의해', '을', '를', '에', '의', '가', '으로', '로', '에게', '뿐이다', '의거하여', '근거하여', '입각하여', '기준으로'
, '예하면', '예를 들면', '예를 들자면', '저', '소인', '소생', '저희', '지말고', '하지마', '하지마라', '다른', '물론', '또한', '그리고', '비길수 없다', '해서는 안된다', '뿐만 아니라' , '만이 아니다'
, '만은 아니다', '막론하고', '관계없이', '그치지 않다', '그러나', '그런데', '하지만', '든간에', '논하지 않다', '따지지 않다', '설사', '비록', '더라도', '아니면', '만 못하다', '하는 편이 낫다', '불문하고'
, '향하여', '향해서', '향하다', '쪽으로', '틈타', '이용하여', '타다', '오르다', '제외하고', '이 외에', '이 밖에', '하여야', '비로소', '한다면 몰라도', '외에도', '이곳', '여기', '부터', '기점으로', '따라서'
, '할 생각이다', '하려고하다', '이리하여', '그리하여', '그렇게 함으로써', '하지만', '일때', '할때', '앞에서', '중에서', '보는데서', '으로써', '로써', '까지', '해야한다', '일것이다'
, '반드시', '할줄알다', '할 수있다', '할수있어', '임에 틀림없다', '한다면', '등', '등등', '제', '겨우', '단지' ,'다만', '할뿐', '딩동', '댕그', '대해서', '대하여', '대하면'
, '훨씬', '얼마나', '얼마만큼', '얼마큼', '남', '여', '얼마간', '약간', '다소', '좀', '조금', '다수', '몇', '얼마', '지만', '하물며', '또한', '그러나', '그렇지만', '하지만', '이외에도', '대해 말하자면','뿐이다'
, '다음에', '반대로', '반대로 말하자면', '이와 반대로', '바꾸어서 말하면', '바꾸어서 한다면', '만약', '그렇지않으면', '까악', '툭', '딱', '삐걱거리다', '보드득', '비걱거리다', '꽈당', '응당', '해야한다', '에 가서'
, '각', '각각', '여러분', '각종', '각자', '제각기', '하도록하다', '와', '과', '그러므로', '그래서', '고로', '한 까닭에', '하기 때문에', '거니와', '이지만', '대하여', '관하여', '관한', '과연', '실로', '아니나 다를가', '생각한대로', '진짜로', '한적이있다'
, '하곤하였다', '하', '하하', '허허', '아하', '거바', '와', '오', '왜', '어째서', '무엇때문에', '어찌', '하겠는가', '무슨', '어디', '어느곳', '더군다나', '하물며', '더욱이는', '어느때', '언제', '야', '이봐', '어이', '여보시오', '흐흐'
, '흥', '휴', '헉헉', '헐떡헐떡', '영차', '여차', '어기여차', '끙끙', '아야', '앗', '아야', '콸콸', '졸졸', '좍좍', '뚝뚝', '주룩주룩', '솨', '우르르', '그래도', '또', '그리고', '바꾸어말하면', '바꾸어말하자면', '혹은', '혹시', '답다', '및', '그에 따르는', 
'때가 되어', '즉', '지든지', '설령', '가령', '하더라도', '할지라도', '일지라도', '지든지', '몇', '거의', '하마터면', '인젠', '이젠', '된바에야', '된이상', '만큼', '어찌됏든', '그위에', '게다가', '점에서 보아'
, '비추어 보아', '고려하면','하게될것이다','일것이다', '비교적','좀', '보다 더', '비하면', '시키다', '하게하다', '할만하다', '의해서', '연이서', '이어서', '잇따라', '뒤따라', '뒤이어', '결국', '의지하여', '기대여', '통하여', '자마자', '더욱더', '불구하고'
, '얼마든지',  '마음대로', '주저하지 않고',  '곧',  '즉시',  '바로',  '당장',  '하자마자',  '밖에 안된다',  '하면된다', '그래',  '그렇지',  '요컨대',  '다시 말하자면',  '바꿔 말하면',  '즉',  '구체적으로',  '말하자면'
, '시작하여', '시초에', '이상', '허', '헉', '허걱', '바와같이', '해도좋다', '해도된다', '게다가', '더구나', '하물며', '와르르', '팍', '퍽', '펄렁', '동안', '이래', '하고있었다', '이었다', '에서', '로부터', '까지', '예하면', '했어요', '해요','함께', '같이', '더불어'
, '마저', '마저도', '양자','모두', '습니다', '가까스로', '하려고하다', '즈음하여', '다른', '다른 방면으로', '해봐요', '습니까', '했어요', '말할것도 없고', '무릎쓰고', '개의치않고', '하는것만 못하다'
, '하는것이 낫다', '매', '매번','들', '모','어느것', '어느', '로써', '갖고말하자면', '어디', '어느쪽', '어느것', '어느해', '어느 년도', '라 해도', '언젠가', '어떤것', '어느것', '저기', '저쪽', '저것', '그때', '그럼', '그러면', '요만한걸', '그래', '그때', '저것만큼'
, '그저', '이르기까지', '할 줄 안다', '할 힘이 있다', '너', '너희', '당신', '어찌', '설마', '차라리', '할지언정', '할지라도', '할망정', '할지언정', '구토하다', '게우다', '토하다', '메쓰겁다'
, '옆사람', '퉤', '쳇', '의거하여', '근거하여', '의해', '따라', '힘입어', '그', '다음', '버금', '두번째로', '기타', '첫번째로', '나머지는', '그중에서', '견지에서', '형식으로 쓰여', '입장에서'
, '위해서', '단지', '의해되다', '하도록시키다', '뿐만아니라', '반대로', '전후', '전자', '앞의것', '잠시', '잠깐', '하면서', '그렇지만', '다음에', '그러한즉', '그런즉', '남들', '아무거나', '어찌하든지', '같다', '비슷하다', '예컨대', '이럴정도로', '어떻게', '만약'
, '만일', '위에서 서술한바와같이', '인 듯하다', '하지 않는다면', '만약에', '무엇', '무슨', '어느', '어떤', '아래윗', '조차', '한데', '그럼에도 불구하고', '여전히', '심지어', '까지도', '조차도', '하지 않도록', '않기 위하여', '때', '시각', '무렵', '시간', '동안'
, '어때','어떠한', '하여금', '네', '예', '우선', '누구', '누가 알겠는import os가', '아무도', '줄은모른다', '줄은 몰랏다', '하는 김에', '겸사겸사', '하는바', '그런 까닭에', '한 이유는', '그러니', '그러니까'
, '때문에', '그', '너희', '그들', '너희들', '타인', '것', '것들', '너', '위하여', '공동으로', '동시에', '하기 위하여', '어찌하여', '무엇때문에', '붕붕', '윙윙', '나', '우리', '엉엉', '휘익', '윙윙'
, '오호','아하', '어쨋든', '만 못하다', '하기보다는', '차라리', '하는 편이 낫다', '흐흐', '놀라다', '상대적으로 말하자면', '마치', '아니라면', '쉿', '그렇지 않으면', '그렇지 않다면', '안 그러면', '아니었다면', '하든지', '아니면', '이라면', '좋아', '알았어', '하는것도'
, '그만이다', '어쩔수 없다', '하나', '일', '일반적으로', '일단', '한켠으로는', '오자마자', '이렇게되면','이와같다면', '전부', '한마디', '한항목', '근거로', '하기에', '아울러', '하지 않도록', '않기 위해서', '이르기까지', '이 되다', '로 인하여', '까닭으로', '이유만으로'
, '이로 인하여', '그래서', '이 때문에', '그러므로', '그런 까닭에', '알 수 있다', '결론을 낼 수 있다', '으로 인하여', '있다', '어떤것', '관계가 있다', '관련이 있다', '연관되다', '어떤것들', '에 대해', '이리하여', '그리하여', '여부', '하기보다는', '하느니', '하면 할수록', '운운', '이러이러하다', '하구나']

processed_text = [] #전처리 결과
vocab = {} #단어 빈도수
encoded_text = [] #정수 인코딩 결과

# 전처리 함수
def text_process(a):
    processed_text = []
    for sentence in a:
        temp_X = mecab.morphs(sentence)
        temp_X = [word for word in temp_X if not word in stopwords]
        processed_text.append(temp_X)
    return processed_text

def Integer_Encoding(processed_text):
    tokenizer.fit_on_texts(processed_text)
    return tokenizer.word_index

def calculate_knowledge_probability(encoded_text, input_text):
    input_processed = text_process([input_text])
    input_encoded = tokenizer.texts_to_sequences(input_processed)

    total_words = sum([len(sentence) for sentence in input_processed])
    matched_words = sum([len([word for word in sentence if word in tokenizer.word_index]) for sentence in input_processed])

    if total_words == 0: return 0

    train_data_unique_words = len(encoded_text)
    probability = (matched_words / train_data_unique_words) * 100

    return probability

processed_text = text_process(text.split('\n'))
encoded_text = Integer_Encoding(processed_text)

while True:
    input_text = input("텍스트를 입력하세요 (끝내려면 '종료' 입력): ")
    if input_text == "종료":
        break

    knowledge_probability = calculate_knowledge_probability(encoded_text, input_text)
    print(f"당신은 이 분야에 대해 {knowledge_probability:.2f}% 알고 있습니다.")