import pyautogui
import time

# Load the target doll image
target_doll_image = r"C:\Users\thomas\Desktop\maii_game\target.png"  # Replace with the path to your specific doll image

# Function to simulate finding and clicking the specific doll
def find_and_click_doll():
    try:
        # Locate the image of the target doll on the screen
        location = pyautogui.locateCenterOnScreen(target_doll_image)#, confidence=0.8)  # Adjust confidence as needed
        if location:
            # Click on the target doll
            pyautogui.click(location)
            print(f"Clicked on the doll at {location}.")
            return True
        else:
            print("Doll not found on the screen.")
            return False
    except Exception as e:
        print(f"Error: {e}")
        return False

# Main simulation loop
def simulate_gameplay():
    score = 0
    while True:
        if find_and_click_doll():
            score += 1
            time.sleep(0.5)  # Wait for the doll to disappear
            print(f"Score: {score}")

        # Simulate increasing density by waiting less between clicks
        # time.sleep(max(0.5, 2 - score * 0.1))  # Reduce wait time as score increases

    print(f"Game over! Final score: {score}")

# Start the simulation
if __name__ == "__main__":
    simulate_gameplay()
