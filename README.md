# hacker-ai

A CLI python program that uses the OpenAI API to respond to user's request for assistance like a hacker from an 80s movie.

## Requirements

- Python 3.8 or higher
- Python packages: openai, python-dotenv
- [OpenAI API Key](https://beta.openai.com/)

## Installation

1. Clone the repository

    ```bash
    git clone
    ```

2. Install the dependencies

    ```bash
    pip install -r requirements.txt
    ```

3. Create a .env file in the root directory and add the following:

    ```bash
    OPENAI_API_KEY=your_key_here
    ```

4. Add to bash etc

    ```bash
    alias hack="python '/path/to/hacker.py'"
    ```

5. Run the program

    ```bash
    hack your_request_here>
    ```

## License

[MIT](https://choosealicense.com/licenses/mit/)
