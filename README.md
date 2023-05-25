# Voice-Activated AI Assistant

This repository contains the code for a voice-activated AI assistant written in Python. The assistant utilizes various technologies and libraries to enable natural language understanding and interaction.

## Overview

The voice-activated AI assistant allows users to interact with a computer system using voice commands. It leverages speech recognition, natural language processing, and text-to-speech conversion to understand user input, generate appropriate responses, and provide a conversational experience.

## Features

- Speech recognition: The assistant listens to user commands through the microphone and converts them into text.
- Natural language understanding: User commands are processed and interpreted to extract intent and context.
- OpenAI integration: The assistant communicates with OpenAI's GPT-3 model to generate human-like responses.
- Text-to-speech conversion: Responses from the assistant are converted into spoken words using pyttsx3 library.
- Graphical user interface (GUI): The assistant's interface is built using Tkinter, providing a user-friendly interaction experience.
- Microphone feedback control: The assistant includes a 'mute' function to prevent picking up its own voice during speech output.

## Setup

To set up the virtual environment and install dependencies, follow these steps:

1. Install the `virtualenv` package by running the following command: pip install virtualenv


2. Create and activate the virtual environment:
- **Windows**:
  ```
  python -m venv myenv
  myenv\Scripts\activate
  ```
- **Linux/macOS**:
  ```
  python -m venv myenv
  source myenv/bin/activate
  ```

3. Install the required packages: pip install ttkthemes openai pyttsx3 SpeechRecognition webbrowser logging PyAudio

 
## Usage

To run the AI assistant, follow these steps:

1. Activate the virtual environment:
- **Windows**: `myenv\Scripts\activate`
- **Linux/macOS**: `source myenv/bin/activate`

2. Execute the main Python file to start the assistant.

3. Speak commands into the microphone and wait for the assistant's responses.

## Customization

You can customize the AI assistant to suit your specific needs. Consider exploring the following possibilities:

- Modifying the conversation history: Adjust the predefined system, user, and assistant messages to change the assistant's behavior and personality.
- Enhancing the user interface: Customize the GUI elements, colors, and layout to create a unique visual experience.
- Extending functionality: Add new features such as voice-activated actions, integration with external services, or additional language support.

Feel free to dive into the code, experiment, and contribute to the project's improvement!

## Contributions

Contributions to this project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request. Let's collaborate to enhance the functionality and capabilities of the voice-activated AI assistant.

## License

This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and distribute the code for personal or commercial purposes.

## Acknowledgements

This project was inspired by the growing field of conversational AI and the advancements made by OpenAI's GPT-3 model. We extend our gratitude to the open-source community for developing and maintaining the libraries and tools used in this project.

## Conclusion

Voice-activated AI assistants are transforming the way we interact with technology. By understanding the underlying concepts and building a basic assistant, you can embark on a journey to explore the possibilities of conversational AI. Let's continue pushing the boundaries of AI technology together!

Happy coding!
