import gradio as gr
from openai import Client


async def get_openai_client(api_key) -> Client | None:
    try:
        client = Client(api_key=api_key, base_url="https://api.openai.com/v1")
        return client
    except Exception as e:
        print(e)
    return None


async def chat(prompt, history, api_key):
    if not history:
        history = [{"role": "system", "content": "You are a friendly chatbot, help me answer questions."}]
    history.append({"role": "user", "content": prompt})

    yield history

    client = await get_openai_client(api_key)
    response = {"role": "assistant", "content": ""}
    for message in client.chat.completions.create(
            messages=history,
            temperature=1.0,
            top_p=0.9,
            max_tokens=512,
            stream=True,
            model="gpt-4o-mini"
    ):
        response["content"] += message.choices[0].delta.content or ""
        yield history + [response]


with gr.Blocks(css="footer {visibility: hidden}") as demo:
    api_key = gr.Textbox(label="API Key", placeholder="Enter your openai api key...", type="password")
    chatbot = gr.Chatbot(label="Chatbot", type="messages")
    prompt = gr.Textbox(label="Message", placeholder="Enter your message...", max_lines=1)
    prompt.submit(chat, inputs=[prompt, chatbot, api_key], outputs=[chatbot])
    prompt.submit(lambda: "", None, [prompt])

if __name__ == "__main__":
    demo.launch()
