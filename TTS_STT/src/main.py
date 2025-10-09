from tools.tts_sst_tools import TTS_STT_Tools as tstools

def main():
    print("\n\n########## Text-to-Speech (TTS) & Speech-to-Text (STT) ########## \n\n")
    print("1. Text-to-Speech (TTS)")
    print("2. Speech-to-Text (STT)")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    while True:
        if choice == '1':
            text = input("Enter the text to convert to speech: ")
            tstools.text_to_speech(text)
            break
        elif choice == '2':
            tstools.speech_to_text()
            break
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    print("\n Thank you for using TTS & STT Services!\n")


if __name__ == "__main__":
    main()
