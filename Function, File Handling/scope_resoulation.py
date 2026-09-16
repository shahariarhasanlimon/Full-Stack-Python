# scope --> a regiom where a variable is accessible

x = 10
print(x)

def func():
    x = 15 #local variable
    y = 20
    print(x)
    print(y)
func()

print(x) #global variable

#LEGB Rule --> Local, Enclosing, Global, Built-in scope

n = 100 #global variable

def outer():
    n = 200 #enclosing variable
    def inner():
        n = 300 #local variable
        print(n)
    inner()
    print(n)


#global --> global variable ke change korte pare, not enclosing ke
#nonlocal --> enclosing variable ke change korte pare, not global ke