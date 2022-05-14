import os
import csv


class Topic:
    """
    This topic object is used to store data from a topic to be edited then rewritten to a file
    """
    def __init__(self, file_info, contents):
        self.file_name = file_info[0]
        self.keywords = file_info[1]
        self.owner = file_info[2]
        self.co_owners = file_info[3]
        self.editors = file_info[4]
        if file_info[5] == 'true':
            self.public = True
        else:
            self.public = False
        self.questions = [row[2] for row in contents if row[1] == 'q']
        self.answers = [row[2] for row in contents if row[1] == 'a']
        next_node_num = 0

        for row in contents:
            if int(row[0]) >= next_node_num:
                next_node_num = int(row[0]) +1
        # if sorted in ascending order by node_id then we can use this code
        # self.next_node_num = int(contents[-1][0]
        self.next_node_num = next_node_num

    def add_node(self, q_or_a: str):
        """
        This function will add an element to either the questions or answers attribute

        :param q_or_a: a string of 'q' to add a question node or 'a' to add an answer node
        :return: an updated list with one item appended depending on q_or_a
        """
        if q_or_a == 'q':
            pass
            return self.questions
        elif q_or_a == 'a':
            pass
            return self.answers

    def edit_node(self, node_number: str):
        """
        This function will allow editing of a particular node in this topic object

        :param node_number: a string of the node number
        :return:
        """
        pass

    def delete_node(self, node_number: str):
        pass

    def add_editor(self):
        pass

    def change_ownership(self):
        pass

    def remove_editor(self):
        pass

    def add_coowner(self):
        pass

    def remove_coowner(self):
        pass
# Problem with add_node and edit_node. I need to add a new line in the file with add_node and overwrite a specific
# line with edit_node but right now it overwrites the very first line in the file


def create_topic():
    path = os.path.join(os.getcwd(), 'topics')

    # assume the file is not new
    new_file = False
    # assume the file name does not exist yet
    name_already_exists = False

    # Stay in this loop until the user enters a valid name for a Topic. It should also
    # let the user know if there are any topics that are already created. This should not
    # stop them from creating a new Topic but force them to name the file differently
    while not new_file:
        if name_already_exists:
            topic_name = input('That Topic name has already been taken please enter different Topic name:\n') + '.csv'
        else:
            topic_name = input("please type the Topic name:\n") + '.csv'
        new_file = True
        for file in os.walk(path):
            # There is a problem here where capital letters are seen as different from
            # lowercase when checking names but not when creating the file
            print(file[2])
            if topic_name in file[2]:
                new_file = False
                name_already_exists = True
                break

    file = open(os.path.join(os.getcwd(), 'topics', topic_name), 'w', encoding='utf8')
    writer_file = csv.writer(file, delimiter='|')
    writer_file.writerow(['node_id', 'q_or_a', 'content', 'keywords', 'relationships', 'reputation'])
    with open(os.path.join(os.getcwd(), 'topics', 'master.csv'), 'a', encoding='utf8') as master_topic_file_object:
        master_topic_file = csv.writer(master_topic_file_object)

    file.close()


def login():
    with open(os.path.join(os.getcwd(), 'users.csv'), 'r', encoding='utf8') as user_csv:
        user_list = csv.reader(user_csv, delimiter='|')
        logged_in = False
        while not logged_in:
            user_input = input('Please enter your username or email:\n(Enter \"b\" to return to the main menu)\n')
            if user_input.lower() == 'b':
                break
            else:
                for row in user_list:
                    if user_input == row[0] or user_input == row[1]:
                        logged_in = True
                        print(f'Welcome {row[0]}')
                        break
