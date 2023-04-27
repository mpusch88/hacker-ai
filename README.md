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

3. Rename the `.env.example` file to `.env` and add your OpenAI API key

    ```bash
    OPENAI_API_KEY=your_api_key_here
    ```

4. (Optional) Add to bash etc.

    Modify .bash_profile (or .bashrc, .zshrc, etc.) to include the following function:

    ```bash
    function hacker() {
        python '/path/to/hacker.py' "$@"
    }
    ```

    Or create an alias:

    ```bash
    alias hacker="python '/path/to/hacker.py'"
    ```

5. Run the program

    ```bash
    hacker <your_request_here>
    ```

    Or, if you did't add the function/alias to your bash profile:

    ```bash
    python /path/to/hacker.py <your_request_here>
    ```

    After a receiving a response, you can enter a new request or type `exit`, `quit`, or `q` to quit.

## License

[MIT](https://choosealicense.com/licenses/mit/)
