# Pitney-Bowes-Hackathon
## API

*  **Endpoint:**  
    ```
    /api/bot/  
    ```

*  **Method :** `[POST]`  

*  **Params:**  

    * `Query`

*  **Request:**

  * **POST**

      ```
      {  
          "query": "Your Question",
      }  
      ```

*  **Response:**  

    *   ```
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

*  **cURL:**  
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
