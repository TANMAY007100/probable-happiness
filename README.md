# Postman Chat

**A simple chat application server for developers to communicate using Postman everyone's favourite  API client.**<br/><br/>

The new release of [Postman](https://www.postman.com/) v8.5.0 brought using **WebSockets (Beta)** inside it's web and desktop application. You can read the [blog](https://blog.postman.com/postman-supports-websocket-apis) or find all other related announcements in [release notes](https://www.postman.com/downloads/release-notes/).
<br/><br/>
## The Purpose:

Nonetheless, I thought of trying my hands-on, while giving a try to FastAPI with WebSockets.
<br/><br/>
## The Features:
* Real-time communication between two users.
* Simple 1-on-1 chat.
<br/><br/>
## Requirements

Programming Language: Python v3.6 or above<br/>
OS: Any<br/>
API Client: Postman (used as a UI)
<br/><br/>
## Python Packages

FastAPI
Uvicorn (ASGI Server)

**Note: You can other ASGI Server for e.g. Daphne, however this was originally tested with uvicorn**
<br/><br/>
## How to run:

### **Step 0:** Download and Install the latest version of Postman if you haven't downloaded yet. It be will be required for the User Interface.

### **Step 1:** Clone the repository and cd into the cloned directory:<br/>
`git clone <repo_url>`<br/>
`cd <repo_directory>`

### **Step 2:** Create a virtual environment:<br/>
`python -m venv venv`

### **Step 3:** Activate the virtual environment:<br/>
`venv\Scripts\activate` (Windows)<br/>
`source venv\bin\activate` (Linux)

### **Step 4:** Install all the package dependencies from the requirements.txt file:<br/>
`pip install -r requirements.txt`

### **Step 5:** Run the server using following command:<br/>
`uvicorn main:app --reload`

### **Step 6:** Open Postman (latest version required)

### **Step 7:** Create New WebSocket request

### **Step 8:** Enter URL in following format

`ws://<host>:<port>/ws/<your_username>`

For e.g. `ws://localhost:8000/ws/john`

Note: Username is not case sensitive. `/ws/john` and `/ws/John` are same.

Click **Connect** at far right corner

### **Step 9:** Now, create another New WebSocket request

### **Step 10:** Enter URL in following format (the person you wish to chat with will enter this URL)

`ws://<host>:<port>/ws/<username>`

For e.g. `ws://localhost:8000/ws/mike`

Click **Connect** at far right corner

### **Step 11:** To send message

Change the **Text** dropdown to **JSON**. Dropdown just below Message box.

Enter your message in the Compose input box provided.

```json
{
    "p": "<partner_username>",
    "m": "<message>"
}
```

For e.g.

```json
{
    "p": "mike",
    "m": "Hello World"
}
```

**Note:**
1. Above will send **Hello World** to a socket identified by username **mike**
2. Any other format will result in message being discarded.
3. You will receive all messages in the Window with your Username.
4. Defaults
   * host: **localhost**
   * port: **8000**