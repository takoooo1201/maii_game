import pyautogui
import time
import cv2
import numpy as np

# Load the target doll image
target_doll_image = r"target_image.png"  # Replace with the path to your specific doll image
target_doll_image_path = "target_image.png"
target_image = cv2.imread(target_doll_image_path, cv2.IMREAD_UNCHANGED)

# Function to simulate finding and clicking the specific doll
def find_and_click_doll():
    try:
        # Locate the image of the target doll on the screen
        location = pyautogui.locateCenterOnScreen(target_doll_image, confidence=0.8)  # Adjust confidence as needed
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
    
# Function to resize and match the doll in different scales
def find_and_click_doll_dynamic(scale_range=(0.5, 1.5), step=0.1):
    screen = pyautogui.screenshot()
    screen_np = np.array(screen)  # Convert screenshot to numpy array
    screen_gray = cv2.cvtColor(screen_np, cv2.COLOR_RGB2GRAY)

    for scale in np.arange(scale_range[0], scale_range[1], step):
        resized_target = cv2.resize(target_image, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
        result = cv2.matchTemplate(screen_gray, cv2.cvtColor(resized_target, cv2.COLOR_BGR2GRAY), cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        # If confidence is high enough, click the location
        if max_val >= 0.8:  # Adjust confidence threshold as needed
            click_point = (max_loc[0] + resized_target.shape[1] // 2, max_loc[1] + resized_target.shape[0] // 2)
            pyautogui.click(click_point)
            print(f"Clicked on the doll at {click_point}, scale {scale}.")
            return True
    print("Doll not found on the screen.")
    return False


# Main simulation loop
def simulate_gameplay():
    score = 0
    while True:
        if find_and_click_doll_dynamic():
            score += 1
            time.sleep(0.5)  # Wait for the doll to disappear
            print(f"Score: {score}")

        # Simulate increasing density by waiting less between clicks
        # time.sleep(max(0.5, 2 - score * 0.1))  # Reduce wait time as score increases

    print(f"Game over! Final score: {score}")

# Start the simulation
if __name__ == "__main__":
    simulate_gameplay()
