
# Virtual Try-On System

This project presents a virtual try-on system that uses inpainting techniques to generate realistic images of users wearing selected clothing items. Users can upload a photo of themselves and an image of a clothing item, and the system will produce a composite image showing the user wearing the selected clothing.

### Key features:

* Easy upload of user photos and clothing images
* Advanced inpainting for realistic clothing integration
* Quick generation of virtual try-on results

Try out the live demo [here](https://huggingface.co/spaces/utkarshpophli/virtual-try-on-outfit-change) to experience the virtual try-on system in action!

## Directory Structure

```
|- notebooks/
   |- data_preparation.ipynb
   |- model_evaluation.ipynb
   |- model_training.ipynb
|- images/
   |- results.png
|- virtual_try_on/
   |- __init__.py
   |- utils.py
   |- body_segmentation.py
   |- clothes_segmentation.py
   |- data.py
   |- try_on.py
|- README.md
|- app.py
|- requirements.txt
|- setup.py
```
## Installation

1. Clone the Repository:
```
git clone https://github.com/your-username/virtual-try-on.git
cd virtual-try-on
```

2. Create and Activate Conda Environment:
```
conda env create -f environment.yml
conda activate virtual-try-on
```
3. Install the Package:
```
pip install -e .
```

## Results

![virtual_try_on_outfit_change\images\Results.png](https://github.com/utkarshpophli/virtual-try-on-outfit-change/blob/main/images/Results.png?raw=true)

## Usage
Run the Streamlit app:
```
streamlit run app.py
```

## How to Use

1. Upload a photo of a person.
2. Upload an image of the clothing item you want to try on.
3. The system will process the images and generate a virtual try-on result.
4. View the output image showing the person wearing the selected clothing.


## License

This project is licensed under the MIT License.

## Contact

If you have any questions or feedback, please contact [pophliutkarsh8@gmail.com].
