def text_stats(text):
    
    res = {}
    lst_text = text.split()
    for i in range(len(lst_text)):
        lst_text[i] = lst_text[i].lower()
        
    for i in text:
        if i in ["!", ","]:
            text = text.replace(i, "")
    
    unique_words = 0
    for n in lst_text:
        if lst_text.count(n) == 1:
            unique_words += lst_text.count(n)
    res["unique_words"] = unique_words
            
    a = lst_text[0]
    for i in range(len(lst_text)):
        if len(a) < len(lst_text[i]):
            a = lst_text[i]
    res["longest_word"] = a
    
    
    frequency = {}
    for i in lst_text:
        frequency[i] = lst_text.count(i)
    res["frequency"] = frequency
    
    words = 0
    for key, value in frequency.items():
        words += value
        
    res["words"] = words
        
    
    return res
        

print(text_stats("Python is great, and Python is easy!"))