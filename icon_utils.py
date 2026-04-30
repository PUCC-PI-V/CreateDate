import ctypes
import os


APP_ID = "ViboraInk.Studio"


def get_icon_path():
    return os.path.join(os.path.dirname(os.path.abspath(__file__)), "icon.ico")


def configure_windows_app_id():
    if os.name != "nt":
        return

    try:
        ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(APP_ID)
    except Exception:
        pass


def _safe_apply_icon(window, icon_path):
    try:
        if window.winfo_exists():
            window.iconbitmap(default=icon_path)
    except Exception:
        pass


def apply_window_icon(window):
    icon_path = get_icon_path()
    if not os.path.exists(icon_path):
        return

    _safe_apply_icon(window, icon_path)
