# -*- coding: utf-8 -*-
from wordcloud import WordCloud
from konlpy.tag import Okt
from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

# 서평을 워드 클라우드로 만들어주는 함수
def make_wordcloud(book_review: str):
    # word cloud font (한글 깨짐 방지용)
    font_path = "C:/Windows/Fonts/malgun.ttf"

    # Okt 형태소 분석기 생성.
    okt = Okt()

    # 명사만 추출 (word cloud에 쓸모없는 글자 제외하기 위함.)
    nouns = okt.nouns(book_review)
    clean_text = ' '.join(nouns)

    # 마스크 이미지 불러오기
    mask_image_path = "C:/Users/USER/Pictures/cloud_img.png"
    mask_image = np.array(Image.open(mask_image_path))

    # 워드 클라우드 객체 생성
    wordcloud = WordCloud(
        width=800,
        height=400,
        background_color='white',
        font_path=font_path,
        mask=mask_image
    ).generate(clean_text)

    return wordcloud


if __name__ == '__main__':
    # 서평 예시
    book_review = """“고전이 박제나 형해에 머무르지 않고 생생하게 살아 있음을 보여 주는 책, 고전을 통해 오늘의 현실을 사유할 수 있는 책, 그리하여 독자 스스로 고전의 세계를 새롭게 재창조해나가는 길을 여는 책을 설계하고자 하였습니다. 
    21세기를 열어갈 미래의 주인공인 청소년 여러분, 그리고 드넓은 세계로 향하여 가치 있는 삶을 살아가고자 하는 동시대인들을 ‘지식과 사유의 보물창고 - 고전과의 대화’에 초대합니다.”

    성·사랑·일상
    고전문학 속에서 살아 숨쉬는 옛사람들의 삶, 사랑, 일상의 자취를 찾아내어 그 생생한 느낌을 현재 다시 되살린 3권은 14종의 고전을 강혜선 외 13인이 소개한다. 

    조선시대 여성의 애환을 다룬 일기와 기행문, 서사가사 등 역사성이 강한 작품을 4편(『한중록』, 『계축일기』, 『관북유람일기』, 「덴동어미 화전가」) 선정하여 최근 활발하게 일고 있는 페미니즘이라는 현재의 문제를 생각해볼 수 있는 계기로 삼았다. 상층 여성과 하층 여성의 작품을 모두 다루어 계층에 따른 여성의 자기서사가 어떻게 다른지도 보여주고자 하였다.
    이어서는 남녀의 사랑을 다룬 소설과 한시 4편(『최척전』, 『운영전』, 『이언』, 『사유악부』)을 선정하였다. 생사를 뛰어넘고 신분을 초월하며 국경을 넘나드는 다양한 사랑의 양태가 담긴 소설 그리고 단정한 여성, 원통한 여자, 음탕한 여성의 결혼생활을 담은 연작의 짧은 시, 자신의 체험적인 사랑을 장편으로 엮은 연작시 등을 통하여 조선시대 여성과 애정의 문제를 오늘날의 문제와 연결하여 생각해볼 수 있도록 하였다.
    마지막으로는 사대부 일상을 엿볼 수 있는 일기나 수필, 한시 등 6편(『매월당집』, 『부휴자담론』, 『미암일기』, 『한정록』, 『이목구심서』, 『북새잡요』)을 묶었다. 일기나 수필, 기행문 등은 오늘날 문학의 범주로 인정되지 못하고 있지만, 예전 선비에게 문학은 오늘날과 같은 순문학의 범위를 넘어서는 전반적인 문필활동이었다. 허구적인 사건을 만들거나 역사에 가탁하여 자신의 이야기를 우회적으로 펼치기도 하고, 철저한 기록정신으로 평생 일기를 적었다. 옛글을 읽다가 마음에 드는 구절을 적고 또 멋진 말을 만들어 자신이 살고자 하는 삶을 제시하기도 하였다. 시를 짓는 것이 교양의 일부였기에 일상의 모든 문제를 시에 담아냈거니와 민심과 풍속을 살피고 이를 시로 적어내는 것도 선비의 문필이었다. 이는 문학의 경계가 허물어지는 최근의 상황과 연결하여 문학의 역할에 대해 다시 생각해 볼 수 있는 계기를 준다."""


    # 워드 클라우드 시각화
    # plt.figure(figsize=(10,5))
    # plt.imshow(wordcloud, interpolation='bilinear')
    # plt.axis("off")
    # plt.show()

    wordcloud = make_wordcloud(book_review)

    # 워드 클라우드 이미지 파일 저장
    wordcloud.to_file("wordcloud.png")
