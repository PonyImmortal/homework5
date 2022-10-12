from pprint import pprint
documents = [
 {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
 {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
 {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
 '1': ['2207 876234', '11-2', '5455 028765'],
 '2': ['10006'],
 '3': []
}
"""p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;"""


def get_name(documents_):
    number_inp = input('Введите номер документа: ')
    for people in documents_:
        if people['number'] == number_inp:
            return people['name']
    print('Неверный номер документа')
    return


"""s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;
Правильно обработайте ситуации, когда пользователь будет вводить несуществующий документ."""


def get_shelf_number(directories_):
    number_doc_inp = input('Введите номер документа ')
    for number in directories_.items():
        if number_doc_inp in number[1]:
            return number[0]
    print('Документ не найдет')
    return


"""l– list – команда, которая выведет список всех документов в формате passport “2207 876234” “Василий Гупкин”;"""


def get_list(documents_list):
    for people_doc in documents_list:
        type_get_list = people_doc['type']
        number_get_list = people_doc['number']
        name_get_list = people_doc['name']
        print(type_get_list, number_get_list, name_get_list)
    return


"""a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя 
владельца и номер полки, на котором он будет храниться. Корректно обработайте ситуацию, когда пользователь будет 
пытаться добавить документ на несуществующую полку."""


def new_people(new_type_document, new_number_document, new_doc_owner, new_directories_add):
    if new_directories_add in directories.keys():
        documents.append({"type": new_type_document, "number": new_number_document, "name": new_doc_owner})
        directories[new_directories_add].append(new_number_document)
        pprint(documents)
        pprint(directories)
    else:
        print('Введенной полки не существует. Запись не осуществлена.')
        shelf = str(input("Хотите создать новую полку для документа да/нет - "))
        if shelf == "да":
            documents.append({"type": new_type_document, "number": new_number_document, "name": new_doc_owner})
            directories[new_directories_add] = new_number_document
            pprint(documents)
            pprint(directories)
        else:
            print("Давай, до свидания!")

"""d– delete – команда, которая спросит номер документа и удалит полностью документ из каталога и его номер
из перечня полок. Предусмотрите сценарий, когда пользователь вводит несуществующий документ;"""


def del_doc(documents1, directories2):
    item = input("Введите номер документа, для удаления: ")
    check_len = len(documents1)
    for i, d in enumerate(documents1):
        if d["number"] == item:
            documents1.pop(i)
    for key, value in directories2.items():
        if item in value:
            value.remove(item)
            print("Готово")
            print(documents)
            print(directories)
    if check_len == len(documents):
        print("Документ не существует")


def move_doc(directories1):
    item = input('Введите номер документа, который хотите переместить: ')
    shelf = input('Введите номер полки, куда переместить: ')
    doc_find = False
    if shelf not in directories1:
     print ('Нет такой полки')
    else:
        for key, value in directories.items():
            if item in value:
                doc_find = True
                directories[shelf] += [item]
                value.remove(item)
            else:
                print('Нет такого документа')
                break
    if doc_find:
        print('Готово')
        print(directories)


while True:
    command = input('\n \
    Введите одну из команд: p, s, l, a. \n \
    Для выхода наберите exit. \n \
    Для вызов справки наберите help. \n \
    Ваша команда: ')
    if command == 'p':
        print(get_name(documents))
    elif command == 's':
        print(get_shelf_number(directories))
    elif command == 'l':
        print(get_list(documents))
    elif command == 'a':
        new_people(new_type_document=input("Введите тип докемента: "), new_number_document=input("Введите номер документа: "), new_doc_owner=input("Введите имя владельца документа: "), new_directories_add=input("Введит номер полки: "))
    elif command == 'd':
        print(del_doc(directories))
        print(del_doc(documents))
    elif command == 'exit':
        break
    elif command == 'help':
        print('\n \
        p – people – команда, которая спросит номер документа и выведет имя человека, которому он принадлежит;\n \
        s – shelf – команда, которая спросит номер документа и выведет номер полки, на которой он находится;\n \
        l – list – команда, которая выведет список всех документов в формате passport "2207 876234" "Василий Гупкин";\n \
        a – add – команда, которая добавит новый документ в каталог и в перечень полок, спросив его номер, тип, имя владельца и номер полки, на котором он будет храниться.')
    else:
        print('Вы ввели некорректную команду, повторите ввод.')

