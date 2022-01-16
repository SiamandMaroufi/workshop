class FileDataSource:
    def __init__(self, filePath, mapper):
        self.filePath = filePath

    def save(self, data):
        serialized = self.mapper.serialize(data)
        with open(self.filePath, "w") as file:
            file.write(serialized)

    def load(self):
        with open(self.filePath, "r") as file:
           data = file.read(serialized)
           return self.mapper.deserialize(data)
