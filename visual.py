import tkinter as tk
import pyotp
import time

def generate_google_2fa_code(secret):
    totp = pyotp.TOTP(secret)
    return totp.now()

def seconds_remaining():
    return 30 - (int(time.time()) % 30)

def update_display():
    #Update name lael
    name_label.config(text=f"{nickName}")

    # Update the 2FA code
    code = generate_google_2fa_code(secretKey)
    code_label.config(text=f"{code}")

    # Update the seconds remaining
    remaining = seconds_remaining()
    time_label.config(text=f"{remaining}")

    # Schedule the next update in 1 second (to decrease the countdown)
    root.after(1000, update_display)

def close_window():
    root.destroy()

if __name__ == "__main__":
    nickName = "Google 2FA Code:"
    secret = 'PASTE YOUR KEY HERE'
    secretKey = secret.replace(" ", "")
    
    # Create the main tkinter window
    root = tk.Tk()
    root.title('2FA Code Display')
    
    # Create a label for the nickname
    name_label = tk.Label(root, font=("Arial", 18))
    name_label.pack(pady=10, padx=10)

    # Create a label for the 2FA code
    code_label = tk.Label(root, font=("Arial", 32))
    code_label.pack(pady=10, padx=20)

    # Create a label for the seconds remaining
    time_label = tk.Label(root, font=("Arial", 16))
    time_label.pack(pady=5, padx=20)

    # Create a "Close" button
    close_button = tk.Button(root, text="Close", command=close_window)
    close_button.pack(pady=10)
    
    # Start the initial update
    update_display()
    
    # Run the tkinter main loop
    root.mainloop()
