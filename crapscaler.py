# Crappy image upscaling
# Done from scratch, with no research done

from PIL import Image

import numpy as np
import itertools
import datetime
import sys
import os

# Take in two numpy ndarrays of colours, in the form:
#  [red green blue alpha]
#   or
#  [red green blue]
# and return a numpy ndarray with the average rgb(a) values
#  i.e. their average colour
def avg_colour(colour_a: np.ndarray, colour_b: np.ndarray) -> np.ndarray:
    # If there is alpha (assuming no other type than rgba and rgb is used)
    if len(colour_a) == 4:
        # Unpack the colour ndarrays, converting into int to avoid overflows
        r_a, g_a, b_a, a_a = map(int, colour_a)
        r_b, g_b, b_b, a_b = map(int, colour_b)
        # Get the averages
        r_m, g_m, b_m, a_m = (r_a+r_b)/2, (g_a+g_b)/2, (b_a+b_b)/2, (a_a+a_b)/2
        # Return the averages, rounded and converted back into uint8
        return np.array(list(map(
            np.uint8,
            [
                round(r_m),
                round(g_m),
                round(b_m),
                round(a_m)
            ]
        )))
    # If there is no alpha (assuming no other type than rgba and rgb is used)
    else:
        # Unpack the colour ndarrays, converting into int to avoid overflows
        r_a, g_a, b_a = map(int, colour_a)
        r_b, g_b, b_b = map(int, colour_b)
        # Get the averages
        r_m, g_m, b_m = (r_a+r_b)/2, (g_a+g_b)/2, (b_a+b_b)/2
        # Return the averages, rounded and converted back into uint8
        return np.array(list(map(
            np.uint8,
            [
                round(r_m),
                round(g_m),
                round(b_m)
            ]
        )))

# Upscale array by inserting n-1 averages
def crapscale_colour_array(array: list) -> list:
    # Make a new list
    new = []
    # Initialise 'previous' variable
    prev = None

    # Go through all the colours in the array
    for colour in array:
        # If there's a 'previous'
        if prev is not None:
            # Find the average between it and the current colour
            mid = avg_colour(colour, prev)
            # Append it to the list
            new.append(np.array(mid))
        # Append the current colour to the list
        new.append(colour)
        # Make the current colour previous
        prev = colour

    # Return the list
    return new

# Crapscale image on path, return new image or error value None
def crapscale(path: str) -> Image.Image:
    # Open the image
    with Image.open(path) as pic:
        # Load it into an array
        ima = np.asarray(pic)

        # Make a list for the new image
        new_pix_array = []
        # Go through the rows of the old image
        for row in ima:
            # Upscale each row
            new_pix_array.append(np.array(crapscale_colour_array(row)))
        # Transpose the array
        new_pix_array = np.transpose(new_pix_array, (1,0,2))
        
        # Make another new list
        newer_pix_array = []
        
        # Go through the rows again, now working on columns actually
        for row in new_pix_array:
            # Upscale each row (column)
            newer_pix_array.append(np.array(crapscale_colour_array(row)))
        # Transpose the array back
        newer_pix_array = np.transpose(newer_pix_array, (1,0,2))

        # Create and return the new image
        return Image.fromarray(newer_pix_array)

# If the program is run and not imported
if __name__ == "__main__":
    # If there are not enough arguments
    if len(sys.argv) < 2:
        # Tell the user what to do
        print("You need to supply a path to an image as the first argument!")
        print("Subsequent arguments will be ignored!")
        # Exit program
        exit()
    # If the first argument is not a file
    elif not os.path.isfile(sys.argv[1]):
        # Tell the user what to do
        print("You need to supply a path to an image as the first argument!")
        print("Subsequent arguments will be ignored!")
        # Exit program
        exit()
    # Provided that the previous two requirements were met
    else:
        # Catch all exceptions
        try:
            # Crapscale the image
            new = crapscale(sys.argv[1])
        # If an error occurs
        except Exception as e:
            # Notify the user
            print("There has been an error:", e)
            # Set new to the error value, None
            new = None
        # If the new image is not the error value, i.e. is not None
        if new is not None:
            # Create a timestamp of that exact moment, excluding milliseconds
            now = str(datetime.datetime.now()).rsplit('.')[0]
            # Format the timestamp a bit
            now = now.replace('-','_').replace(':','_').replace(' ','_')
            # Split the argument name
            argsplit = sys.argv[1].rsplit('.', 1)
            # Make the new filename
            filename = argsplit[0]+'_crapscaled_'+now+'.'+argsplit[1]
            # Save the image with the old name plus the timestamp
            new.save(filename)
            # Notify the user that the file has been crapscaled
            print(f"File {sys.argv[1]} crapscaled and saved as {filename}")
        # If there was an error
        else:
            # Report that the image has not been crapscaled
            print("The image has not been crapscaled.")
