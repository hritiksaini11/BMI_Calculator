GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
END = '\033[0m'

def get_category_and_color(bmi):
    """Returns the category name and a color code based on BMI value."""
    if bmi < 18.5:
        return "Underweight", YELLOW
    elif bmi < 25:
        return "Normal weight", GREEN
    elif bmi < 30:
        return "Overweight", YELLOW
    elif bmi < 35:
        return "Obesity class I", RED
    elif bmi < 40:
        return "Obesity class II", RED
    else:
        return "Obesity class III", RED


def get_health_message(category: str) -> str:
    messages = {
        "Underweight": "You may need to gain some weight. Consider consulting a nutritionist.",
        "Normal weight": "You're in the healthy range — great job!",
        "Overweight": "Consider adopting healthier eating habits and increasing physical activity.",
        "Obesity class I": "It is recommended to consult a doctor or nutritionist.",
        "Obesity class II": "Medical evaluation and lifestyle changes are strongly recommended.",
        "Obesity class III": "Please seek professional medical advice as soon as possible."
    }
    return messages.get(category, "No message available for this category.")


def main():
    print("=== SIMPLE BMI CALCULATOR ===")
    
    # List to store our history
    history = []

    running = True
    while running:
        print("\nPlease enter your details:")
        
        
        try:
            weight = float(input("Weight (kg): "))
            height = float(input("Height (meters): "))
            
            if weight <= 0 or height <= 0:
                print("Error: Weight and height must be positive numbers.")
                continue
        except ValueError:
            print("Error: Please enter numbers only (e.g., 70.5).")
            continue

        
        bmi = weight / (height * height)
        
        
        category, color = get_category_and_color(bmi)
        message = get_health_message(category)

       
        print("\nRESULTS:")
        print("BMI:      " + color + str(round(bmi, 2)) + END)
        print("Category: " + color + category + END)
        print("Advice:   " + message)

        # Add to history list 
        history_entry = f"Weight: {weight}kg | BMI: {round(bmi, 2)} | {category}"
        history.append(history_entry)

       # if user wants to continue
        choice = input("\nCalculate another? (y/n): ").lower()
        if choice != 'y':
            running = False

   
    print("\n=== SESSION SUMMARY ===")
    if len(history) == 0:
        print("No calculations performed.")
    else:
        for item in history:
            print("- " + item)
    
    print("\nThank you for using the calculator!")


if __name__ == "__main__":
    main()
