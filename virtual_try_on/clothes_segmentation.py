# ClothesSegmentation.py
from transformers import pipeline
from PIL import Image
import numpy as np

# Segmentation pipeline
segmentation_pipeline = pipeline(model="mattmdjaga/segformer_b2_clothes")

def segment_clothing(image, clothing_items=["Hat", "Upper-clothes", "Skirt", "Pants", "Dress", "Belt", "Left-shoe", "Right-shoe", "Scarf"]):
    segmented_output = segmentation_pipeline(image)
    masks = [segment['mask'] for segment in segmented_output if segment['label'] in clothing_items]

    combined_mask = np.array(masks[0])
    for mask in masks[1:]:
        combined_mask += np.array(mask)

    combined_mask_image = Image.fromarray(combined_mask)
    image.putalpha(combined_mask_image)

    return image
