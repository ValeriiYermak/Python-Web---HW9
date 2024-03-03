from hw9 import find_by_tag, find_by_author


def search_quotes():
    while True:
        command = input("Input command (tag, author або tags): ").strip().split(':', 1)
        if len(command) != 2:
            if command[0] == 'exit':
                print("Good bye!")
                break
            print("Wrong format of command. Try again.")
            continue

        action, value = command
        if action not in ['tag', 'author', 'tags']:
            print("Wrong command. Available commands: tag, author, tags.")
            continue

        if action == 'tag':
            print(find_by_tag(value.strip()))
        elif action == 'author':
            print(find_by_author(value.strip()))
        elif action == 'tags':
            tags = value.split(',')
            for tag in tags:
                print(find_by_tag(tag.strip()))

if __name__ == '__main__':
    search_quotes()
