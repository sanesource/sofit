import requests as rq
from PyInquirer import prompt
from bs4 import *
from termcolor import colored, cprint


def printWelcomeMessage():
    print('\n ', end='')
    cprint("Welcome to SOFIT!\n", 'white', 'on_blue', attrs=['bold'])


def askIssue():
    questions = [
        {
            'type': 'input',
            'name': 'issue_text',
            'message': 'Enter Issue/Error text here:',
        }
    ]
    issue_text = prompt(questions)['issue_text']
    return issue_text


def getSolutions(issue_text):
    r = rq.get('https://google.com/search?q=' + issue_text)
    soup = BeautifulSoup(r.text, 'html.parser')
    answers = soup.select('a[href^="/url?q=https://stackoverflow.com/"]')
    return answers


def printTotalSolutions(answers_count):
    total_answers_text = 'Total Solutions:'
    total_answers_output = colored(
        total_answers_text, 'green', attrs=['bold', 'underline'])
    print('\n', total_answers_output, end='')
    print(' ', answers_count)


def printBestSolution(best_solution):
    best_answer_url = best_solution['href'].replace('/url?q=', '')
    best_answer_output = colored(
        'Best Solution: ', 'green', attrs=['bold', 'underline'])
    print('\n', best_answer_output)
    cprint('\n [Question]: ', 'blue', attrs=['bold'], end='')
    print(best_solution.text)
    cprint('\n [Solution]: ', 'blue', attrs=['bold'], end='')
    print(best_answer_url)


def printOtherSolutions(other_solutions):
    other_answers_output = colored(
        'Other Answers: ', 'green', attrs=['bold', 'underline'])
    print('\n', other_answers_output, end='\n\n')

    for answer in other_solutions:
        answer_url = answer['href'].replace('/url?q=', '')
        answer_output = colored(answer_url)
        cprint(' [Solution]: ', 'blue', attrs=['bold'], end='')
        print(answer_output, end='\n\n')


def printNoResults():
    cprint('\nNo Results\n', 'red', attrs=['bold'])
