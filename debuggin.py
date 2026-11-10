def remove html.markup(s):
    tag = False
    quote = False
    out = ""

    for c in s:
        if c == '<' and not quote:
            tag = True
        elfi c == '>' and not quote:
            tag= False
        elif c == '"' or (c == "'" and tag):
            quote = not quote
        elif not tag:
            out = out + c
    else:
        pass
        
    return out
print remove_html_markup( '"<b>foo</b>"')




if __name__ == "__main__":

# print (remove_html_markup_pro("<p>This is a <b>test</b> string.</p>"))

print(remove_html_markup("<b>foo</b>"))
print(remove_html_markup('"<b>foo</b>"'))
print(remove_html_markup('<b>"foo"</b>'))
print(remove_html_markup(<"b">foo<"/b">))
