from screeninfo import get_monitors

def center_window(root, width=800, height=600):
    monitor = get_monitors()[0]

    screen_width = monitor.width
    screen_height = monitor.height

    x = monitor.x + (screen_width - width) // 2
    y = monitor.y + (screen_height - height) // 2

    root.geometry(f"{width}x{height}+{x}+{y}")