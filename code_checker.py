from prettytable import PrettyTable

class CodeCheckerResult:
    """
    Class that stores the code checker result
    """
    def __init__(self):
        self.blank_lines = 0
        self.lines_with_comments = 0
        self.lines_with_code = 0
        self.lines_in_the_file = 0
        self.lines_with_import = 0

    def __add__(self, other):
        new = CodeCheckerResult()
        for key in CodeCheckerResult().__dict__.keys():
            setattr(new, key, getattr(self, key) + getattr(other, key))

        return new

    def __str__(self):
        table = PrettyTable(['Blank', 'Comments', 'Code', 'Import Lines', 'Total'])
        table.add_row([
            self.blank_lines,
            self.lines_with_comments,
            self.lines_with_code,
            self.lines_with_import,
            self.lines_in_the_file
        ])
        print(table)
        return ''


class CodeChecker:
    """
    Runs Lines of Code Counter

    :param data: Code to check
    """

    def __init__(self, data):
        self.__data = data
        self.code_checker_result = CodeCheckerResult()
        self.single_line_comment_char = None
        self.multiple_line_comment_chars = None

    def __str__(self):
        print(self.code_checker_result)
        return ''

    def number_of_blank_lines(self):
        """
        Returns number of blank lines
        """
        count = 0
        for line in self.__data:
            if line.strip() == '':
                count = count + 1
        return count

    def check_multiple_line_comments(self, multiple_line_comment_char):
        """
        Returns lines count of multiple line comments

        :param multiple_line_comment_char: Contains a dict of staring_char and ending_char to determine multiple line comments
        """
        flag = 0
        count = 0
        updated_data = []
        for line in self.__data:
            if multiple_line_comment_char.get('starting_char') in line and flag == 0:
                flag = 1
                if not line.strip().startswith(multiple_line_comment_char.get('starting_char')):
                    count = count - 1
            elif multiple_line_comment_char.get('ending_char') in line and flag == 1:
                flag = 0
                if line.strip().endswith(multiple_line_comment_char.get('ending_char')):
                    count = count + 1

            if flag != 0:
                count = count + 1
            else:
                updated_data.append(line)

        self.__data = updated_data

        return count

    def check_lines_with_single_line_comments(self, single_line_comment_char):
        """
        Return the count of single line comments

        :param single_line_comment_char: The char which determines a single line comment
        """
        count = 0
        updated_data = []
        for line in self.__data:
            if line.strip().startswith(single_line_comment_char):
                count = count + 1
            else:
                updated_data.append(line)

        self.__data = updated_data

        return count

    def check(self):
        """
        Runs the logic for Lines of Code Counter
        """
        self.code_checker_result.lines_in_the_file = len(self.__data)
        for multiple_line_comment_char in self.multiple_line_comment_chars:
            self.code_checker_result.lines_with_comments = self.code_checker_result.lines_with_comments + self.check_multiple_line_comments(multiple_line_comment_char)
        self.code_checker_result.lines_with_comments = self.code_checker_result.lines_with_comments + self.check_lines_with_single_line_comments(self.single_line_comment_char)
        self.code_checker_result.blank_lines = self.number_of_blank_lines()
        self.code_checker_result.lines_with_code = self.code_checker_result.lines_in_the_file - self.code_checker_result.lines_with_comments - self.code_checker_result.blank_lines
