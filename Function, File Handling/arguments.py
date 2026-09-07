def addition(*args):
    print(args) 
    return sum(args)

r = addition(10, 20, 30, 40, 50)
print(r)