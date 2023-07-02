from code_checker import CodeCheckerResult
from locc import locc
import argparse
import glob
import os
import sys


def get_filenames(files):
    """
    Returns a list of all matching filenames

    :param files: List of file or regular expression(ex. main.py, *.py)
    """
    filenames = []
    for file in files:
        filenames = filenames + glob.glob(file)

    return filenames

def print_results(results):
    """
    Prints the Code Checker Results

    :param results List of CodeCheckerResult
    """
    results_total = CodeCheckerResult()
    for result in results:
        print(result.get('filename'))
        print(result.get('code_checker_result'))

        results_total = results_total + result.get('code_checker_result')

    print("Total")
    print(results_total)

def locc_cli(filenames):
    """
    Runs LOCC for all the filenames and returns a list of CodeCheckerResult

    :param filenames: List of all filenames to check
    """
    code_checker_results = []
    for filename in filenames:
            f = open(filename, 'r')
            ext = filename.split('.')[1]
            code_checker = locc(f.read(), ext)
            code_checker_results.append({
                'filename': filename,
                'code_checker_result': code_checker.code_checker_result
            })

            f.close()

    return code_checker_results

if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument("--files", required=True, help="files that need to be checked", type=str)
    args = parser.parse_args()
    if args.files:
        filenames = get_filenames(args.files.split(","))
        code_checker_results = locc_cli(filenames)
        print_results(code_checker_results)
