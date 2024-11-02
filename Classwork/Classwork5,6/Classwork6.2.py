class Pen:
    def write(self):
        print("Writing")

class Heighlighter:
    def highlight(self):
        print("Highlighting")

class Marker(Pen, Heighlighter):
    pass

marker1 = Marker()
marker1.write()
marker1.highlight()