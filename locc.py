from importlib import import_module
import sys

sys.path.append('./languages')


def locc(data, language):
    """
    Checks Lines of Code Counter for a code of particular coding language

    :param data: Code to check
    :param language: Coding language of the Code
    """
    cls = getattr(import_module('{}_code_checker'.format(language)), '{}CodeChecker'.format(language.capitalize()))
    code_checker = cls(data.split('\n')[:-1])
    code_checker.check()

    return code_checker

if __name__ == "__main__":

    sample_code = "import os"
    language = 'py'
    code_checker = locc(sample_code, 'py')
    print(code_checker.code_checker_result)
