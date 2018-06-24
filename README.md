# Pitney-Bowes-Hackathon

## About

```
FAQ bot for processing the queries of customers and giving them relevant answers and suggestions based on it.
The FAQs are being fetched and processed by the file FAQs.csv which contains Questions, answers and their class.

Using Flask to deploy an API endpoint which fetches requests using POST method.
The FAQ processing module was initially forked from https://github.com/MrJay10/banking-faq-bot
```
## How to Run

* **Requirements**
```
* Python
* Pip
```

* **Install the prerequisites using pip**
```
pip install -r requirements.txt
```
* **Run the server**
```
python deploy.py
```

## Demo Link
```
https://faqbothackerearth.herokuapp.com/
```

## Theme

*  **E-commerce Enablement**

```
It is really difficult for a small online retailer to manage and streamline his E- commerce store operations.
How can disruptive technology like AI, ML and distributed computing can help these online retailers to streamline operations.

Some key Areas Include :

* Customer Support (Using Freshworks APIs and SDK)
* Returns management
* Order Management
* Marketing
* Hyperlocal Delivery Management
```
## API

*  **Endpoint:**  
    ```
    /api/bot/  
    ```

*  **Method :** `[POST]`  

*  **Params:** `Query`

*  **Request:**

   **POST**

      ```
      {  
          "query": "Your Question",
      }  
      ```

   **Response:**  

      ```  
      {  
          answer: "Answer to the Query."
          ques: "Most Relevznt question for the query" 
          suggest: Object(5)
                   0: "Question Suggestion 1"
                   1: "Question Suggestion 2"
                   2: "Question Suggestion 3"
                   3: "Question Suggestion 4"
                   4: "Question Suggestion 5"
          type: "Class/Category of question"
      }  
      ```

    **cURL:**  
    ```
    curl -X POST http://localhost:5000/api/bot/ -H "Content-Type: application/json" -d '{"query": "Your Question"}'
        
        {  
            answer: "Answer to the Query."
            ques: "Most Relevznt question for the query" 
            suggest: Object(5)
                    0: "Question Suggestion 1"
                    1: "Question Suggestion 2"
                    2: "Question Suggestion 3"
                    3: "Question Suggestion 4"
                    4: "Question Suggestion 5"
            type: "Class/Category of question"
        }  
    ```
