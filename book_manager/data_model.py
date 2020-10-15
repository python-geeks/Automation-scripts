class Book:
    """ The Class for Book Record Details """

    def __init__(self, name, path, tags, notes):
        self.name = name
        self.path = path
        self.notes = notes
        self.tags = tags

    def __repr__(self):
        return f"Book Name: {self.name}\n Book path: {self.path} \n Book Notes: {self.notes}\n Book Tags: {self.tags}"
