from typing import Tuple
import sys
import time

# ANSI color codes (works in terminals: VS Code, Linux, macOS, Windows)
class Colors:
    HEADER    = '\033[95m'
    OKBLUE    = '\033[94m'
    OKCYAN    = '\033[96m'
    OKGREEN   = '\033[92m'
    WARNING   = '\033[93m'
    FAIL      = '\033[91m'
    ENDC      = '\033[0m'
    BOLD      = '\033[1m'
    UNDERLINE = '\033[4m'


def calculate_bmi(weight_kg: float, height_m: float) -> float:
    """Calculate BMI using the standard formula: weight(kg) / height(m)²"""
    return weight_kg / (height_m ** 2)


def get_bmi_category(bmi: float) -> Tuple[str, str]:
    """
     according to WHO classification
    """
    if bmi < 18.5:
        return "Underweight", Colors.WARNING
    elif 18.5 <= bmi < 25:
        return "Normal weight", Colors.OKGREEN
    elif 25 <= bmi < 30:
        return "Overweight", Colors.WARNING
    elif 30 <= bmi < 35:
        return "Obesity class I", Colors.FAIL
    elif 35 <= bmi < 40:
        return "Obesity class II", Colors.FAIL
    else:
        return "Obesity class III", Colors.FAIL


def get_health_message(category: str) -> str:
    messages = {
        "Underweight": "You may need to gain some weight. Consider consulting a nutritionist.",
        "Normal weight": "You're in the healthy range — great job!",
        "Overweight": "Consider adopting healthier eating habits and increasing physical activity.",
        "Obesity class I": "It is recommended to consult a doctor or nutritionist.",
        "Obesity class II": "Medical evaluation and lifestyle changes are strongly recommended.",
        "Obesity class III": "Please seek professional medical advice as soon as possible."
    }
    return messages.get(category, "No specific advice available.")


def get_valid_float(prompt: str, min_val: float, max_val: float) -> float:
    """Get float input with validation loop"""
    while True:
        try:
            value = float(input(prompt))
            if min_val <= value <= max_val:
                return value
            else:
                print(f"{Colors.WARNING}Value must be between {min_val} and {max_val}.{Colors.ENDC}")
        except ValueError:
            print(f"{Colors.FAIL}Please enter a valid number.{Colors.ENDC}")


def main():
    print(f"\n{Colors.HEADER}{Colors.BOLD}═══ BMI Calculator (WHO Classification) ═══{Colors.ENDC}\n")

    history = []

    while True:
        print(f"{Colors.OKCYAN}→ Enter your measurements:{Colors.ENDC}")

        weight = get_valid_float("Weight (kg)     → ", 20, 300)
        height = get_valid_float("Height (meters) → ", 1.0, 2.5)

        bmi = calculate_bmi(weight, height)
        category, color = get_bmi_category(bmi)
        message = get_health_message(category)

        print(f"\n{Colors.BOLD}Results:{Colors.ENDC}")
        print(f"  • BMI          : {color}{bmi:.2f}{Colors.ENDC}")
        print(f"  • Classification: {color}{category}{Colors.ENDC}")
        print(f"  • Health note  : {message}\n")

        # Save to history
        entry = f"{time.strftime('%H:%M:%S')} | {weight:5.1f} kg | {height:4.2f} m | {bmi:5.2f} | {category}"
        history.append(entry)

        again = input(f"{Colors.OKBLUE}Calculate another? (y/n): {Colors.ENDC}").strip().lower()
        if again not in ('y', 'yes', ''):
            break

    # Summary
    if history:
        print(f"\n{Colors.HEADER}{Colors.BOLD}═══ Session Summary ═══{Colors.ENDC}")
        print(f"Total calculations: {len(history)}\n")
        for line in history:
            print(f"  {line}")
        print()

    print(f"{Colors.OKGREEN}Thank you for using the BMI Calculator!{Colors.ENDC}\n")


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{Colors.WARNING}Program terminated by user.{Colors.ENDC}")
        sys.exit(0)
    except Exception as e:
        print(f"\n{Colors.FAIL}An unexpected error occurred: {e}{Colors.ENDC}")
        sys.exit(1)