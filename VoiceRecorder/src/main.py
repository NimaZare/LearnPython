from tools.voice_tools import VoiceTools as vt

def main():
    print("\n ********** Voice Recorder ********** \n")
    print("1. Record Audio")
    print("2. Play Audio")
    print("3. Exit")
    choice = input("Enter your choice: ")
    
    while True:
        if choice == '1':
            vt.record_audio(5, 44100)
            break
        elif choice == '2':
            file_path = input("Enter the file path to play: ").strip('"').strip("'").strip()
            vt.play_audio(file_path)
            break
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

    print("\n Thank you for using Voice Recorder!\n")


if __name__ == "__main__":
    main()
