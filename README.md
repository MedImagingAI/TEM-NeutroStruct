# TEM-NeutroStruct
TEM-NeutroStruct: A Robust Dataset of Neutrophil Ultrastructures for Deep Learning and Biomedical Applications

Overview
--------
TEM-NeutroStruct is a rigorously annotated and validated dataset of neutrophil ultrastructures derived from transmission electron microscopy (TEM) images. Developed over 1 year and 9 months, this dataset provides high-resolution TEM images accompanied by high-quality annotations for object detection and segmentation tasks. It is the first publicly available dataset of its kind, designed to support research in automated TEM image analysis, hematological studies, and deep learning.

The dataset includes:
- 83 training images and 10 test images.
- 21,143 annotations in the training set and 3,150 annotations in the test set.
- Seven annotated classes: Non-specific Primary Granules, Non-specific Secondary Granules, Specific Granules, Non-specific Tertiary Granules, Empty Vesicles, Emptying Vesicles, and Vacuoles.

Annotations
-----------
- **Formats Provided**:
  - COCO JSON format: Compatible with object detection frameworks like YOLO, Faster R-CNN, and EfficientDet.
  - CVAT XML format: Retains the original elliptical shapes for segmentation and modification in annotation tools. These formats are easily convertible to other formats required for deep learning models.
- **Segmentation Masks**:
  - Masks are provided in PNG format, with each class represented by a unique color.

Dataset Features
----------------
- **Image Resolution**:
  - Most images are 4096 x 4224 pixels.
  - Six images have a resolution of 2048 x 2115 pixels.
- **Classes and Annotations**:
  - Seven biologically relevant classes are annotated to capture the structural diversity of neutrophils.
  - Each annotation has been rigorously validated for quality and accuracy.


# 4-to-7 Class Conversion Workflow

The TEM-NeutroStruct dataset includes annotations in both 4-class and 7-class formats, making it ready for use in training and evaluating deep learning models without requiring any additional processing.

For researchers interested in replicating the process of extending 4 classes to 7, this repository includes scripts and instructions for performing the conversion. The workflow involves calculating granule statistics, updating annotations, generating segmentation masks, and verifying the results.

## Steps in the Workflow

### 1. Extract Scale (Micrometer per Pixel)
Using the scale bar in TEM images, extract the micrometer per pixel value using **ImageJ** or similar tools. Save these values as a `.csv` file for further use.

### 2. Calculate Granule Statistics
Run `2_generate_statistics.py` to calculate the mean and median diameters of primary and secondary granules for each image. This script generates an Excel file (`statistics.xlsx`) with:
- Mean and median diameters
- Average diameters for further classification

### 3. Update COCO JSON
Run `3_update_coco_json.py` to:
- Reclassify primary and secondary granules into 4 sub-classes based on median diameter.
- Further classify empty structures into `Empty Vesicles` and `Vacuoles`.

### 4. Update CVAT XML
Run `4_update_cvat_xml.py` to update the CVAT XML annotations from 4 to 7 classes. This uses spatial information from the updated COCO JSON.

### 5. Generate Segmentation Masks
Run `5_generate_masks.py` to create color-coded segmentation masks for the 7 classes. Each class is represented by a unique color.

### 6. Verify Masks
Run `6_verify_masks.py` to overlay the masks onto the original images and visually inspect the accuracy of the annotations.

---

## Requirements
Install the required Python libraries:
```bash
pip install -r requirements.txt

