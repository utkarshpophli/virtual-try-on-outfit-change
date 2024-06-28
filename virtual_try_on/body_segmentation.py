# BodySegmentation.py
import numpy as np
import cv2
from PIL import Image, ImageDraw
import insightface
from insightface.app import FaceAnalysis
from transformers import pipeline

# Face detection
face_analyzer = FaceAnalysis(providers=['CUDAExecutionProvider', 'CPUExecutionProvider'])
face_analyzer.prepare(ctx_id=0, det_size=(640, 640))

# Segmentation pipeline
segmentation_model = pipeline(model="mattmdjaga/segformer_b2_clothes")

def mask_face(img, mask):
    img_array = np.array(img)
    detected_faces = face_analyzer.get(img_array)

    if not detected_faces:
        return mask

    face = detected_faces[0]['bbox']

    face_width = face[2] - face[0]
    face_height = face[3] - face[1]

    face[0] -= face_width * 0.5
    face[2] += face_width * 0.5
    face[1] -= face_height * 0.5
    face[3] += face_height * 0.2

    face_coords = [(face[0], face[1]), (face[2], face[3])]

    draw = ImageDraw.Draw(mask)
    draw.rectangle(face_coords, fill=0)

    return mask

def apply_segmentation(original_img, include_face=True):
    img = original_img.copy()
    segments = segmentation_model(img)

    segment_labels = ["Hat", "Hair", "Sunglasses", "Upper-clothes", "Skirt", "Pants", "Dress", "Belt", "Left-shoe", "Right-shoe", "Face", "Left-leg", "Right-leg", "Left-arm", "Right-arm", "Bag", "Scarf"]
    masks = [s['mask'] for s in segments if s['label'] in segment_labels]

    combined_mask = np.array(masks[0])
    for mask in masks:
        combined_mask += np.array(mask)

    combined_mask_img = Image.fromarray(combined_mask)

    if not include_face:
        combined_mask_img = mask_face(img.convert('RGB'), combined_mask_img)

    img.putalpha(combined_mask_img)

    return img, combined_mask_img

def apply_torso_segmentation(original_img):
    img = original_img.copy()
    segments = segmentation_model(img)

    torso_labels = ["Upper-clothes", "Dress", "Belt", "Face", "Left-arm", "Right-arm"]
    masks = [s['mask'] for s in segments if s['label'] in torso_labels]

    combined_mask = np.array(masks[0])
    for mask in masks:
        combined_mask += np.array(mask)

    combined_mask_img = Image.fromarray(combined_mask)
    combined_mask_img = mask_face(img.convert('RGB'), combined_mask_img)

    img.putalpha(combined_mask_img)

    return img, combined_mask_img
