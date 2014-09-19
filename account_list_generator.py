__author__ = 'dwight'

import random


def generate_account_list():
    file = open('account_number_list.txt', 'w')
    number_of_accounts = 100

    for x in range(number_of_accounts):
        account_number = generate_account_number()

        for num in range(len(account_number)):
            file.write(str(account_number[num]))

        file.write('\n')

    file.close()
    print('Account number written to \'account_number_list.txt\'.')


def generate_account_number():
    length = 7
    account_number = [0] * length
    min_value = 0
    max_value = 9

    for digit in range(len(account_number)):
        account_number[digit] = random.randint(min_value, max_value)

    return account_number


generate_account_list()


