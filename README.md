# ChatBox

![ChatBox](docs/chatbox.png)

A simple desktop application that provides a user-friendly interface for interacting with OpenAI's chat models like GPT-4o.

## Features

- Clean, desktop-native interface for ChatGPT interactions
- Streaming responses for real-time feedback
- Chat history maintained during session
- Configurable OpenAI model selection
- Custom API endpoint support
- Secure API key storage

## Requirements

- Python 3.12 or higher
- OpenAI API key

## Installation

### From Source

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/chatbox.git
   cd chatbox
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

   Or using uv:
   ```
   uv pip install -e .
   ```

3. Run the application:
   ```
   python src/app.py
   ```

### Building a Standalone Executable

You can build a standalone executable using PyInstaller:

```
python installer.py
```

Or using the Makefile:

```
make installer
```

The executable will be created in the `dist` directory.

## Usage

1. Launch the application
2. Enter your OpenAI API key in the designated field
3. Type your message in the input box and press Enter
4. View the AI's response in the chat window

## Configuration

The application can be configured using environment variables:

- `OPENAI_API_KEY`: Your OpenAI API key (can also be entered in the UI)
- `OPENAI_BASE_URL`: Custom API endpoint (default: https://api.openai.com/v1)
- `OPENAI_MODEL`: The model to use (default: gpt-4o-mini)

You can set these variables in a `.env` file in the project root.

## Dependencies

- gradio: For creating the chat interface
- openai: For interacting with OpenAI's API
- pywebview: For creating the desktop window
- environs: For environment variable handling

## Development

To set up the development environment:

```
uv pip install -e ".[dev]"
```

## License

[MIT License](LICENSE)
