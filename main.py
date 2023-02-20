from contours import contours
from detect_text import calcRectangle, detect_position_by_keyword, detect_text, getSymbols


response = detect_text("sample2.jpeg")
symbols = getSymbols(response)
positions: list = detect_position_by_keyword("テキスト", response)

if (len(positions)==0):
    print("not exists keyword.")
    exit()

# サンプルなので、複数出現あったとしても1回目の出現のみを使う
position = positions[0]

(x, y, h, w) = calcRectangle(position, symbols)

contours("sample2.jpeg", x, y, h, w)