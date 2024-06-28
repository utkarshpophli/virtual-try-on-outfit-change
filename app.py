import streamlit as st
from PIL import Image
from virtual_try_on.try_on import virtual_try_on
from virtual_try_on.body_segmentation import apply_segmentation
from virtual_try_on.clothes_segmentation import segment_clothing

st.title("Virtual Try-On App")

st.sidebar.title("Upload Images")
person_image_file = st.sidebar.file_uploader("Upload a photo of the person", type=["jpg", "jpeg", "png"])
clothes_image_file = st.sidebar.file_uploader("Upload an image of the clothes", type=["jpg", "jpeg", "png"])

if person_image_file and clothes_image_file:
    person_image = Image.open(person_image_file).resize((512, 512)).convert('RGB')
    clothes_image = Image.open(clothes_image_file).resize((512, 512)).convert('RGB')
    
    st.image(person_image, caption="Person Image", use_column_width=True)
    st.image(clothes_image, caption="Clothes Image", use_column_width=True)
    
    st.write("Segmenting clothes...")
    seg_clothes_image = segment_clothing(image=clothes_image, clothing_items=["Hat", "Upper-clothes", "Skirt", "Pants", "Dress", "Belt", "Left-shoe", "Right-shoe", "Scarf"])
    
    st.write("Generating virtual try-on...")
    result_image = virtual_try_on(
        img=person_image,
        clothing=seg_clothes_image,
        prompt="photorealistic, perfect body, beautiful skin, realistic skin, natural skin",
        negative_prompt="ugly, bad quality, bad anatomy, deformed body, deformed hands, deformed feet, deformed face, deformed clothing, deformed skin, bad skin, leggings, tights, stockings, naked"
    )
    
    st.image(result_image, caption="Virtual Try-On Result", use_column_width=True)
else:
    st.write("Please upload both the person's photo and the clothing image.")

