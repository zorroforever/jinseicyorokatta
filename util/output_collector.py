class OutputCollector:
    def __init__(self):
        self.contents = []

    def write(self, message):
        self.contents.append(message)

    def flush(self):
        pass

    def get_contents(self):
        return ''.join(self.contents)
