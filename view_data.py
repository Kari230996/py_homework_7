def operation():
    op = int(input(' 1 - добавить пользователя \n 2 - вывести таблицу \n 3 - вывести только имя и фамилию \n 4 - отсортировать по именам \n 5 - отсортировать по id \n 6 - выход \n'))
    return op

def add_number():
    id = int(input())
    name = input()
    surname = input()
    number = int(input())
    comments = input()
    line = f"{id}, {name}, {surname}, {number}, {comments}\n"

    with open('human_list.txt', 'a') as file:
        file.write(line)
    print('Saved')


def show_table():
    with open('human_list.txt', 'r') as file:
        for line in file.readlines():
            print(line, end='')

def only_fullname():
    with open('human_list.txt', 'r') as file:
        for line in file.readlines():
            arr = line.split(',')
            print(f'Имя: {arr[1]}, Фамилия: {arr[2]}')


