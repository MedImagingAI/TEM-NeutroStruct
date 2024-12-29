import json
import pandas as pd
import numpy as np

# Load the COCO JSON file
with open('./7classes_version/train/annotations/annotations_7classes.json', 'r') as f:
    data = json.load(f)

# Load the scale data
scale_data = pd.read_excel('./metadata/train_images_statistics_with_diameters.xlsx')
average_diameter = scale_data.set_index('image_name')['average_diameter_SG_PG'].to_dict()

# Define new class IDs
NEW_CLASSES_CLASS3 = {
    'Empty vesicles': 9,
    'Vacuoles': 10
}

# Update the annotations for class 3
for annotation in data['annotations']:
    image_name = next((img['file_name'] for img in data['images'] if img['id'] == annotation['image_id']), None)

    if not image_name or annotation['category_id'] != 3:  # Skip if not class 3
        continue

    PIXELS_PER_MICROMETER = scale_dict.get(image_name, 375)
    diameter = (annotation['bbox'][2] + annotation['bbox'][3]) / (2 * PIXELS_PER_MICROMETER)

    threshold = average_diameter.get(image_name)
    annotation['category_id'] = NEW_CLASSES_CLASS3['Vacuoles'] if diameter > threshold else NEW_CLASSES_CLASS3['Empty vesicles']

# Save the updated JSON
output_json_path = './7classes_version/train/annotations/annotations_7classes_updated.json'
with open(output_json_path, 'w') as f:
    json.dump(data, f)
print(f"Updated JSON file saved to: {output_json_path}")
