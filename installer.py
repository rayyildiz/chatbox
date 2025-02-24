import PyInstaller.__main__


PyInstaller.__main__.run(
    [
        "app.py",
        "--onefile",
        "--windowed",
        "--icon=./app_icon.ico",
        "--add-data=./app_icon.ico:.",
        "--collect-data=gradio",
        "--collect-data=gradio_client",
        "--additional-hooks-dir=./hooks",
        "--runtime-hook=./runtime_hook.py",
    ]
)
