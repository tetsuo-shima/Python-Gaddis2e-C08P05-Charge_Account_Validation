__author__ = 'dwight'

# Write a program that reads the contents of a charge account number file into a list. Each account number is a
# seven-digit number, such as 5658845. The program should then ask the user to enter a charge account number. The
# program should determine whether the number is valid by searching for it in the list. If the number is in the list,
# the program should display a message indicating the number is valid. If the number is not in the list, the program
# should display a message indicating the number is invalid.


def main():
    account_number_list = read_in_account_numbers('account_number_list.txt')
    account_number = input('Enter account number to check validity: ')
    if is_account_number_valid(account_number, account_number_list):
        print('This account number is valid.')
    else:
        print('This account number is invalid.')


def is_account_number_valid(item, item_list):
    if item in item_list:
        return True

    return False


def read_in_account_numbers(filename):
    file = open(filename, 'r')
    account_list = []

    account_number = file.readline().rstrip('\n')

    while account_number != '':
        account_list.append(account_number)
        account_number = file.readline().rstrip('\n')

    file.close()

    return account_list


main()