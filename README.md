# Falcon Coder Chat UI

## Overview
This is a Flask-based web application that provides a simple UI to interact with the Falcon language model. Users can enter queries, receive responses, and download their chat history.

## Features
- **Interact with Falcon Model**: Send text queries and get responses.
- **Clear Chat History**: Clear your chat anytime during the session.
- **Download Chat History**: Download your entire chat as a `.txt` file.
- **Multiple Model Support**: Switch between models easily (e.g., Falcon, Another Model).
- **Beautiful User Interface**: Fully styled UI with responsive design and smooth interactions.

## Installation

### Prerequisites
- Python 3.9 or higher
- pip (Python package installer)
- **Ollama** library (to interact with the LLM models)

## Installation

### 1. Install Ollama

Follow this [guide](https://dev.to/bradstondev/unlock-the-power-of-meta-llama-llm-easy-guide-to-hosting-in-your-local-dev-environment-7d) to install **Ollama**. This guide will walk you through the process of installing Ollama and setting it up in your local development environment.

Once Ollama is installed, you can use it to interact with various LLM models, such as **Falcon**.

### 2. Install the Falcon Model

After installing Ollama, you need to install the **Falcon** model (or any other model you prefer). To install Falcon, run the following command:

```bash
ollama run falcon
```

### Steps to Run Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/yourusername/falcon-coder-chat-ui.git
   cd falcon-coder-chat-ui
   ```

2. **Install the required dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Flask app**:
   ```bash
    python app.py
   ```

4. Open your browser and go to `http://127.0.0.1:5000/`.

## Usage

1. **Select a Model**: Choose between Falcon or other models from the dropdown menu.
2. **Input a Query**: Type your query into the input box and click "Submit".
3. **Clear History**: Press "Clear Chat" to erase the conversation.
4. **Download History**: Click "Download Chat" to save your chat history as a `.txt` file.

## License
This project is open-source and available under the MIT License.
