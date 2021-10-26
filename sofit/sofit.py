import click
from .utils import *


@click.command()
def main():
    printWelcomeMessage()
    issue_text = askIssue()
    solutions = getSolutions(issue_text)
    solutions_count = len(solutions)
    if solutions_count > 0:
        printTotalSolutions(solutions_count)
        printBestSolution(solutions[0])
        if solutions_count > 1:
            printOtherSolutions(solutions[1::])
    else:
        printNoResults()


if __name__ == '__main__':
    main()
