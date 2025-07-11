import socket
import json
import tkinter.simpledialog as simpledialog
import tkinter.messagebox as messagebox

def receive_data(sock):
    try:
        data = json.loads(sock.recv(1024).decode())
        return data
    except json.JSONDecodeError:
        print("Error: Invalid data received from the server.")
        return None

def handle_quiz(sock):
    player_name = ask_name()
    sock.sendall(player_name.encode())
    while True:
        data = receive_data(sock)
        if not data:
            break
        if isinstance(data, dict):
            if "question" in data:
                question = data["question"]
                user_answer = ask_question(question)
                send_answer(sock, user_answer)
                feedback = sock.recv(1024).decode().strip()
                show_feedback(feedback)
            elif "score" in data:
                final_score = data["score"]
                print(f"Your final score is: {final_score}")
                sock.close()
                break
        else:
            print("Error: Invalid data received from the server.")

def ask_name():
    root = simpledialog.Tk()
    root.withdraw()
    player_name = simpledialog.askstring("Player Name", "Enter your name:")
    root.destroy()
    return player_name

def ask_question(question):
    root = simpledialog.Tk()
    root.withdraw()
    user_answer = simpledialog.askstring("Quiz Question", question)
    root.destroy()
    return user_answer

def send_answer(sock, answer):
    sock.sendall(answer.encode())

def show_feedback(feedback):
    messagebox.showinfo("Quiz Feedback", feedback)

def connect_to_server():
    server_address = ('192.168.76.12', 9999)
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(server_address)
    handle_quiz(client_socket)

if __name__ == "__main__":
    connect_to_server()

