import sys
sys.path.append('../')
from code_checker import CodeChecker


class PyCodeChecker(CodeChecker):
    """
    Runs Lines of Code Counter for Python

    :param data: Code to check
    """
    def __init__(self, data):
        super().__init__(data)
        self.single_line_comment_char = '#'
        self.multiple_line_comment_chars = [{
            'starting_char': '"""',
            'ending_char': '"""'
        },
        {
            'starting_char': "'''",
            'ending_char': "'''"
        }]

    def check_for_import_lines(self):
        """
        Returns the count of import lines
        """
        count = 0
        for line in self._CodeChecker__data:
            if 'import' in line:
                count = count + 1

        return count

    def check(self):
        """
        Runs the logic for Lines of Code Counter
        """
        super().check()
        self.code_checker_result.lines_with_import = self.check_for_import_lines()
