from utils.config import read_config

def main():
    config = read_config()
    collection = connect_collection(config)

    while(True):
        cmd = raw_input('>>> ')
        if cmd == ":q":
            print("Program finished")
            exit(0)
        elif cmd == ':h':
            print("Type a name after the promt (>>>)")
            print(":h Help")
            print(":q Quit")
        else:
            pass

if __name__ == "__main__":
    main()
