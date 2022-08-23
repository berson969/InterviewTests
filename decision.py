class Person:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f'{self.name}'

    def push_name(self, person):
        person.name = self.name

    def pull_name(self, person):
        self.name = person.name

    def show_name(self):
        print(f"Hello, I am {self.name}")

    def attack(self, person):
        attack_exe = Destroyer(self.name, '')
        attack_exe(person)


class Destroyer:
    def __init__(self, chars: str, replace_chars='#'):
        self.chars = chars.lower()
        self.replace_chars = replace_chars

    def __call__(self, person):
        self.name = person.name
        person.name = "".join(char if char.lower() not in self.chars else self.replace_chars for char in self.name)
        lost_char = "', '".join(sorted(set(self.name.lower()) - set(person.name.lower())))
        print(f"Destroyed: '{lost_char}' from {person.name}'s name.")
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
