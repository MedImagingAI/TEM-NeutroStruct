import json
import pandas as pd

# Load the COCO JSON file
with open('./7classes_version/train/annotations/annotations_4classes.json', 'r') as f:
    data = json.load(f)

# Load the scale and median values from the train statistics file
scale_data = pd.read_excel('./metadata/train_images_statistics_with_diameters.xlsx')
median_dict = scale_data.set_index('image_name')['median_diameter'].to_dict()

# Define new class IDs
NEW_CLASSES = {
    'Specific granules': 5,
    'Non-specific primary granules': 6,
    'Non-specific tertiary granules': 7,
    'Non-specific secondary granules': 8
}

# Update the annotations
for annotation in data['annotations']:
    image_name = next((img['file_name'] for img in data['images'] if img['id'] == annotation['image_id']), None)
    median_threshold = median_dict.get(image_name)

    if image_name and annotation['category_id'] == 1:  # Primary granules
        diameter = (annotation['bbox'][2] + annotation['bbox'][3]) / (2 * scale_dict[image_name])
        annotation['category_id'] = NEW_CLASSES['Specific granules'] if diameter <= median_threshold else NEW_CLASSES['Non-specific primary granules']
    elif image_name and annotation['category_id'] == 2:  # Secondary granules
        diameter = (annotation['bbox'][2] + annotation['bbox'][3]) / (2 * scale_dict[image_name])
        annotation['category_id'] = NEW_CLASSES['Non-specific tertiary granules'] if diameter <= median_threshold else NEW_CLASSES['Non-specific secondary granules']

# Save the updated JSON
output_json_path = './7classes_version/train/annotations/annotations_7classes.json'
with open(output_json_path, 'w') as f:
    json.dump(data, f)
print(f"Updated COCO JSON saved to: {output_json_path}")
