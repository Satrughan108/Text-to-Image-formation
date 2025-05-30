# -*- coding: utf-8 -*-
"""Text to image formation

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1zkaz5R8c68xQDh2fGJJ2NDV5Fyk5rzRa
"""

!pip install diffusers transformers accelerate torch

from diffusers import StableDiffusionPipeline
import torch

# Check for GPU availability
device = 'cuda' if torch.cuda.is_available() else 'cpu'
print(f'Using device: {device}')

## Load the Stable Diffusion model
def load_model():
    global stable_pipe
    stable_pipe = StableDiffusionPipeline.from_pretrained(
        'runwayml/stable-diffusion-v1-5', torch_dtype=torch.float16
    ).to(device)
    print('Model loaded successfully')

load_model()

## Generate Image Function
def generate_image(prompt):
    image = stable_pipe(prompt).images[0]
    return image

# Example usage
prompt = 'A futuristic cityscape with flying cars'
image = generate_image(prompt)
image.show()

