import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Hello World App")

# Set window size
window.geometry("400x500")

# Create a label widget
label = tk.Label(window, text="Hello, World!", font=("Arial", 16))

# Add the label to the window
label.pack(pady=20)

# Run the application
window.mainloop()
