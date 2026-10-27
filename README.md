##### **Build a Simple API Client**

###### 

###### **Project Description**

This project is a simple Python API client that connects to a public REST API, retrieves JSON data, and displays selected information in a clean and readable format. It also includes error handling to manage connection problems, HTTP errors, timeouts, and invalid user input.

###### 

###### **Objective**

To understand basic API consumption, HTTP requests, and JSON response handling using Python.



###### **Technologies Used**

\- Python

\- Requests library

\- JSON Place holder Public REST API



###### **Features**

\- Fetches post details from a public API.

\- Processes JSON responses.

\- Displays post ID, user ID, title, and content.

\- Validates user input.

\- Handles HTTP errors and connection failures.

\- Uses a timeout to prevent requests from waiting indefinitely.



###### **Requirements**

\- Python 3.x

\- Requests library



###### **Installation**

Install the required library using: pip install requests

###### 

###### **How to Run**

1\. Download or clone this repository.

2\. Save the Python program as `api\_client.py`.

3\. Open a terminal in the project folder.

4\. Run the following command: python api\_client.py

5\. Enter a post ID between 1 and 100 to view the API response.



###### **API Used**

JSON Place holder: https://jsonplaceholder.typicode.com/posts/1



This public API provides sample post data for testing and learning purposes.



###### **Sample Output**

Welcome to the Simple API Client!

Enter a post ID (1-100): 1



========================================

&#x20;          API RESPONSE

========================================

Post ID : 1

User ID : 1

Title   : Sunt Aut Facere Repellat Provident

Content : Sample post content retrieved

&#x20;         from the API

========================================





**Note**: The actual title and content are retrieved from the API and may differ from this example.\*



###### **Learning Outcomes**

\- Learned how to send HTTP GET requests using Python.

\- Understood how to retrieve and process JSON data.

\- Practiced input validation and exception handling.

\- Learned how to check HTTP status codes.

\- Gained practical experience working with a public REST API.

###### 

###### **Conclusion**

This project demonstrates how Python can communicate with a REST API and process the returned data. It provides a foundation for developing more advanced API-based applications.



