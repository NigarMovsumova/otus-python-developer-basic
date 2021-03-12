from additional.Parent import Parent


class Child(Parent):

    def test(self):
        print("I am a child")


parent = Parent()
print(parent)
child = Child()
print(child)
child.test()
