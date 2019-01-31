
class Section:

    def __init__(self, name, layers, inter_layer_insulation=True, start_point = (2,0), length=5, space=0.5):
        self.name = name
        self.layers = layers
 #       self.start_direction = start_direction
        self.inter_layer_insulation = inter_layer_insulation
        self.start_point = start_point
        self.length = length
        self.space = space
        self.asy_commands = []
        self.currentpen = 0.5

    def set_number_turns_per_layer(self,turns_per_layer):
        self.turns_per_layer = turns_per_layer

    def set_wire_parameters(self, bare_wire_dia, enam_wire_dia):
        self.bare_wire_dia = bare_wire_dia
        self.enam_wire_dia = enam_wire_dia

    def set_insulation_thickness(self, thickness):
        self.ins_thickness = thickness

    def set_start_label(self):
        start_label_point = (self.start_point[0]-0.25, self.start_point[1])
        self.asy_commands.append('label("1",(%s, %s));' % start_label_point)

    def set_end_label(self):
        # Assume arror is pointig left
        end_label_point = (self.end_point[0]-0.25, self.end_point[1])
        # If its pointing right position the label to the right
        if self.end_point[0] > self.start_point[0]:
            end_label_point = (self.end_point[0] + 0.25, self.end_point[1])
        self.asy_commands.append('label("1",(%s, %s));' % end_label_point)

    def create_asy_commands(self):

        self.asy_commands.append('defaultpen(fontsize(10pt));')
        self.asy_commands.append('currentpen=linewidth(%s);' % self.currentpen)

        current_start_point = self.start_point
        length = self.length

        # Draw the layers
        for layer in range(0,self.layers):
            end_point = current_start_point
            end_point= (end_point[0] + length, end_point[1])

            self.asy_commands.append('draw(%s -- %s, arrow=Arrow);' % (current_start_point,end_point))

            current_start_point = end_point
            end_point = (current_start_point[0],current_start_point[1] + self.space)

            # last layer doesnt need a connector
            if layer == self.layers -1:
                break

            self.asy_commands.append('draw(%s -- %s);' % (current_start_point, end_point))
            current_start_point = end_point

            length *= -1


        end_x = self.start_point[0]
        end_y = current_start_point[1]

        # The most LHS of the top
        self.last_top_home = (end_x, end_y)
        self.end_point = current_start_point


        # Draw the insulation if any
        if self.inter_layer_insulation :
            number_of_ins_layers = self.layers -1

            for ins in range(0, number_of_ins_layers):

                y_offset = (self.space/2.0) + (ins * self.space)

                start_point = (self.start_point[0], y_offset)
                end_point = (self.start_point[0] + self.length, y_offset)
                self.asy_commands.append('draw(%s -- %s, currentpen+dashed);' % (start_point, end_point) )

        # draw dots at start and end
        self.asy_commands.append('currentpen=linewidth(%s);' % (self.currentpen*3))
        self.asy_commands.append('dot((%s ,%s));' % self.start_point)
        self.asy_commands.append('dot((%s, %s));' % self.end_point)




