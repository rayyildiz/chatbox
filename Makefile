
installer:
	pyinstaller app.py --onefile --windowed --collect-data gradio --collect-data gradio_client --additional-hooks-dir=./hooks --runtime-hook ./runtime_hook.py