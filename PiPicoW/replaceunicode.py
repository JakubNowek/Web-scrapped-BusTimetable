def txtReplacePL(txt):
    txt = txt.replace('&nbsp;',' ')
    txt = txt.replace('<blink>&gt;&gt;&gt;','TERAZ')
    txt = txt.replace(r'\u0105','ą')
    #txt = txt.replace(r'\u0104','Ą')
    txt = txt.replace(r'\u0107','ć')
    #txt = txt.replace(r'\u0106','Ć')
    txt = txt.replace(r'\u0119','ę')
    #txt = txt.replace(r'\u0118','Ę')
    txt = txt.replace(r'\u0142','ł')
    txt = txt.replace(r'\u0141','Ł')
    txt = txt.replace(r'\u0144','ń')
    #txt = txt.replace(r'\u0143','Ń')
    txt = txt.replace(r'\u00f3','ó')
    #txt = txt.replace(r'\u00d3','Ó')
    txt = txt.replace(r'\u015b','ś')
    txt = txt.replace(r'\u015a','Ś')
    txt = txt.replace(r'\u0179','ź')
    txt = txt.replace(r'\u017a','Ź')
    txt = txt.replace(r'\u017c','ż')
    txt = txt.replace(r'\u017b','Ż')
    return txt

def txtReplace(txt):
    txt = txt.replace('&nbsp;',' ')
    txt = txt.replace('<blink>&gt;&gt;&gt;','TERAZ')
    txt = txt.replace(u'\u0105','a')
    #txt = txt.replace(u'\u0104','A')
    txt = txt.replace(u'\u0107','c')
    #txt = txt.replace(u'\u0106','C')
    txt = txt.replace(u'\u0119','e')
    #txt = txt.replace(u'\u0118','E')
    txt = txt.replace(u'\u0142','l')
    txt = txt.replace(u'\u0141','L')
    txt = txt.replace(u'\u0144','n')
    #txt = txt.replace(u'\u0143','N')
    txt = txt.replace(u'\u00f3','o')
    #txt = txt.replace(u'\u00d3','O')
    txt = txt.replace(u'\u015b','s')
    txt = txt.replace(u'\u015a','S')
    txt = txt.replace(u'\u0179','z')
    txt = txt.replace(u'\u017a','Z')
    txt = txt.replace(u'\u017c','z')
    txt = txt.replace(u'\u017b','Z')
    return txt