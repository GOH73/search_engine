import thulac

mark = {'‘', '’', '“', '”', '，', '。', '？', '！'}
meaningless_words = {"的", "是", "你", "我", "和", "在", "了", '她', '他', '它', '得'}
meaningless = mark | meaningless_words

thu1 = thulac.thulac(seg_only=True, filt=True, rm_space=True)
with open('./txt/上嫁.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    outs = thu1.cut(text)

with open('./words/index.txt', 'w', encoding='utf-8') as file:
    for out in outs:
        out = out[0]
        if not out.isspace() and out not in meaningless:
            file.writelines(out + '\n')
print(outs)
