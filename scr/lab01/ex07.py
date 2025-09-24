ex = "thisisabracadabraHt1eadljjl12ojh."
def res_str(s):
    
    for i, ch in enumerate(s):
        if ch.isupper():
            start = i
            break
    else:
        return None  
    
    for i, ch in enumerate(s):
        if ch.isdigit() and i + 1 < len(s):
            step = (i + 1) - start
            if step <= 0:
                continue
            
            result = []
            pos = start
            while pos < len(s):
                result.append(s[pos])
                if s[pos] == '.':
                    return ''.join(result)
                pos += step
    
    return None
    
print(res_str(ex))