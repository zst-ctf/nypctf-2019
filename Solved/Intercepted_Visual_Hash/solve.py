import hashlib
import string
import re
 
charset = string.ascii_uppercase + string.ascii_lowercase + string.digits

# From our 4 colors in the screenshot, split them up into hex-pairs
target_color = ''.join(["EDF482", "7C92E0", "B766A0", "67947E"])
target_colors_hexpairs = re.findall('..', target_color)

for _a in list(charset):
    for _b in list(charset):
        for _c in list(charset):
            for _d in list(charset):
                text = "NYP{" + _a + _b + _c + _d + "}"
                # assert len(text) == 9

                # Get the hash value and convert to hex-pairs
                hash_color = hashlib.sha1(text.encode()).hexdigest()
                colors_hexpairs = re.findall('..', hash_color)
                # print(colors_hexpairs, target_colors_hexpairs)

                # Tolerance is due to randomisation in the Visual Hashing
                # code and also due to the image JPG compression.
                tolerance = 20

                # For each target hex-pair, compare to our current hash
                # if it is within tolerance, then it matches.
                correct_color = 0
                for i in range(len(target_colors_hexpairs)):
                    color = int(colors_hexpairs[i], 16)
                    lower = int(target_colors_hexpairs[i], 16) - tolerance
                    upper = int(target_colors_hexpairs[i], 16) + tolerance
                    if lower < (color) < upper:
                        correct_color += 1
                print(text, correct_color, end='\r')

                # If it has all correct colors, then print out the flag.
                if correct_color >= len(target_colors_hexpairs):
                    print("Success:", text)
                    quit()
