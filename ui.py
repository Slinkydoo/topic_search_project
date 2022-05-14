import PySimpleGUI as sg
import os
import csv

list_of_topics = ['Dogs', 'Cats', 'wildlife', 'veganism', 'Dumb ways to die']
list_of_topics_index = 0
list_of_questions = []
input_question = None
sg.theme('Darkgrey10')
topics_path = os.path.join(os.getcwd(), 'topics')
for root,dir,file in os.walk(topics_path):
    file_names = file


def create_home_win(title):
    layout_home = [[sg.Text('Welcome!')],
                   [sg.Button('Login'), sg.Button('Sign Up')],
                   [sg.Listbox(file, select_mode='extended', key='Topic', size=(30, 9))],
                   [sg.Button('Next'), sg.Button('Exit')]]
    return sg.Window(title, layout=layout_home)


def create_login_win(title):
    layout_login = [[sg.Text('Write Account details below')],
                    [sg.Text('Username'), sg.InputText()],
                    [sg.Text('Password'), sg.InputText("", key='Password', password_char='*')],
                    [sg.Button('Login'), sg.Button('Home')]]
    return sg.Window(title, layout=layout_login)


def create_signup_win(title):
    layout_signup = [[sg.Text('Create Account')],
                     [sg.Text('Username'), sg.InputText('Example: raham12')],
                     [sg.Text('Password'), sg.InputText("", key='Password', password_char='*')],
                     [sg.Text('Confirm Password'), sg.InputText("", key='Password', password_char='*')],
                     [sg.Button('Signup'), sg.Button('Home')]]
    return sg.Window(title, layout=layout_signup)


def create_pre_search_win(title):
    layout_pre_search = [[sg.Text('Create Account')],
                         [sg.Listbox(list_of_topics, select_mode='extended', key='Topic', size=(30, 9))],
                         [sg.Button('Search'), sg.Button('Home')]]
    return sg.Window(title, layout=layout_pre_search)


def create_ov_win(title):
    layout_ov = [[sg.Text(file_to_be_checked[0][:-4])],
                 [sg.InputText('What would you like to know?')],
                 [sg.Listbox(questions, select_mode='extend', key='Topic', size=(45, 9))],
                 [sg.Text(answers)],
                 [sg.Button('Confirm'), sg.Button('Back'), sg.Button('Home')]]
    return sg.Window(title, layout=layout_ov)


def create_ov_logged_in_win(title):
    layout_ov_logged_in_win = [[sg.InputText('This would be file name')],
                               [sg.InputText('This would be reference')],  # , sg.InputText('Example: raham12')],
                               [sg.Listbox(list_of_questions, select_mode='extend', key='Topic', size=(30, 9))],
                               # sg.InputText("", key='Password', password_char='*')],
                               [sg.Text(answers)],  # sg.InputText("", key='Password', password_char='*')],
                               [sg.Button('Update'), sg.Button('Confirm'), sg.Button('Back'), sg.Button('Home')]]
    return sg.Window(title, layout=layout_ov_logged_in_win)


#window = create_ov_logged_in_win('test')
#window = create_ov_win('test')
#window = create_signup_win('test')
#window = create_pre_search_win('test')
# window = create_login_win('test')
window = create_home_win('Home screen')
event,values = window.read()



if event == 'Next':
    file_to_be_checked = values['Topic']
    current_working_file_path = open(os.path.join(topics_path,file_to_be_checked[0]), "r", encoding='utf8')
    current_working_file = csv.reader(current_working_file_path, delimiter="|")
    questions = {}
    answers = {}
    for row in current_working_file:
        if row[1] == 'q':
            questions[row[0]] = row[4]
        elif row[1] == 'a':
            answers[row[0]] = row[4]
    window.close()
    print(questions)
    print(answers)
answers = []
window2 = create_ov_win('Overview')
event, values = window2.read()
row = 0
if event == 'Confirm':
    for question in questions:
        if question == values['Topic']:
            ref = row[2]
    window2.close()
    window2 = create_ov_win('test')
    event,values = window2.read()
    # for row in current_working_file:
    #     if row[1] == 'a':
    #         answers.append(row[2])



# if event == 'Ok':
#     if values[0] == '':
#         for val in values['Topic']:
#             input_question = val
#             print(input_question)
#     else:
#         input_question = p.preprocess(values[0])
#         print(input_question)
# if event == 'home':
#     window2 = create_home_win('argument')
#     event, values = window2.read()
#     # window = sg.Window('Argument Maker 1.0', layout=layout1)

