import re
import html
from urllib import parse
import requests

GOOGLE_TRANSLATE_URL = 'http://translate.google.cn/m?q=%s&tl=%s&sl=%s'

def translate(text, text_language="auto", to_language="auto"):

    text = parse.quote(text)
    url = GOOGLE_TRANSLATE_URL % (text,to_language,text_language)
    response = requests.get(url)
    data = response.text
    expr = r'(?s)class="(?:t0|result-container)">(.*?)<'
    result = re.findall(expr, data)
    if (len(result) == 0):
        return ""

    return html.unescape(result[0])

if __name__ == '__main__':
    print(translate("你吃饭了么?", "zh-CN", "en")) #汉语转英语
    print(translate("你吃饭了么？","zh-CN", "ja")) #汉语转日语
    print(translate("about your situation","en", "zh-CN")) #英语转汉语