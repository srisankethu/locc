import sys
sys.path.append('../')
from code_checker import CodeChecker


class JavaCodeChecker(CodeChecker):
    """
    Runs Lines of Code Counter for Java

    :param data: Code to check
    """
    def __init__(self, data):
        super().__init__(data)
        self.single_line_comment_char = '//'
        self.multiple_line_comment_chars = [{
            'starting_char': '/*',
            'ending_char': '*/'
        }]
