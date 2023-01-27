import sort_data, view_data

def start():
    while True:
        op = view_data.operation()
        if op == 1:
            view_data.add_number()

        elif op == 2:
            view_data.show_table()

        elif op == 3:
            view_data.only_fullname()

        elif op == 4:
            sort_data.sort_only_names()

        elif op == 5:
            sort_data.sort_only_id()

        elif op == 6:
            break





