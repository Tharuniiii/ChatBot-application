# ChatBot-application
A simple rule-based chatbot built using Python, NLTK, and Streamlit. The chatbot responds to user inputs using predefined patterns and reflections, and the conversation is displayed as interactive chat bubbles in a Streamlit app.

# Features

Rule-based chatbot using NLTK’s Chat module.

Interactive chat interface built with Streamlit.

Chat bubbles UI for user and bot messages.

Maintains conversation history during the session.

Simple predefined responses for greetings, help, weather, and more.

Installation

Clone the repository:
```
git clone https://github.com/your-username/simple-chatbot.git
cd simple-chatbot
```
Install dependencies:
```pip install streamlit nltk```
Download NLTK data:
```
import nltk
nltk.download('punkt')
```
# Usage

Type your messages in the input box.

Chatbot responds based on the predefined patterns.

Use “quit” to end the conversation.

Example inputs:

“hi” → Bot responds “Hello”

“my name is Tharuni” → Bot responds “Hello Tharuni, How are you today?”

“raining in Hyderabad” → Bot responds with weather info.
