class ReadFile(object):

    def __init__(self, filename):

        self.filename = filename
        self.data = []
        self.read_file()

    def read_file(self):

        x, y = [], []
        with open(self.filename, "r") as file:
            nb_lines = 0
            for line in file:
                nb_lines += 1
                if nb_lines > 3:
                    line_split = line.replace("\n", "").split("    ")
                    x.append(float(line_split[0]))
                    y.append(float(line_split[1]))

        self.data = [x, y]
