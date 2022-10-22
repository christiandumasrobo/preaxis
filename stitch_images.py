import sys
from PIL import Image

filenames = zip(['images/' + str(x) + '_depth.png' for x in range(60)], ['images/' + str(x) + '_color.png' for x in range(60)])
for idx, filename in enumerate(filenames):
    images = [Image.open(x) for x in filename]
    widths, heights = zip(*(i.size for i in images))

    total_width = sum(widths)
    max_height = max(heights)

    new_im = Image.new('RGB', (total_width, max_height))

    x_offset = 0
    for im in images:
      new_im.paste(im, (x_offset,0))
      x_offset += im.size[0]

    new_im.save('stitched/' + str(idx) + '_stitched.png')