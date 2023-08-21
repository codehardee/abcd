def div(a,b):
    print(a/b)

def smart_div(func):
    def innerdiv(a,b):
        if a<b:
            a,b = b,a
        return func(a,b)
    return innerdiv

div = smart_div(div)
div(2,4)
div(4,2)