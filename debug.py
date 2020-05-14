from send_email import extract_summary, extract_contacts, authenticate_account
import fire
import os

if __name__ == '__main__':
    # Export to fire
    # Change module to debug
    fire.Fire(authenticate_account)

    # Debugging Checkpoint 3
    # print(f"os.environ['EMAIL_ADDRESS'] : {os.environ['EMAIL_ADDRESS']}")
    # print(f"os.environ['EMAIL_PASSWORD'] : {os.environ['EMAIL_PASSWORD']}")
