
class Build:

    def __init__(self, name):
        self.name = name
        self.sections = []
	self.wire = {}

    def add_section(self, section):
        self.sections.append(section)

    def add_wire(self, name, bare_thickness, maximum_thickness):


