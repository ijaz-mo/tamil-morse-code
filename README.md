# Tamil Morse Code

To view detailed mappings of Tamil letters and their corresponding Morse code representations, please refer to the [`morse_tamil_mappings.md`](./morse_tamil_mappings.md) file located within this repository.

This project provides a Flask server and a command-line interface for converting between Tamil text and Morse code.

## Setup

1. Install dependencies:

   ```bash
    python3 -m venv venv
    source venv/bin/activate
    pip3 install -r requirements.txt
  ```

## Client Mode: Use the command-line interface

    ```bash
    # Convert tamil sentence to morse code
    python cli.py "அனைவருக்கும் வணக்கம்"

    ```bash
    # Convert morse code to tamil sentence
    python cli.py -m morse_to_tamil ".- -. .- .. ...- .-. ..- -.-. .... ..- -- .- ..-. .-. ..- ..-. ...- .- -. .- -.-. .... -.-. --- --"
    ```


## Server Mode: Run the Flask server

    ```bash
    python server.py
    ```

**API Endpoints**

- `/tamil_to_morse`: Convert Tamil text to Morse code

  - Method: POST
  - Payload: `{ "tamil_text": "அனைவருக்கும் வணக்கம்" }`
  - Response: `{ "morse_code": "... --- -- . -- --- .-. ... . -.-. --- -.. ." }`

    ```bash
    curl -X POST http://127.0.0.1:5000/tamil_to_morse -H "Content-Type: application/json" -d '{"tamil_text": "அனைவருக்கும் வணக்கம்"}'
    ```

- `/morse_to_tamil`: Convert Morse code to Tamil text

  - Method: POST
  - Payload: `{ "morse_code": "... --- -- . -- --- .-. ... . -.-. --- -.. ." }`
  - Response: `{ "tamil_text": "அனைவருக்கும் வணக்கம்" }`

    ```bash
    curl -X POST http://127.0.0.1:5000/morse_to_tamil -H "Content-Type: application/json" -d '{"morse_code": ".- -. .- .. ...- .-. ..- -.-. .... ..- -- .- ..-. .-. ..- ..-. ...- .- -. .- -.-. .... -.-. --- --"}'
    ```
