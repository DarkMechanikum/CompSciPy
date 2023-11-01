from utils import *

if __name__ == "__main__":
    try:
        args = parse_args()
    except Exception as e:
        print(f"Error: {e}")
        exit(1)

    command = args.command
    if command == "1":
        print_pythin_version()
    elif command == "2":
        create_dir_by_path(args.path)
    elif command == "3":
        print_parent_dir()
    else:
        print(f"Invalid command: {command}")