class Person:
    def __init__(self, name):
        self.name = name

    def __str__(self):
        return self.name

    def push_name(self, person):
        person.name = self.name

    def attack(self, person):
        name = str(person)
        for _ in str(name):
            if _ in self.name.lower() + self.name.upper():
                name = name.replace(_, '')
        person.name = name

    def show_name(self):
        print(f"Hello, I am {self.name}")


class Destroyer:
    def __init__(self, chars, replace_chars='#'):
        self.chars = chars
        self.replace_chars = replace_chars

    def __call__(self, person):
        name = str(person)
        repl_list = []
        for _ in str(name):
            if _ in self.chars.lower() + self.chars.upper():
                name = name.replace(_, self.replace_chars)
                repl_list.append(f"'{_.lower()}'")
        print(f"Destroyed: {', '.join(set(repl_list))} from {name}'s name.")
        person.name = name
        return person


if __name__ == '__main__':
    john = Person("John")
    alberta = Person("Alberta")
    print(john, alberta)
    v_kill = Destroyer("aeiou")
    v_kill(john)
    print(john, alberta)
    alpha_kill = Destroyer("".join(chr(i) for i in range(65, 91)), "")
    print(john, alberta)
    alpha_kill(john)
    print(john, alberta)
    alberta.push_name(john)
    print(john, alberta)
    caitlin = Person("Caitlin")
    john.attack(caitlin)
    print(caitlin)
    v_kill(caitlin).show_name()
    alberta.show_name()
