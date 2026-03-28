def count_substring(string, sub_string):
    f=0
    s=0
    while(1):
        pos=string.find(sub_string,s)
        if pos==-1:
            break
        f=f+1
        s=pos+1
    return f
