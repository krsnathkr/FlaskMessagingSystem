# Building a Simple Distributed System

Project Description: In this project, I have designed and implemented a simple distributed system in Python. The distributed system includes the following components:

- Server Clustering: Multiple server instances running on different ports.
- Client Registration: Clients can register with a specific server instance.
- Data Sharing: Clients can share data with each other through the server.
- Fault Tolerance: The system should handle server failures gracefully.


## 1. Server Setup:

Creating multiple server instances each listening on a different port (8080,8081,8082) 

In the terminal, run python server8080.py 
- Server running on port 8080:

  ![image](https://github.com/krsnathkr/FlaskMessagingSystem/assets/66662960/eacea52e-46f5-48e7-a5e2-85b4c64e3043)

- Server running on port 8081:

  ![image](https://github.com/krsnathkr/FlaskMessagingSystem/assets/66662960/d6ef2b05-1607-4514-9cbe-b1194f7eec27)

- Server running on port 8082:

  ![image](https://github.com/krsnathkr/FlaskMessagingSystem/assets/66662960/dc605d6e-80cd-483c-ba8c-fa73cdfc44af)


## 2. Client Registration:

Here are are creating 6 different clients, 2 on each port.

- Client 1 & 2 on port 8080:

  ![image](https://github.com/krsnathkr/FlaskMessagingSystem/assets/66662960/f186f428-7ea3-4450-aa30-3f9c2b7ca9f9)

- Client 3 & 4 on port 8081:

  ![image](https://github.com/krsnathkr/FlaskMessagingSystem/assets/66662960/b87b51e3-2c9e-4f43-80f4-1863e8e7d10f)

- Client 5 & 6 on port 8082:

  ![image](https://github.com/krsnathkr/FlaskMessagingSystem/assets/66662960/f058050b-b8b1-477a-9f18-f1db224b1070)

Now I am adding screenshots of the ports showing the registration on the clients.

- Port 8080:
  ![image](https://github.com/krsnathkr/FlaskMessagingSystem/assets/66662960/87e45a8f-8a80-4d1e-bd2f-3b2cecb6d774)

- Port 8081:
  ![image](https://github.com/krsnathkr/FlaskMessagingSystem/assets/66662960/16a2774c-7a54-4207-bef4-95a4017bcc8d)

- Port 8082:
  ![image](https://github.com/krsnathkr/FlaskMessagingSystem/assets/66662960/9e727bac-da96-435d-8bfe-58e5a1fb1354)


## 3. Data Sharing:

- Here, I sent message from user 1 to user 2 on port 8080:
  
  ![image](https://github.com/krsnathkr/FlaskMessagingSystem/assets/66662960/83fe60ae-922e-4832-81fd-4174981f6e61)

  We can confirm that it was transmitted through port 8080 because we can see the share function running in the port:

  ![image](https://github.com/krsnathkr/FlaskMessagingSystem/assets/66662960/c03eb067-a325-4539-bb83-78e0efb159fc)

  
- Here, I sent message from user 3 to user 4 on port 8081:
  
  ![image](https://github.com/krsnathkr/FlaskMessagingSystem/assets/66662960/d809e286-b1e8-4265-a3c7-f7843700542e)
  
  And we can see the port 8081 here:

  ![image](https://github.com/krsnathkr/FlaskMessagingSystem/assets/66662960/25b48775-d2f0-4520-85c3-be7a189ad26b)

- Here I sent message from user 5 to user 6 on port 8082:

  ![image](https://github.com/krsnathkr/FlaskMessagingSystem/assets/66662960/39d5b2ad-67ee-4cf4-bf83-eb21178bcc92)

  And this is port 8082:

  ![image](https://github.com/krsnathkr/FlaskMessagingSystem/assets/66662960/40525150-7274-4e5c-9db9-6e00cc9bbf13)


This also shows that we can run multiple server instances running on different ports simultaneously.



  




