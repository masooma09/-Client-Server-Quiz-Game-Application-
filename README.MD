# 🎮 Client-Server Quiz Game (Cloud Server)

A multi-client quiz game built in Python using socket programming and a GUI (Tkinter), where multiple users can connect to a centralized server, enter their names, and participate in a real-time quiz game.

---

## 📁 Project Structure

- `server.py` – Python script to launch the quiz server.
- `client.py` – Python script for the quiz client with a GUI interface.
- `README.md` – Project guide and instructions.
- `project_report.pdf` – Includes output snippets and detailed documentation *(if applicable)*.

---

## 🚀 How to Run the Project

### 🖥️ Server Side

1. Open a terminal or command prompt.
2. Navigate to the folder containing `server.py`.
3. Run the following command:
   ```bash
   python server.py
   ```
4. The server will start listening for incoming client connections on the specified IP address and port.

### 👥 Client Side

1. Open another terminal or command prompt (on the same or another device).
2. Navigate to the folder containing `client.py`.
3. Run the following command:
   ```bash
   python client.py
   ```
4. A GUI window will appear where the user can enter their name and start answering quiz questions.

> 📌 **Note:** Ensure the IP address and port in `client.py` match the server settings.

---

## 📦 Dependencies

This project uses the following Python standard libraries:

- `socket` – For network communication between client and server.
- `json` – For sending and receiving data in structured format.
- `tkinter` – For building the client-side GUI.

> ✅ These libraries are part of Python’s standard library (no additional installation required).

---

## ⚙️ Features

- Supports **multiple client connections** to a central server.
- GUI-based user interface for client interaction using `tkinter`.
- Real-time **quiz gameplay** with user input and feedback.
- **JSON-based communication** for structured and reliable data exchange.
- Error handling to manage disconnections, invalid inputs, and other edge cases.
- Easy customization of quiz questions via the server script.

---

## 📌 Additional Notes

- Ensure both server and client scripts are using the **same IP address and port**.
- For better flexibility, consider configuring IP and port using:
  - Command-line arguments (e.g., `argparse`)
  - Environment variables
  - A separate `config.json` file
- Test on a **local network** or over the internet using proper port forwarding (if applicable).
- Output examples and screenshots are provided in the attached **project report** for reference.

---

## 👨‍💻 Project Contributors

- **Masooma Hassan** 
- **Muhammad Haris** @Perister2904  
- **Muhammad Abdullah**  

---

## 📄 License

This project is intended for academic purposes. You are free to modify and expand it for personal or educational use.
