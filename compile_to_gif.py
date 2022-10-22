import imageio

def compile_images(output_filename, directory, filetype, num_images):
    images = []
    filenames = [directory + str(x) + filetype for x in range(num_images)]
    for filename in filenames:
        images.append(imageio.imread(filename))
    imageio.mimsave(output_filename, images)

#compile_images('depth_images.gif', 'images/', '_depth.png', 60)
#compile_images('color_images.gif', 'images/', '_color.png', 60)
compile_images('stitched_gif.gif', 'stitched/', '_stitched.png', 60)