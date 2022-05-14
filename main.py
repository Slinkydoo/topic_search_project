import os
import csv
import preprocess as process
import backend

topic_headers = ['node_id', 'q_or_a', 'content', 'keywords', 'relationships', 'reputation']

print('Welcome to the early stages of Topic navigator')
# Open the master file that houses all the topics. This file will have keywords that user input can be compared to
# when searching for a Topic
with open(os.path.join(os.getcwd(), 'topics', 'master.csv'), 'r', encoding='utf8') as master_topic_file:
    master_topic_list = csv.reader(master_topic_file, delimiter='|')

    topic_chosen = False
    # possible_topics will store all topics that match any word in the "keywords" column for any Topic
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

    with open(os.path.join(os.getcwd(), 'topics', possible_topics[user_input-1][1][0] + '.csv'), 'r', encoding='utf8') as topic_file:
        topic_file = csv.reader(topic_file, delimiter='|')
        topic_content = [[column for column in row if column not in topic_headers] for row in topic_file if row[0] != 'node_id']
        current_topic = backend.Topic(possible_topics[user_input - 1][1], topic_content)

    print('Program Closed')
