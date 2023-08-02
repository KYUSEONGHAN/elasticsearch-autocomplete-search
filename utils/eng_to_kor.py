# 영어 키보드 입력을 한글 키보드로 변환용 dictionary
eng_to_kor = {
    'q': 'ㅂ', 'w': 'ㅈ', 'e': 'ㄷ', 'r': 'ㄱ', 't': 'ㅅ', 'y': 'ㅛ', 'u': 'ㅕ', 'i': 'ㅑ', 'o': 'ㅐ', 'p': 'ㅔ',
    'a': 'ㅁ', 's': 'ㄴ', 'd': 'ㅇ', 'f': 'ㄹ', 'g': 'ㅎ', 'h': 'ㅗ', 'j': 'ㅓ', 'k': 'ㅏ', 'l': 'ㅣ',
    'z': 'ㅋ', 'x': 'ㅌ', 'c': 'ㅊ', 'v': 'ㅍ', 'b': 'ㅠ', 'n': 'ㅜ', 'm': 'ㅡ',
    'Q': 'ㅃ', 'W': 'ㅉ', 'E': 'ㄸ', 'R': 'ㄲ', 'T': 'ㅆ', 'O': 'ㅒ', 'P': 'ㅖ',
    'Z': 'ㅋ', 'X': 'ㅌ', 'C': 'ㅊ', 'V': 'ㅍ', 'B': 'ㅠ', 'N': 'ㅜ', 'M': 'ㅡ'
}

# 영타 -> 한글로 변환하는 함수
def convert_to_korean(eng_text: str) -> str:
    return ''.join([eng_to_kor.get(ch, ch) for ch in eng_text])


if __name__ == '__main__':
    english_text = 'hello world' # ㅗㄷㅣㅣㅐ ㅈㅐㄱㅣㅇ
    print(convert_to_korean(english_text))