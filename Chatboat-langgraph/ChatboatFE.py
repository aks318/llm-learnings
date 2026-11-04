from dotenv import load_dotenv

import streamlit as st
from ChatboatBE import chatbot, retrieve_all_thread_func
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
import uuid

load_dotenv()

# === utility fubnction===========

def generate_thread_id():
    return uuid.uuid4()

def reset_chat():
    thread_id = generate_thread_id()
    st.session_state["thread_id"] = thread_id
    st.session_state["message_history"] = []
    add_thread(thread_id)

def add_thread(thread_id):
    if thread_id not in st.session_state["chat_threads"]:
        st.session_state["chat_threads"].append(thread_id)

def load_chat(thread_id):
    CONFIG = {'configurable': {'thread_id': thread_id}}
    st.session_state["thread_id"] = thread_id
    messages = chatbot.get_state(config=CONFIG).values.get('messages', [])
    
    temp_message = []

    for message in messages:
        if isinstance(message, HumanMessage):
            role = "user"
        else:
            role = "assistant"
        temp_message.append({"role": role, 'content': message.content})
    st.session_state["message_history"] = temp_message


# Session State==========================

if 'message_history' not in st.session_state:
    st.session_state['message_history'] = []

if "thread_id" not in st.session_state:
    st.session_state["thread_id"] = generate_thread_id()

if 'chat_threads' not in st.session_state:
    st.session_state['chat_threads'] = retrieve_all_thread_func()

add_thread(st.session_state["thread_id"])

# Sidebar ======================================================

st.sidebar.title("Langgraph Chatbot")
if st.sidebar.button("New Chat"):
    reset_chat()
st.sidebar.header("My converstation")

for thread_id in st.session_state["chat_threads"][::-1]:
    if st.sidebar.button(str(thread_id)):
        load_chat(thread_id)

# loading the conversation history
for message in st.session_state['message_history']:
    with st.chat_message(message['role']):
        st.text(message['content'])

CONFIG = {
    'configurable': {'thread_id': st.session_state['thread_id']},
    'metadata':  {'thread_id': st.session_state['thread_id']},
    'run_name': 'chat_run'
    }

user_input = st.chat_input('Type here')

if user_input:
    # Show user's message
    st.session_state["message_history"].append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.text(user_input)

    CONFIG = {
        "configurable": {"thread_id": st.session_state["thread_id"]},
        "metadata": {"thread_id": st.session_state["thread_id"]},
        "run_name": "chat_turn",
    }

    # Assistant streaming block
    with st.chat_message("assistant"):
        # Use a mutable holder so the generator can set/modify it
        status_holder = {"box": None}

        def ai_only_stream():
            for message_chunk, metadata in chatbot.stream(
                {"messages": [HumanMessage(content=user_input)]},
                config=CONFIG,
                stream_mode="messages",
            ):
                # Lazily create & update the SAME status container when any tool runs
                if isinstance(message_chunk, ToolMessage):
                    tool_name = getattr(message_chunk, "name", "tool")
                    if status_holder["box"] is None:
                        status_holder["box"] = st.status(
                            f"🔧 Using `{tool_name}` …", expanded=True
                        )
                    else:
                        status_holder["box"].update(
                            label=f"🔧 Using `{tool_name}` …",
                            state="running",
                            expanded=True,
                        )

                # Stream ONLY assistant tokens
                if isinstance(message_chunk, AIMessage):
                    yield message_chunk.content

        ai_message = st.write_stream(ai_only_stream())

        # Finalize only if a tool was actually used
        if status_holder["box"] is not None:
            status_holder["box"].update(
                label="✅ Tool finished", state="complete", expanded=False
            )

    # Save assistant message
    st.session_state["message_history"].append(
        {"role": "assistant", "content": ai_message}
    )