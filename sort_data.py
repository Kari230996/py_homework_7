
def sort_only_names():
    with open('human_list.txt', 'r+') as file:
        temp = []
        file_read = file.readlines()
        for line in file_read:
            arr = line.split(',')
            temp.append(arr)
        new_file = sorted(temp, key= lambda x: x[1])
        file.seek(0)
        for human in new_file:
            file.write(','.join(human))
        print('Sorted!')



def sort_only_id():
    with open('human_list.txt', 'r+') as file:
        temp = []
        file_read = file.readlines()
        for line in file_read:
            arr = line.split(',')
            temp.append(arr)
        new_file = sorted(temp, key=lambda x: x[0])
        file.seek(0)
        for human in new_file:
            file.write(','.join(human))

        print('Sorted!')