class bird:
    def intro(self):
        print("there are many types of birds")
    def flight(self):
        print("most of the bird can fly but some cannot fly")
class sparrow(bird):
    def flight(self):
        print("sparrow can fly")
class ostrich(bird):
    def flight(self):
        print("ostrich cannot fly")
b=bird()
s=sparrow()
o=ostrich()

b.intro()
b.flight()

s.intro()
s.flight()
o.intro()
o.flight()
