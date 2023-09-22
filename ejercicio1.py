class Matrix:
    def __init__(self, elements):
        self.elements = elements

    def print(self):
        for row in self.elements:
            print(row)

    def transpose(self):
        print("In transpose")
        return Matrix([[row[i] for row in self.elements] for i in range(len(self.elements[0]))])

