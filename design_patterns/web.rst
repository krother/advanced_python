
API Programming
===============

Exercise 1: Run FastAPI
-----------------------

Install FastAPI with:

::

   pip install fastapi uvicorn pytest httpx

Then create a file `app.py` with a hello-world example:

.. code:: python3

   from fastapi import FastAPI
   
   app = FastAPI()
   
   
   @app.get("/")
   def read_root():
       return {"Hello": "World"}
   
   
   @app.get("/items/{item_id}")
   def read_item(item_id: int, q: str|None = None):
       return {"item_id": item_id, "q": q}
    
Run the server from the comman line with:

::

   uvicorn --reload app:app

In the browser, visit any of:

- `http://localhost:8000/ <http://localhost:8000/>`__
- `http://localhost:8000/docs <http://localhost:8000/docs>`__


.. seealso::

   `FastAPI documentation <https://fastapi.tiangolo.com/>`__

Exercise 2: Pydantic models
---------------------------

Implement a **word counter API** that counts the words in an input sentence.
It should receive the sentence as a string and return a list of words and the word count
(both as JSON documents).

Define an input and output model with pydantic.
Then use the following signature for the endpoint:

.. code:: python3

   def word_counter(request: WordCountRequest) -> WordCountResponse:
       ...

Run the app, make sure it works. Also check what happens if you use wrong input.

Exercise 3: Test Client
-----------------------

Implement a test for the word counter app. Use the following starter code:

.. code:: python3

    from fastapi.testclient import TestClient

    client = TestClient(app)

    def test_read_main():
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"msg": "Hello World"}

Run the tests with pytest.

Exercise 4: Requests
--------------------

Write a standalone program that uses the `httpx <https://www.python-httpx.org/>`__  library to send requests to your web server. 

Exercise 5: Async
-----------------

Make the response slower by using `asyncio.sleep(5)`. 
Then define the endpoints as  `async` functions as well.

Make the httpx client send multiple requests and see if they are returned any faster than the absolute wainting time.


Exercise 6: Lazy Loading
------------------------

Write the client in such a way that it sends out 10 requests.

As soon as 5 of them have completed, it should output a result.

Exercise 7: Security
--------------------

Run the example in :download:`app_security.py` .

Refactor the code.

Exercise 8: Dungeon Game
------------------------

Implement a REST API interface for the Dungeon Game.
Check how fast it is.

