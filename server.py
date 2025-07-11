import socket
import json
import threading
from threading import Barrier

def load_questions():
    # Load quiz questions from a JSON file or database
    # For simplicity, let's define sample questions here
    questions = [
        {
            "question": "What is the capital of France? Choices: London, Berlin, Paris, Madrid",
            "answer": "Paris"
        },
        {
            "question": "Who wrote 'Romeo and Juliet'? Choices: Jane Austen, William Shakespeare, Charles Dickens, Mark Twain",
            "answer": "William Shakespeare"
        },
        {
            "question": "What is the largest mammal? Choices: Elephant, Giraffe, Blue Whale, Tiger",
            "answer": "Blue Whale"
        },
        {
            "question": "What is the chemical symbol for water? Choices: H, O, W, H2O",
            "answer": "H2O"
        },
        {
            "question": "Which planet is known as the Red Planet? Choices: Mars, Venus, Jupiter, Saturn",
            "answer": "Mars"
        },
        {
            "question": "What is the capital of Japan? Choices: Beijing, Seoul, Tokyo, Bangkok",
            "answer": "Tokyo"
        },
        {
            "question": "Who painted the Mona Lisa? Choices: Leonardo da Vinci, Vincent van Gogh, Pablo Picasso, Michelangelo",
            "answer": "Leonardo da Vinci"
        },
        {
            "question": "Which country is known as the Land of the Rising Sun? Choices: China, India, Japan, South Korea",
            "answer": "Japan"
        },
        {
            "question": "What is the chemical symbol for gold? Choices: G, Au, Go, Ag",
            "answer": "Au"
        },
        {
            "question": "Who discovered penicillin? Choices: Alexander Fleming, Marie Curie, Albert Einstein, Isaac Newton",
            "answer": "Alexander Fleming"
        }
        # Add more questions as needed
    ]
    return questions

def handle_client(conn, addr, scores, lock, names, questions, num_clients):
    print(f"Player connected: {addr}")
    player_name = conn.recv(1024).decode()
    names.append(player_name)
    score = 0
    for question_data in questions:
        question = question_data["question"]
        answer = question_data["answer"]
        conn.sendall(json.dumps({"question": question}).encode())
        client_answer = conn.recv(1024).decode().strip()
        if client_answer.lower() == answer.lower():
            score += 1
            conn.sendall(b"Correct!\n")
        else:
            conn.sendall(b"Incorrect. The correct answer is: " + answer.encode() + b"\n")
    with lock:
        scores.append((player_name, score))
    conn.sendall(json.dumps({"score": score}).encode())  # Send score as JSON data
    print(f"Player {player_name} finished with score: {score}")
    with lock:
        num_clients[0] += 1

def start_server():
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('192.168.76.12', 9999))
    server_socket.listen(5)
    print("Server is listening on port 9999...")
    scores = []
    names = []
    lock = threading.Lock()  # Lock for thread-safe access to scores list
    questions = load_questions()
    num_clients = [0]  # Counter to track the number of clients that have completed the quiz

    while num_clients[0] < 1:
        conn, addr = server_socket.accept()
        client_thread = threading.Thread(target=handle_client, args=(conn, addr, scores, lock, names, questions, num_clients))
        client_thread.start()

    # Wait for all threads to complete
    for thread in threading.enumerate():
        if thread != threading.current_thread():
            thread.join()

    server_socket.close()

    # Print final scores and determine the winner
    print("Quiz session ended. Final scores:")
    scores.sort(key=lambda x: x[1], reverse=True)
    print("Player scores:")
    for i, (player_name, score) in enumerate(scores):
        print(f"Player {player_name}: {score}")

    # Determine the winner
    if len(scores) > 1:
        if scores[0][1] == scores[1][1]:
            print("It's a tie!")
        else:
            print(f"Player {scores[0][0]} wins!")
    else:
        print("There's only one player.")

if __name__ == "__main__":
    start_server()

