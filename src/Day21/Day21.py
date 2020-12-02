
import io

rules = {}

# Process Input
f=open("input.txt",'r')
f=open("inputTest.txt",'r')
for line in f.readlines():
    key = line.split('=>')[0].strip()
    rules[key] = line.split('=>')[1].strip().split('\n')[0]
f.close()

def get_active_pixels(image):
    return image.count('#')

def get_image_size(image):
    return len(image.split('/')[0])

def rotate_image_90_degrees(image):
    return image[8] + image[4] + image[0] + '/' + image[9] + image[5] + image[1] + '/' + image[10] + image[6] + image[2]

def flip_image(image):
    return image[2] + image[1] + image[0] + '/' + image[6] + image[5] + image[4] + '/' + image[10] + image[9] + image[8]

def create_all_patterns(image):
    split_image = image.split('/')
    if len(split_image) == 3:
        patterns = [image, flip_image(image)]

        # rotate and flip it 3 times
        for i in range(3):
            # Rotate the image
            rotated_image = rotate_image_90_degrees(image)
            patterns.append(rotated_image)

            # Flip the image
            patterns.append(flip_image(rotated_image))

            # Set the base image to the rotated image
            image = rotated_image
    elif len(split_image == 2):
        patterns = []
        # Rotate each image
        patterns.append(image[0] + image[1] + '/' + image[3] + image[4])
        patterns.append(image[3] + image[0] + '/' + image[4] + image[1])
        patterns.append(image[4] + image[3] + '/' + image[1] + image[0])
        patterns.append(image[1] + image[4] + '/' + image[0] + image[3])
        # Flip each image
        patterns.append(image[1] + image[0] + '/' + image[4] + image[3])
        patterns.append(image[0] + image[3] + '/' + image[1] + image[4])
        patterns.append(image[3] + image[4] + '/' + image[0] + image[1])
        patterns.append(image[4] + image[1] + '/' + image[3] + image[0])
    return patterns

def find_matching_rule(image):
    patterns = create_all_patterns(image)
    return next(p for p in patterns if rules.get(p) != None)

def break_image_in_subimages(image, size_subimage, amount):
    sub_images = []
    inc = get_image_size(image) + 1
    for a in range(amount):
        if size_subimage == 2:
            sub_images.append(image[0 + (inc * int(a))] + image[1 + (inc * int(a))] + '/' + image[0 + (inc * int(a)) + get_image_size(image)] + image[1 + (inc * int(a)) + get_image_size(image)])

    return sub_images

image = '.#./..#/###'
image = '#..#/..../..../#..#'

ims = break_image_in_subimages(image, 2, 4)

print('DOne!')
#for i in range(2):
#    size = get_image_size(image)
#    if size % 3 == 0:
#        # Calculate how many times to split up the image
#        am = size / 3


#image_matching_rule = find_matching_rule(image)
