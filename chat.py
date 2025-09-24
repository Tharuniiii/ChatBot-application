import streamlit as st
from nltk.chat.util import Chat, reflections

# Chatbot pairs
pairs = [
    [r"(.*)my name is (.*)", ["Hello %2, How are you today?",]],
    [r"(.*)help(.*)", ["I can help you",]],
    [r"(.*) your name ?", ["My name is thecleverprogrammer, but you can just call me robot and I'm a chatbot.",]],
    [r"how are you (.*) ?", ["I'm doing very well", "I am great!"]],
    [r"sorry (.*)", ["It's alright", "It's OK, never mind that",]],
    [r"i'm (.*) (good|well|okay|ok)", ["Nice to hear that", "Alright, great!",]],
    [r"(hi|hey|hello|hola|holla)(.*)", ["Hello", "Hey there",]],
    [r"what (.*) want ?", ["Make me an offer I can't refuse",]],
    [r"(.*)created(.*)", ["Prakash created me using Python's NLTK library", "Top secret ;)",]],
    [r"(.*) (location|city) ?", ['Hyderabad, India',]],
    [r"(.*)raining in (.*)", ["No rain in the past 4 days here in %2", "In %2 there is a 50% chance of rain",]],
    [r"how (.*) health (.*)", ["Health is very important, but I am a computer, so I don't need to worry about my health",]],
    [r"(.*)(sports|game|sport)(.*)", ["I'm a very big fan of Cricket",]],
    [r"who (.*) (Cricketer|Batsman)?", ["Virat Kohli"]],
    [r"quit", ["Bye for now. See you soon :)", "It was nice talking to you. See you soon :)"]],
    [r"(.*)", ['Our customer service will reach you']]
]

# Initialize chatbot
chat = Chat(pairs, reflections)

# Initialize session state
if "history" not in st.session_state:
    st.session_state.history = []

# CSS for chat bubbles
st.markdown("""
<style>
.user {
    background-color: #1f1f1f;
    color: white;
    padding: 10px 15px;
    border-radius: 15px;
    text-align: left;
    margin-bottom: 5px;
    width: fit-content;
    max-width: 70%;
}
.bot {
    background-color: #333333;
    color: white;
    padding: 10px 15px;
    border-radius: 15px;
    text-align: left;
    margin-bottom: 5px;
    width: fit-content;
    max-width: 70%;
}
.container {
    display: flex;
    flex-direction: column;
}
.user-container {
    display: flex;
    justify-content: flex-end;
}
.bot-container {
    display: flex;
    justify-content: flex-start;
}
</style>
""", unsafe_allow_html=True)

st.title("Simple Chatbot")
st.write("Hi! I am a bot 🤖. I can assist you. Please write in lower case to start the conversation.")

# Input form
with st.form(key='chat_form', clear_on_submit=True):
    user_input = st.text_input("You:")
    submit_button = st.form_submit_button(label='Send')

if submit_button and user_input:
    response = chat.respond(user_input)
    st.session_state.history.append(("You", user_input))
    st.session_state.history.append(("Bot", response))

# Display conversation history as chat bubbles
for sender, message in st.session_state.history:
    if sender == "You":
        st.markdown(f'<div class="container user-container"><div class="user">{message}</div></div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="container bot-container"><div class="bot">{message}</div></div>', unsafe_allow_html=True)
