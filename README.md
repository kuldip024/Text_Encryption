# Text_Encryption
This project is a straightforward web application that provides functionality for encrypting and decrypting text using Python's cryptography library. The application is built with Flask, a lightweight web framework, and features a simple HTML front-end enhanced with JavaScript and CSS.

# Text Encryption and Decryption Web App

This project is a simple web application that allows users to encrypt and decrypt text using the `cryptography` library in Python. The application is built using Flask and includes a basic HTML front-end with JavaScript and CSS for styling.

- Encrypt text using a secure key.
- Decrypt text using the same key.
- Simple web interface to interact with the encryption and decryption functions.

  ## Requirements
  
- Python 3.x
- Flask
- cryptography

  ## Installation

  1. Clone the repository:
    ```bash
    git clone https://github.com/kuldip024/text-encryption-decryption.git
    cd text-encryption-decryption
    ```

2. Create and activate a virtual environment:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

4. Run the application:
    ```bash
    python app.py
    ```

5. Open your browser and navigate to `http://127.0.0.1:5000/`.


## Project Structure

text-encryption-decryption/
│
├── app.py
├── requirements.txt
├── static/
│ ├── styles.css
│ └── script.js
└── templates/
└── index.html


- `app.py`: The main Flask application file.
- `requirements.txt`: A file listing the Python dependencies.
- `static/`: Directory containing static files (CSS and JS).
- `templates/`: Directory containing HTML templates.

## Usage

1. Navigate to the home page.
2. Enter the text you want to encrypt or decrypt.
3. Click the appropriate button to perform the action.
4. The result will be displayed on the page.

## Security

- The encryption key is generated each time the application is started. For a production environment, you should save the key securely and reuse it for both encryption and decryption.
- Ensure the key is kept safe and not exposed in the code or the repository.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Flask](https://flask.palletsprojects.com/)
- [cryptography](https://cryptography.io/)













