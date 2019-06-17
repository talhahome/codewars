# You have to extract a portion of the file name as follows:
# Assume it will start with date represented as long number
# Followed by an underscore
# You'll have then a filename with an extension
# It will always have an extra extension at the end

class FileNameExtractor:
    def __init__(self, dirty_file_name):
        self.dirty_file_name = dirty_file_name

    def extract_file_name(self):
        x = self.dirty_file_name.split('.')
        y = x[0].split('_')
        z = ''.join(y[1:]) + '.' + x[1]
        print(z)
        return z

Input = FileNameExtractor("1231231223123131_FILE_NAME.EXTENSION.OTHEREXTENSION")
Input.extract_file_name()
