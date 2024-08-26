import threading
import time

def timed_input(prompt, timeout):
    """
    Prompt the user for input with a timeout.

    :param prompt: The prompt to display to the user
    :param timeout: The time in seconds before the input times out
    :return: User's input or None if the timeout is reached
    """
    print(prompt, end='', flush=True)

    # Function to get input
    def get_input():
        nonlocal user_input
        user_input = input()

    user_input = None
    thread = threading.Thread(target=get_input)
    thread.start()
    thread.join(timeout)

    if thread.is_alive():
        print("\nTempo esgotado! Ação não realizada.")
        thread.join()  # Wait for the thread to finish
        return None
    else:
        return user_input

# Example usage
def main():
    print("Você tem 5 segundos para fazer uma escolha:")
    choice = timed_input("Escolha uma opção (1/2/3): ", 5)

    if choice is None:
        print("Nenhuma escolha foi feita a tempo.")
    else:
        print(f"Você escolheu: {choice}")

if __name__ == "__main__":
    main()
