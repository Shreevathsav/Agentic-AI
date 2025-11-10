from ollama import chat, ChatResponse
import textwrap

messages = [
    {
        'role': 'user',
        'content': '"you got lottery click the below link to claim your prize" classify this message as spam or not spam. Also tell in one line why did you think so',
    },
]

response: ChatResponse = chat(model='deepseek-r1:1.5b', messages=messages)

# Access the message content correctly
text_output = response.message.content

print(textwrap.dedent(text_output))