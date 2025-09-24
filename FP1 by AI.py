import random
import time

def generate_lottery_numbers():
    """
    Generates and prints a set of PowerBall lottery numbers.
    The first five numbers are between 1 and 69.
    The final number (Powerball) is between 1 and 26.
    """
    # Greet the user and get their name
    user_name = input("Hello! What is your name? ")
    print(f"Hello, {user_name}! Let's generate your PowerBall numbers.\n")

    # Generate the first five numbers (white balls)
    white_ball_1 = random.randint(1, 69)
    time.sleep(1) # Add a 1-second delay
    white_ball_2 = random.randint(1, 69)
    time.sleep(1)
    white_ball_3 = random.randint(1, 69)
    time.sleep(1)
    white_ball_4 = random.randint(1, 69)
    time.sleep(1)
    white_ball_5 = random.randint(1, 69)
    time.sleep(1)

    # Generate the last number (red Powerball)
    powerball_number = random.randint(1, 26)

    # Print the numbers with the required spacing
    print(f"Your lucky numbers are:")
    print(f"{white_ball_1}  {white_ball_2}  {white_ball_3}  {white_ball_4}  {white_ball_5}    {powerball_number}")

    # Farewell message
    print(f"\nGood luck, {user_name}!")

# Run the function to generate the numbers
if __name__ == "__main__":
    generate_lottery_numbers()