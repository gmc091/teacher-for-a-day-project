# Import necessary modules
import tkinter as tk  # Used to create GUI
from tkinter import ttk
from tkinter import font
import openai  # Used to access the OpenAI API
import pyttsx3  # Used to convert text to speech
import speech_recognition as sr  # Used for speech recognition
import language_tool_python  # Used for grammar and spelling correction (Not used in this example)
import threading  # Used to run multiple threads
import queue  # Used for thread-safe queue operations
import webbrowser

# Set the assistant's name
ASSISTANT_NAME = "jarvis"
is_talking = False

# Read API key from file
with open("openai_api_key.txt", "r") as file:
    api_key = file.read().strip()

# Check if API key is set
if not api_key:
    raise ValueError("OpenAI API key is not properly set.")

# Set OpenAI API key
openai.api_key = api_key

# Initialize the LanguageTool
tool = language_tool_python.LanguageTool("en-US")

# Variables to control the assistant
is_assistant_active = False  # To check if the assistant is active
conversation_history = [
    {
        "role": "system",
        "content": "You are an helpful AI assistant made by Giovanni Croese for an english school project called 'Theacher for a day' your default name is Jarvis, you love breaking bad, better call saul and star wars.",
    },
    {
        "role": "user",
        "content": "Remember that when I say 'Hello there' you have to answer with 'General Kenobi', when I say 'say my name', you should reply with 'You're Heisenberg' and when I say 'You're god damn right' tell me something about breaking bad, and if I say that I need a lawyer you have to tell me 'Better call saul!",
    },
    {
        "role": "assistant",
        "content": "Of course, when you say 'Hello there' I will answer with 'Generalk Kenobi', when you say 'say my name', I'll respond with 'You're Heisenberg' and when you'll say 'You're god damn right' I'll tell you something about breaking bad starting with the sentence 'I see you like breaking bad', and if you say that you need a lawyer I'm going to just tell you the only sentence: 'Better call saul!",
    },
]


# Initialize the text-to-\ engine
engine = pyttsx3.init()
engine.setProperty(
    "voice",
    "HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_EN-US_ZIRA_11.0",
)

speak_queue = queue.Queue()  # Create a queue to hold text to be spoken

for voice in engine.getProperty("voices"):
    print(voice)


# Function to speak the text in the queue
def speak_text():
    global is_talking
    while True:
        text = speak_queue.get()  # Get text from queue
        if text is None:  # Break loop if text is None
            break
        is_talking = True
        engine.say(text)  # Convert text to speech
        engine.runAndWait()  # Wait until speech is complete
        is_talking = False


# Start a new thread that will handle speaking text
speak_thread = threading.Thread(target=speak_text, daemon=True)
speak_thread.start()

# Create a tkinter window
window = tk.Tk()
window.title("AI Assistant")

# Create a label to display the assistant's name and status
assistant_label = tk.Label(
    window, text="My name is: " + ASSISTANT_NAME, font=("Arial", 30)
)
assistant_label.pack(pady=20)

status_label = tk.Label(window, text="🤖", font=("Arial", 150))
status_label.pack(pady=50)


# Function to update the status of the assistant
def update_status():
    if is_assistant_active:
        status_label.config(fg="green")
    else:
        status_label.config(fg="red")
    window.update_idletasks()


update_status()


# Function to run when the window is closing
def on_close():
    global is_assistant_active
    is_assistant_active = False
    window.destroy()


window.protocol("WM_DELETE_WINDOW", on_close)  # Set the function to run on window close


# Add a "Stop" button
def stop_assistant():
    global is_assistant_active
    is_assistant_active = False
    update_status()
    if engine is not None:
        engine.stop()


# Create a new style
style = ttk.Style()

# Set the font
my_font = font.Font(family="Helvetica", size=18, weight="bold")

# Configure the style
style.configure(
    "TButton", background="red", foreground="red", font=my_font, borderwidth=0
)

# Change the padding
style.configure("TButton", padding=(0, 5, 0, 5))

# Change the label color when the button is under the cursor
style.map(
    "TButton", background=[("active", "dark red")], foreground=[("active", "red")]
)

stop_button = ttk.Button(window, text="Stop", style="TButton", command=stop_assistant)
stop_button.pack(pady=10)


# Function to process speech input
def process_speech_input():
    global is_assistant_active
    global ASSISTANT_NAME
    global conversation_history
    global is_talking
    recognizer = sr.Recognizer()  # Initialize the speech recognizer
    print("Started processing speech input")

    while True:
        try:
            with sr.Microphone() as source:
                audio = recognizer.listen(source)  # Listen for speech

            text = recognizer.recognize_google(
                audio, language="en-EN"
            ).lower()  # Recognize speech and convert to lowercase
            print(f"Corrected text: {text}")

            # Check if the assistant's name is in the text
            if ASSISTANT_NAME in text.lower():
                if not is_assistant_active:  # If the assistant is not active
                    is_assistant_active = True  # Activate the assistant
                    print("Assistant ready to answer.")
                    update_status()  # Update the assistant's status color
                    speak_queue.put("Yes?")  # Speak "Yes?"
                    continue

            # Check if "stop" is in the text
            if "stop" in text.lower():
                if is_assistant_active:  # If the assistant is active
                    is_assistant_active = False  # Deactivate the assistant
                    print("Assistant deactivated.")
                    speak_queue.put("Goodbye,")  # Speak "Goodbye,"
                    update_status()  # Update the assistant's status color
                    continue
                if engine is not None:
                    engine.stop()

            # If user wants to change the assistant's name
            if "change your name to" in text.lower():
                new_name = text.split("change your name to")[-1].strip()
                ASSISTANT_NAME = new_name
                assistant_label.config(text=ASSISTANT_NAME)
                speak_queue.put(f"My name has been changed to {new_name}.")
                continue

            if "play a song" in text.lower():
                webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")
                continue

            # If the assistant is active
            if is_assistant_active:
                # Add the user's text to the conversation history
                conversation_history.append(
                    {"role": "user", "content": text.split(ASSISTANT_NAME)[-1].strip()}
                )
                # Get a response from GPT-3
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=conversation_history,
                )

                # Get the assistant's reply from the response
                reply = response.choices[0].message["content"].strip()
                print(f"GPT3 responded: {reply}")
                # Add the assistant's reply to the conversation history
                conversation_history.append({"role": "assistant", "content": reply})

                # Add the assistant's reply to the speech queue
                speak_queue.put(reply)

        except sr.UnknownValueError:
            if not is_talking:
                print("Speech recognition could not understand audio")
        except sr.RequestError as e:
            print(f"Could not request results from speech recognition service; {e}")
        except Exception as e:
            print(f"An error occurred: {e}")


# If this script is run directly
if "__main__" == __name__:
    # Start a new thread to process speech input
    threading.Thread(target=process_speech_input, daemon=True).start()
    # Start the tkinter main loop
    window.mainloop()
