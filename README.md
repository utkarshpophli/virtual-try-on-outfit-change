
# Virtual Try-On System

A virtual try-on system using inpainting techniques that allows users to upload a photo of a person and an image of clothing to generate a virtual try-on of the person wearing the clothes.


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
## Usage
Run the Streamlit app:
```
streamlit run app.py
```
## Results

![virtual_try_on_outfit_change\images\Results.png](https://github.com/utkarshpophli/virtual-try-on-outfit-change/blob/main/images/Results.png?raw=true)


## License



## Contact

If you have any questions or feedback, please contact [pophliutkarsh8@gmail.com].
