import PyInstaller.hooks.rthooks.pyi_rth_multiprocessing  # noqa: F401

if __name__ == "__main__":
    # This is necessary to prevent an infinite app launch loop.
    import multiprocessing

    multiprocessing.freeze_support()
