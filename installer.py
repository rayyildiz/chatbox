import PyInstaller.__main__


PyInstaller.__main__.run(
    [
        "./src/app.py",
        "--onefile",
        "--windowed",
        "--clean",
        "--noconfirm",
        "--name=chatbox",
        "--icon=./app_icon.ico",
        "--add-data=./app_icon.ico:.",
        "--collect-data=gradio",
        "--collect-data=gradio_client",
        "--additional-hooks-dir=./src/hooks",
        "--runtime-hook=./src/runtime_hook.py",
        # "--exclude-module=cffi",
        "--exclude-module=.git"
    ]
)
