import socket
from threading import thread
import random

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip_address ='192.168.1.42'
port = 8000

server.bind((ip_address, port))
server.listen()

list_of_clients= []

print("Server has started....")

def clientthread(conn, nickname):
    conn.send("Welcome to this quizroom!",encode('utf-8'))
    while True:
        try:
            message= conn.recv(2048).decode('utf-8')
            if message:
                print (message)


                broadcast(message, conn)
            else:
                remove(conn)
                remove_nickname(nickname)
        except:
            continue

questions = [
    "What is the Italian word for PIE? \a. Mozarella\n b.Pasty\n c.Patty\n d.Pizza",
    "What boils at 212 units at which scale? \n a.Fahrenheit\n b. Celsius\n c.Rankine\n d.Kelvin",
    "Which sea creature has three hearts? \n a.Dolphin\n b.Octopus\n c.Wlrus\n d.Seal",
    "Who was the character famous in our childhood rhymes associated with a lamb? \n a.Mary\n b.Jack\n c.Jhonny\n d.Mukesh",
    "How many bones does an adut human have? \n a.100\n b.206\n c.300 d.302",
    "How many wonder are there in the world? \n a.7\n b.9\n c.4\n d.8",
    "How many states are there in India? \ a.30\n b.29\n c.28\n d.27"]

answers=['d','a','b','b','b','a','b']

def clientthread(conn):
    score=0
    conn.send("Welcome to this quiz game!". encode('utf-8'))
    conn.send("You will recieve a question. The answer to that question should be one od a,b,c,d")
    conn.send("Good Luck!\n\n".encode('utf-8'))
    index, question, answer = get_random_question_answer(conn)
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            if message:
                if message.lower() == anwer:
                    score+= 1
                    conn.send(f"Bravo! Your score is {score}\n\n",encode('utf-8'))
                else:
                    conn.send("Incorrect answer! BEetter luck next time!\n\n".encode('utf-8'))
                remove_question(index)
                index, question, answer = get_random_question_answer(conn)
            else:
                remov(conn)
        except:
            continue

def get_random_question_answer(conn):
    random_index = random.randit(0,len(questions)-1)
    random_question = quesitons[random_index]
    conn.send(random_question.encode('utf-8'))
    return random_index, random_question, get_random_question_answer

def remove_question(index):
    questions.pop(index)
    answers.pop(index)   

while True:
    conn, addr = server.accept()
    conn,send('NICKNAME'.encode('utf-8'))
    nickname=conn.recv(2048).decode('utf-8')
    list_of_clients.append(conn)
    nicknames.appencd(nickname)
    print(nickname + "connected!")
    

    new_thread = Thread(target= clienthread,args=(conn,nickname))
    new_thread.start() 

    receive_thread = Thread(target=receive)
    receive_thread.start()
    write_thread = Thread(target=write)
    write_thread.start()  

    