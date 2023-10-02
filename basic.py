import pyotp
import time

def generate_google_2fa_code(secret):
    totp = pyotp.TOTP(secret)
    return totp.now()

def seconds_remaining():
    return 30 - (int(time.time()) % 30)

if __name__ == "__main__":
    secret = 'PASTE YOUR KEY HERE'
    secretKey = secret.replace(" ", "")
    while True:
        print("Current 2FA Code:", generate_google_2fa_code(secretKey))
        time.sleep(seconds_remaining())
