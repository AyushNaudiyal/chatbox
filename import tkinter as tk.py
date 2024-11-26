import tkinter as tk
from tkinter import scrolledtext
from datetime import datetime
import random
from tkinter import ttk

class ChatApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("Chat Application")
        self.root.geometry("600x400")
        
        # Create main container
        self.main_container = ttk.Frame(self.root, padding="10")
        self.main_container.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
        # Create chat display area
        self.chat_display = scrolledtext.ScrolledText(
            self.main_container,
            wrap=tk.WORD,
            width=50,
            height=20
        )
        self.chat_display.grid(row=0, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S))
        self.chat_display.config(state=tk.DISABLED)
        
        # Create message input field
        self.message_input = ttk.Entry(
            self.main_container,
            width=40
        )
        self.message_input.grid(row=1, column=0, sticky=(tk.W, tk.E), padx=(0, 5), pady=5)
        self.message_input.bind("<Return>", self.send_message)
        
        # Create send button
        self.send_button = ttk.Button(
            self.main_container,
            text="Send",
            command=self.send_message
        )
        self.send_button.grid(row=1, column=1, sticky=(tk.E), pady=5)
        
        # Configure grid weights
        self.main_container.columnconfigure(0, weight=1)
        self.main_container.rowconfigure(0, weight=1)
        
        # Sample responses for demo
        self.responses = [
            "That's interesting! Tell me more.",
            "I understand what you mean.",
            "Could you elaborate on that?",
            "That's a great point!",
            "I hadn't thought about it that way before.",
            "Thanks for sharing that with me.",
            "What makes you say that?",
            "That's fascinating!"
        ]

    def display_message(self, message, sender):
        self.chat_display.config(state=tk.NORMAL)
        timestamp = datetime.now().strftime("%H:%M")
        formatted_message = f"[{timestamp}] {sender}: {message}\n"
        self.chat_display.insert(tk.END, formatted_message)
        self.chat_display.see(tk.END)
        self.chat_display.config(state=tk.DISABLED)

    def send_message(self, event=None):
        message = self.message_input.get().strip()
        if message:
            # Display user message
            self.display_message(message, "You")
            self.message_input.delete(0, tk.END)
            
            # Simulate response after a short delay
            self.root.after(1000, self.automated_response)

    def automated_response(self):
        response = random.choice(self.responses)
        self.display_message(response, "Bot")

def main():
    root = tk.Tk()
    app = ChatApplication(root)
    root.mainloop()

if __name__ == "__main__":
    main()