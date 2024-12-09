from flask import Flask, request, jsonify, render_template, send_file
import subprocess
import os

app = Flask(__name__)

# In-memory conversation history
chat_history = []
selected_model = 'falcon'  # Default model

@app.route('/', methods=['GET', 'POST'])
def chat():
    global chat_history, selected_model
    
    if request.method == 'POST':
        user_input = request.form.get('input', '').strip()
        selected_model = request.form.get('model', 'falcon')  # Get selected model
        
        if not user_input:
            error_message = "Error: No input provided!"
            return render_template('index.html', chat_history=chat_history, error_message=error_message, selected_model=selected_model)

        try:
            # Run the query using the Falcon model or another model
            result = subprocess.run(
                ["ollama", "run", selected_model, user_input],
                stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
            )
            
            # Check for errors in the model response
            if result.returncode != 0:
                chat_history.append({
                    "input": user_input,
                    "response": f"Error: {result.stderr}",
                    "error": True
                })
            else:
                chat_history.append({
                    "input": user_input,
                    "response": result.stdout.strip(),
                    "error": False
                })
        except Exception as e:
            chat_history.append({
                "input": user_input,
                "response": f"Error: {str(e)}",
                "error": True
            })
    
    return render_template('index.html', chat_history=chat_history, selected_model=selected_model)


@app.route('/clear', methods=['POST'])
def clear_chat():
    global chat_history
    chat_history = []  # Clear the chat history
    return render_template('index.html', chat_history=chat_history, selected_model=selected_model)


@app.route('/download', methods=['GET'])
def download_chat():
    # Save chat history to a file
    chat_filename = 'chat_history.txt'
    with open(chat_filename, 'w') as file:
        for entry in chat_history:
            file.write(f"You: {entry['input']}\n")
            file.write(f"{selected_model.title()}: {entry['response']}\n\n")
    
    # Send the file for download
    return send_file(chat_filename, as_attachment=True, download_name=chat_filename)


# Main entry point to run the app
if __name__ == '__main__':
    # Ensure static files like CSS are served
    app.run(debug=True)
