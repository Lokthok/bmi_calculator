from functions import slow_typing
from functions import bmi_calc
import time
import sys

def main():
    if not len(sys.argv) == 4:
        print("Usage: python3 main.py <name> <weight> <height>")
        print("name: string | weight(kg): integer | height(cm): integer")
        sys.exit(1)
    name = sys.argv[1]
    weight = int(sys.argv[2])
    height = int(sys.argv[3])
    bmi = bmi_calc(weight, height)
    print("============ BMI-CALCULATOR ============")
    slow_typing("Analyzing data...")
    slow_typing("")
    slow_typing(f"Name: {name}")
    slow_typing(f"Weight: {weight}")
    slow_typing(f"Height: {height}")
    slow_typing("")
    slow_typing("Calculating...")
    slow_typing("")
    slow_typing(f"{name} your BMI is: {bmi}")
    print("============= END ===============")

main()
