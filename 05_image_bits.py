
# checks input is a number more than a given value
def num_check(question, low):
    valid = False
    while not valid:

        error = "Please enter a integer that is more than (or equal to) {}".format(low)

        try:

            # ask user to enter a number 
            response = int(input(question))

            # checks number is more than zero
            if response >= low:
                return response

            # outputs error if input is invalid
            else:
                print(error)
                print()

        except ValueError:
            print(error) 
            print()

# finds # of bits for 24 bit colour
def image_bits():

    # get width and height...
    image_width = num_check("Image width? ", 1)
    image_height = num_check("Image height? ", 1)

    # calculate # of pixels
    num_pixels = image_width * image_height

    # calculate # of bits (24 x num pixels)
    num_bits = num_pixels * 24

    # output answer with working
    print()
    print("# of pixels = {} x {} x {}".format(image_height, image_width, num,_pixels))                                         
    print("# bits = {} x 24 = {}").format(num_pixels, num_bits)
    print()

    return ""

# Main routine goes here
image_bits()
