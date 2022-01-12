from uwimg import *

# 1. Getting and setting pixels
im = load_image("data/dog.jpg")
for row in range(im.h):
    for col in range(im.w):
        set_pixel(im, col, row, 2, 0)
save_image(im, "dog_no_blue")


# 3. Grayscale image
im = load_image("data/dog.jpg")
graybar = rgb_to_grayscale(im)
save_image(graybar, "graybar")

# 4. Shift Image
im = load_image("data/dog.jpg")
shift_image(im, 0, .4)
shift_image(im, 1, .4)
shift_image(im, 2, .4)
save_image(im, "overflow")

# 5. Clamp Image
# im = load_image("data/dog.jpg")
# clamp_image(im)
# save_image(im, "doglight_fixed")

# 6-7. Colorspace and saturation
im = load_image("data/image-7.png")
rgb_to_hsv(im)
shift_image(im,0,0.1)
hsv_to_rgb(im)
save_image(im, "dog_saturated")
