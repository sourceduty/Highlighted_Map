# Find and highlight map image locations.
#Copyright (C) 2023,  Sourceduty - All Rights Reserved.

from PIL import Image, ImageDraw

def highlight_locations(image_path, locations, output_path):
    # Open the map image
    image = Image.open(image_path)
    draw = ImageDraw.Draw(image)

    # Define the highlight color and size
    highlight_color = (255, 0, 0)  # Red color
    highlight_size = 10  # Radius of the highlight circle

    for location in locations:
        x, y = location
        # Calculate the coordinates for the circle to highlight the location
        x0, y0 = x - highlight_size, y - highlight_size
        x1, y1 = x + highlight_size, y + highlight_size

        # Draw a filled circle to highlight the location
        draw.ellipse([x0, y0, x1, y1], fill=highlight_color)

    # Save the modified image with highlights
    image.save(output_path)
    image.show()

if __name__ == "__main__":
    map_image_path = "your_map_image.jpg"  # Replace with your map image file path
    highlighted_locations = [(100, 200), (300, 400)]  # Add the coordinates of the locations to highlight
    output_image_path = "highlighted_map.jpg"  # Output image with highlights

    highlight_locations(map_image_path, highlighted_locations, output_image_path)
