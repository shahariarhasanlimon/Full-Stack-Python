def print_my_name(f_name, l_name="khan"):
    print(f"Hello, {f_name} {l_name}!")

    print_my_name("Rahim", "khan")
    print_my_name("Karim")

    def greet(name, age=18):
        print(f"Hello, {name}! You are {age} years old.")

    greet("Alice")
    greet("Bob", 25)