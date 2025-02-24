import webview

from gradio_app import demo as gradio_app

gradio_app.launch(prevent_thread_lock=True)


def on_closing():
    gradio_app.close()


app = webview.create_window("ChatBox", gradio_app.local_url, width=800, height=740, resizable=False)
# app.events.shown += lambda: gradio_app.launch(prevent_thread_lock=True)
app.events.closed += on_closing
webview.start()
