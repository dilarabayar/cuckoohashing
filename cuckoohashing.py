def intake():
    while True:
        num_of_table = input("Please enter number of tables: ")
        try:
            value = int(num_of_table)
            if 2 <= value <= 5:
                break
            else:
                print("Number of table must be between 2 and 5, try again")
        except ValueError:
            print("Number of table must be a number, try again")

    while True:
        size_of_table = input("Please enter size of tables: ")
        try:
            value = int(size_of_table)
            if 10 <= value <= 30:
                break
            else:
                print("Size of table must be between 10 and 30, try again")
        except ValueError:
            print("Size of table must be a number, try again")

    return int(num_of_table), int(size_of_table)


def initialise(table_size, table_number):
    tables = []

    for i in range(0, table_number):
        table = []
        for j in range(table_size):
            table.append("-")
        tables.append(table)
    return tables


def toASCII(key, string):
    value = 0
    try:
        new_key = int(key)
    except ValueError:
        try:
            new_key = float(key)
        except ValueError:
            if len(key) > 1:
                for i in range(0, len(key)):
                    value = value + ord(key[i])
                string[key] = value
                new_key = key
            else:
                new_key = key
    return string, new_key


def h1(key, table_size):
    index = key % table_size
    return round(index)


def h2(key, table_size):
    index = (key / table_size) % table_size
    return round(index)


def h3(key, table_size):
    index = (key * 2) % table_size
    return round(index)


def h4(key, table_size):
    index = (key * 3) % table_size
    return round(index)


def h5(key, table_size):
    index = (key + 7) % table_size
    return round(index)


def selection(key, select, table_size):
    index = -1

    if select == 0:
        index = h1(key, table_size)
    elif select == 1:
        index = h2(key, table_size)
    elif select == 2:
        index = h3(key, table_size)
    elif select == 3:
        index = h4(key, table_size)
    elif select == 4:
        index = h5(key, table_size)
    else:
        print("Oops! Something must went wrong!")
    return index


def search(key, hashtable):
    found = False

    for i in range(0, len(hashtable)):
        for j in range(0, len(hashtable[i])):
            if key == hashtable[i][j]:
                found = True
                return found, i, j
    return found, None, None


def insertion(key, hashtable, string):
    collision = {}
    num_of_collision = 0
    new_key = 0

    if key == "-":
        print("Sorry, This character is used to represent empty index so insertion is failed!")

    else:
        found, place, index = search(key, hashtable)
        if found:
            print("\n")
            print("Insertion is failed because it's already exist!\n")
            print("Key is found in " + str(place + 1) + "th table " + "index of it is " + str(index + 1), end=' ')
            print(hashtable[place])
            print("\n")
            loadfactor(hashtable)
            print("\n")
            return hashtable
        else:
            while True:
                for i in (range(0, len(hashtable))):

                    if type(key) == str:
                        if len(key) > 1:
                            for item in string.keys():
                                if key == item:
                                    new_key = string[item]
                        else:
                            new_key = ord(key)
                    else:
                        new_key = key

                    index = selection(new_key, i, len(hashtable[i]) - 1)

                    if hashtable[i][index] == "-":
                        if num_of_collision == 0:
                            print("\n")
                        print("Key " + str(key) + " will be inserted in place of " + str(index + 1) + " for ", end=' ')
                        print(str(i + 1), end=' | ')
                        print(*hashtable[i], sep=' ')
                        print("\n")
                        hashtable[i][index] = key
                        loadfactor(hashtable)
                        print("Total number of collision occurred is " + str(num_of_collision))
                        print("\n")
                        return hashtable

                    elif bool(collision) and key in collision.keys() and i in collision[key].keys() and index in \
                            collision[key][i]:
                        print("CYCLE OCCURRED for {0} in place of {1} for {2}. table\n".format(str(key), str(index + 1),
                                                                                               str(i + 1)))
                        print("Total number of collision occurred is " + str(num_of_collision))

                        return hashtable

                    else:  # collision is occurred
                        if num_of_collision == 0:
                            print("\n")
                        print("Key " + str(key) + " will be inserted in place of " + str(index + 1) + " for ",
                              end=' ')
                        print(str(i + 1), end=' | ')
                        print(*hashtable[i], sep=' - ')
                        num_of_collision = num_of_collision + 1
                        print(str(num_of_collision) + ". collision is occurred for " + str(key) + " in " + str(
                            i + 1) + ". table")
                        value = hashtable[i][index]
                        if key not in collision.keys():
                            collision[key] = dict()
                        if i not in collision[key].keys():
                            collision[key][i] = []
                        collision[key][i].append(index)
                        hashtable[i][index] = key
                        key = value
                        print("New table will be: ", end=' ')
                        print(str(i + 1), end=' | ')
                        print(*hashtable[i], sep=' ')
                        if i == len(hashtable) - 1:
                            print("For " + str(key) + " key " + "h" + str(1) + " will be found")
                        else:
                            print("For " + str(key) + " key " + "h" + str(i + 2) + " will be found")
                        print("\n")
    return hashtable


def deletion(key, place, index, hashtable):

    print("\n" + key + " is found in place of " + str(index + 1) + " for " + str(place + 1) + ". table ")
    print("\n")
    print("Before deletion: ")
    print(str(place + 1), end=' | ')
    print(*hashtable[place], sep=' - ')
    hashtable[place][index] = "-"
    print("After deletion: ")
    print(str(place + 1), end=' | ')
    print(*hashtable[place], sep=' - ')
    print("\n")
    loadfactor(hashtable)
    print("\n")
    print("Tables are: ")
    for i in range(0, len(hashtable)):
        print(str(i + 1), end=' | ')
        print(*hashtable[i], sep='   ')
    print("\n")

    return hashtable


def loadfactor(hashtable):
    load_factor = 0

    for i in (range(0, len(hashtable))):
        for j in (range(0, len(hashtable[i]))):
            if hashtable[i][j] != "-":
                load_factor = load_factor + 1
        print("Load Factor of table " + str(i + 1) + " is " + str(load_factor) + "/" + str(len(hashtable[0])))
        load_factor = 0


def main():
    loop = True
    string = {}

    table_number, table_size = intake()
    hashtable = initialise(table_size, table_number)

    while loop:
        print("1 for Insert\n2 for Search\n3 for Delete\n4 for Exit")
        option = input("Please enter your choice [1-4]: ")

        if option == '1':
            key = input("Please enter an integer key to insert: ")
            string, value = toASCII(key, string)
            hashtable = insertion(value, hashtable, string)
            print("Tables are: ")
            for i in range(0, len(hashtable)):
                print(str(i + 1), end=' | ')
                print(*hashtable[i], sep='   ')
            print("\n")

        elif option == '2':
            key = input("Please enter an integer key to be searched: ")
            string, value = toASCII(key, string)
            found, place, index = search(value, hashtable)
            if found:
                print(
                    "\n" + key + " is found in place of " + str(index + 1) + " for " + str(place + 1) + ". table ")
                print(str(place + 1), end=' | ')
                print(*hashtable[place], sep='   ')
                print("\n")
            else:
                print("\n")
                print("Key is not exist in any of the tables!")
                print("\n")

        elif option == '3':
            key = input("Please enter an integer key to delete: ")
            string, value = toASCII(key, string)
            found, place, index = search(value, hashtable)
            if found:
                hashtable = deletion(key, place, index, hashtable)
            else:
                print("\n")
                print("Key is not found!")
                print("\n")

        elif option == '4':
            print("\n")
            print("End of the program...Bye...")
            loop = False
        else:
            print("Wrong selection of menu!Please try again.")


if __name__ == "__main__":
    main()
