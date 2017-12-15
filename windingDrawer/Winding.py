
class Winding:

    def __init__(self, name):
        self.name = name
        self.sections = []

    def add_section(self, section):
        self.sections.append(section)

