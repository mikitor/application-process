def print_table(table, title_list):
    cell_min_length = 8

    max_cell_length = list(0 for _ in range(len(title_list)))
    for n, cell in enumerate(title_list):
        if max_cell_length[n] < len(cell):
            max_cell_length[n] = len(cell)
    for i, row in enumerate(table):
        for n, cell in enumerate(row):
            if max_cell_length[n] < len(cell):
                max_cell_length[n] = len(cell)

    sum_max_cell_length = 0
    for i in max_cell_length:
        sum_max_cell_length += i

    print("/", end="")
    print("-" * (sum_max_cell_length + len(max_cell_length)*2 + len(row) - 1), end="")
    print("\\")
    for i, n in enumerate(title_list):
        print("|" + n.center(max_cell_length[i]+2), end="")
    print("|")

    for row in table:
        print("|", end="")
        for i, cell in enumerate(row):
            print("-" * (max_cell_length[i]+2), end="|")
        print()
        for i, cell in enumerate(row):
            print("|" + cell.center(max_cell_length[i]+2), end="")
        print("|")
    print("\\", end="")
    print("-" * (sum_max_cell_length + len(max_cell_length)*2 + len(row) - 1), end="")
    print("/")


def print_menu(title, list_options, exit_message):
    print(title)
    for option in enumerate(list_options):
        print("({0}) {1}".format(option[0] + 1, option[1]))
    print("({0}) {1}".format("0", exit_message))


def get_inputs(list_labels, title):
    inputs = []
    print(title)
    for question in list_labels:
        user_input = input(question)
        inputs.append(user_input)
    return inputs


def print_error_message(message):
    print("Error: {0}".format(message))
