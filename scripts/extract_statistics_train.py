import json
import pandas as pd
import numpy as np

# Load the COCO JSON file
with open('./7classes_version/train/annotations/annotations_4classes.json', 'r') as f:
    data = json.load(f)

# Load the scale values from the train statistics file
scale_data = pd.read_excel('./metadata/train_images_statistics.xlsx')
scale_dict = scale_data.set_index('image_name')['Pixles per microm'].to_dict()

# Dictionary to store results
results = {}

# Calculate mean and median diameters for each image
for image in data['images']:
    image_id = image['id']
    image_name = image['file_name']
    diameters = []

    PIXELS_PER_MICROMETER = scale_dict.get(image_name, 375)  # Default if not found

    for annotation in data['annotations']:
        if annotation['image_id'] == image_id and annotation['category_id'] in [1, 2]:
            width = annotation['bbox'][2] / PIXELS_PER_MICROMETER
            height = annotation['bbox'][3] / PIXELS_PER_MICROMETER
            diameter = (width + height) / 2
            diameters.append(diameter)

    if diameters:
        results[image_name] = {
            'mean_diameter': np.mean(diameters),
            'median_diameter': np.median(diameters)
        }

# Save the results to an Excel file
output_path = './metadata/train_images_statistics_with_diameters.xlsx'
df = pd.DataFrame.from_dict(results, orient='index')
df.to_excel(output_path)
print(f"Train set statistics saved to: {output_path}")
