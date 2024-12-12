import tkinter as tk
from tkinter import Canvas, messagebox
from qrcode import QRCode
from PIL import Image, ImageTk

def draw_ui(canvas):
    canvas.delete("all")

    # Load and display the logo image on the canvas
    logo = Image.open("resources/spot_on_beauty.png")  # Load the image
    logo_resized = logo.resize((400, 133))  # Resize if needed to fit canvas dimensions
    logo_image = ImageTk.PhotoImage(logo_resized)  # Convert to PhotoImage for Tkinter

    # Keep a reference to avoid garbage collection
    canvas.image = logo_image

    # Draw the image on the canvas
    canvas.create_image(250, 110, image=logo_image)  # Centered in the 220x220 canvas

def update_ui():
    try:
        link = entry.get()
        file_name = file_name_entry.get()

        if not link or not file_name:
            messagebox.showerror("Error", "Please enter a name for the QR Code file and a link")
            return

        # Generate a QR code
        qr = QRCode()
        qr.add_data(link)
        qr.make(fit=True)
        qr_image = qr.make_image()

        # Save the QR code image
        qr_image.save("qrCodes/" + file_name + ".png")
        messagebox.showinfo("Success", "QR Code has been generated and saved in the qrCodes folder")

    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    finally:
        entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("QR Code Generator")

# Canvas for drawing the gauge
canvas = Canvas(root, width=500, height=200, bg="white")
canvas.pack()

# Initialize the gauge to a default value and display the logo
draw_ui(canvas)

# Label for the Entry
file_name_label = tk.Label(root, text="Enter the name for the QR Code:")
file_name_label.pack()

file_name_entry = tk.Entry(root, width=25)
file_name_entry.pack()

# Label for the Entry
entry_label = tk.Label(root, text="Enter the link for QR Code:")
entry_label.pack()

# Entry widget for text input
entry = tk.Entry(root, width=50)
entry.pack()

# Button to generate QR Code
update_button = tk.Button(root, text="Generate QR Code", command=update_ui)
update_button.pack()

root.mainloop()
