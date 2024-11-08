import tkinter as tk
from tkinter import Canvas, messagebox
from qrcode import QRCode
from PIL import Image, ImageTk

def draw_ui(canvas):
    canvas.delete("all")

    # Load and display the logo image on the canvas
    logo = Image.open("resources/spot_on_beauty.png")  # Load the image
    logo_resized = logo.resize((200, 100))  # Resize if needed to fit canvas dimensions
    logo_image = ImageTk.PhotoImage(logo_resized)  # Convert to PhotoImage for Tkinter

    # Keep a reference to avoid garbage collection
    canvas.image = logo_image

    # Draw the image on the canvas
    canvas.create_image(110, 110, image=logo_image)  # Centered in the 220x220 canvas

def update_ui():
    try:
        link = entry.get()
        
        if not link:
            messagebox.showerror("Error", "Please enter text for the QR Code.")
            return

        # Generate a QR code
        qr = QRCode()
        qr.add_data(link)
        qr.make(fit=True)
        qr_image = qr.make_image()

        # Save the QR code image
        qr_image.save("qr_code_test.png")
        messagebox.showinfo("Success", "QR Code has been generated and saved as 'qr_code_test.png'.")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    finally:
        entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Label for the Entry
entry_label = tk.Label(root, text="Enter text for QR Code:")
entry_label.pack()

# Entry widget for text input
entry = tk.Entry(root)
entry.pack()

# Button to generate QR Code
update_button = tk.Button(root, text="Generate QR Code", command=update_ui)
update_button.pack()

# Canvas for drawing the gauge
canvas = Canvas(root, width=400, height=200, bg="white")
canvas.pack()

# Initialize the gauge to a default value and display the logo
draw_ui(canvas)

root.mainloop()
