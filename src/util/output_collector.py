import sys

from src.util.translations import get_translation


class OutputCollector:
    language = "en"

    def __init__(self, file_path=None, language="en"):
        self.contents = []
        self.file_path = file_path
        self.language = language
        self._original_stdout = sys.stdout
        sys.stdout = self

    def write(self, message):
        self.contents.append(message)
        self._original_stdout.write(message)

    def flush(self):
        self._original_stdout.flush()

    def get_contents(self):
        return ''.join(self.contents)

    def output_to_file(self, mode='w'):
        if self.file_path:
            try:
                with open(self.file_path, mode, encoding='utf-8') as f:
                    data = self.get_contents()
                    f.write(data)
                    f.flush()
            except IOError as e:
                print(get_translation("output_file_error", self.language).format(self.file_path, e))

    def restore_stdout(self):
        sys.stdout = self._original_stdout
        self._original_stdout = None
