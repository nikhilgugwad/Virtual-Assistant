# Voice-Activated Assistant (Jarvis)

## Description
This is a simple voice-activated personal assistant inspired by Jarvis. It can perform tasks such as:
- Opening applications like Notepad and Command Prompt  
- Fetching news and IP address  
- Searching Wikipedia  
- Telling jokes  
- Browsing the web (Google, YouTube)  
- Switching off on command  

The assistant uses `pyttsx3` for text-to-speech, `speech_recognition` for voice input, and several other libraries to provide functionalities.

## Folder Structure
```
weather-monitoring-project/
│
├── src/
│   └── main.py      # Main code for the voice assistant
└── README.md        # Documentation (this file)
```

## Prerequisites
Make sure you have the following installed:
- **Python 3.11.9**: Download from [Python's official site](https://www.python.org/downloads/)
- **Git** (optional, for version control)

You will also need the following Python packages:
```bash
pip install pyttsx3 speechrecognition opencv-python-headless wikipedia webbrowser pyjokes requests
```

## How to Run
1. Clone the repository (optional):
   ```bash
   git clone https://github.com/nikhilgugwad/Virtual-Assistant.git
   cd <Your project folder>
   ```

2. Navigate to the `src/` folder:
   ```bash
   cd src
   ```

3. Run the `main.py` file:
   ```bash
   python main.py
   ```

4. The assistant will greet you and start taking voice commands.

## Features
- **Voice Interaction:** Use your voice to give commands.
- **Application Control:** Open and close Notepad, Command Prompt, and Camera.
- **News Updates:** Fetch the latest news headlines.
- **IP Address:** Get your device's IP address.
- **Wikipedia Search:** Retrieve summaries from Wikipedia.
- **Web Search:** Browse Google and YouTube with voice input.
- **Jokes:** Brighten your day with a joke.
- **Graceful Shutdown:** Say "switch off" to exit the assistant.

## Example Commands
- "Open Notepad"  
- "Close Notepad"  
- "Open Command Prompt"  
- "Open Camera"  
- "IP Address"  
- "Search Wikipedia for Albert Einstein"  
- "Open YouTube"  
- "Search Google for weather today"  
- "Tell me a joke"  
- "News"
- "Switch off"

## Technologies Used
- **Python**: Programming language
- **Pyttsx3**: Text-to-speech conversion
- **SpeechRecognition**: Voice input recognition
- **OpenCV**: Camera handling
- **Wikipedia API**: Wikipedia search
- **Pyjokes**: Joke generation
- **Requests**: API requests for news and IP address

## Troubleshooting
1. **Microphone not detected**:  
   - Ensure your microphone is connected and enabled in system settings.
   - Run as administrator if permission issues occur.

2. **Speech recognition errors**:  
   - Check your internet connection (Google’s API requires internet).
   - Ensure the microphone volume is adequate.

3. **Missing modules**:  
   - Make sure all dependencies are installed with:
     ```bash
     pip install -r requirements.txt
     ```

4. **News API key error**:  
   - Replace the API key in the `news()` function with your own from [NewsAPI](https://newsapi.org/).

## Future Improvements
- Add support for more voice commands.
- Integrate reminders and alarms.
- Use machine learning for personalized responses.
- Improve error handling and robustness.