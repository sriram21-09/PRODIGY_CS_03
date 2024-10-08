import re

def assess_password_strength(password):
    strength = {"Length": False, "Uppercase": False, "Lowercase": False, "Digits": False, "Special Characters": False}
    
    if len(password) >= 8:
        strength["Length"] = True
    if re.search(r'[A-Z]', password):
        strength["Uppercase"] = True
    if re.search(r'[a-z]', password):
        strength["Lowercase"] = True
    if re.search(r'[0-9]', password):
        strength["Digits"] = True
    if re.search(r'[\W_]', password):
        strength["Special Characters"] = True
    
    total_strength = sum(strength.values())
    
    feedback = "Password Strength: "
    if total_strength < 3:
        feedback += "Weak"
    elif total_strength == 3 or total_strength == 4:
        feedback += "Moderate"
    elif total_strength == 5:
        feedback += "Strong"

    return feedback, strength

password = input("Enter the password: ")
feedback, strength = assess_password_strength(password)

print(feedback)
for criterion, met in strength.items():
    print(f"{criterion}: {'Met' if met else 'Not Met'}")
