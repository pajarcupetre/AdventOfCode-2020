#!/usr/bin/python3

import sys
import string


def distinct_questions(list_of_responses):
    questions = set()
    for response in list_of_responses:
        for question in response:
            questions.add(question)
    return len(questions)


def same_questions(list_of_responses):
    questions_common = set(string.ascii_lowercase)
    for respone in list_of_responses:
        questions_per_answer = set()
        for question in respone:
            questions_per_answer.add(question)
        questions_common = questions_common.intersection(questions_per_answer)
    return len(questions_common)


if __name__ == '__main__':
    filename = sys.argv[1]
    file = open(filename, 'r')
    question_answered = list()
    sum = 0
    sum2 = 0
    for line in file:
        if len(line.strip()) == 0:
            if len(question_answered) > 0:
                sum += distinct_questions(question_answered)
                sum2 += same_questions(question_answered)
                question_answered = list()
        else:
            question_answered.append(line.strip())

    if len(question_answered) > 0:
        sum += distinct_questions(question_answered)
        sum2 += same_questions(question_answered)
    print("question_answered:", sum)
    print("same questions:", sum2)

