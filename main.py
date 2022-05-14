import os
import csv
import preprocess as process

topic_headers = ['node_id', 'q_or_a', 'content', 'keywords', 'relationships', 'reputation']
class Topic:
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
    def add_node(self):
        pass
# Problem with add_node and edit_node. I need to add a new line in the file with add_node and overwrite a specific
# line with edit_node but right now it overwrites the very first line in the file
def add_node(user_input, file_name):
    file = open(os.path.join(os.getcwd(), 'topics', file_name),'w', encoding='utf8')
    writer_file = csv.writer(file, delimiter='|')
    writer_file.writerow(user_input)


def edit_node(node_number, column_name, user_input, file_name):
    file = open(os.getcwd().join(file_name),'w', encoding='utf8')
    writer_file = csv.writer(file, delimiter='|')
    # writer_file.writerow()


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
        master_topic_file
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


if __name__ == '__main__':
    print('Welcome to the early stages of Topic navigator')
    # Open the master file that houses all the topics. This file will have keywords that user input can be compared to
    # when searching for a Topic
    with open(os.path.join(os.getcwd(), 'topics', 'master.csv'), 'r', encoding='utf8') as master_topic_file:
        master_topic_list = csv.reader(master_topic_file, delimiter='|')


        topic_chosen = False
        # possible_topics will store all topics that match any word in the keywords column for any Topic
        possible_topics = []
        while not topic_chosen:
            user_input = input('What Topic would you like to learn about today?\n')
            processed_input = process.preprocess(user_input)
            processed_input = process.get_useful_words(processed_input)

            # This loop finds the files that could answer the users question
            index = 1
            for row in master_topic_list:
                for keyword in processed_input:
                    if keyword in row[1]:
                        possible_topics.append([index, row])
                        index += 1

            # Handling input
            if len(possible_topics) == 0:
                print('Sorry there aren\'t any topics that match what you are looking for.')
            else:
                print('Here are the topics we found that may answer your question:\n')
                for index, topic in possible_topics:
                    print(index, topic[0])
                valid_input = False
                while not valid_input:
                    user_input = input('\nEnter the number of the Topic you would like to explore:\n')
                    try:
                        user_input = int(user_input)
                        if 1 > user_input > len(possible_topics):
                            print(f'Please enter a number between 1 and {len(possible_topics)}')
                        elif user_input != 1 and len(possible_topics) == 1:
                            print(f'We found only one Topic that matches your search.\nEnter \"1\" to learn about {possible_topics[0][1]}')
                        else:
                            valid_input = True
                    except ValueError as e:
                        print('Please enter a integer')

            if valid_input:
                topic_chosen = True

        with open(os.path.join(os.getcwd(), 'topics', possible_topics[user_input-1][1][0]+ '.csv'), 'r', encoding='utf8') as topic_file:
            topic_file = csv.reader(topic_file, delimiter='|')
            topic_content = [[column for column in row if column not in topic_headers] for row in topic_file if row[0] != 'node_id']
            current_topic = Topic(possible_topics[user_input - 1][1], topic_content)

        print('Program Closed')