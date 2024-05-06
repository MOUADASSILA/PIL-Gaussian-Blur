#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon May  6 11:46:49 2024

@author: mac
"""
from PIL import Image, ImageFilter

new_image_path = "/Users/mac/Downloads/original.png"
new_original_image = Image.open(new_image_path)

# Corrected the typo in variable name from 'guassian_chihaja_image' to 'gaussian_chihaja_image'
gaussian_chihaja_image = new_original_image.filter(ImageFilter.GaussianBlur(radius=2))

gaussian_chihaja_image_path = "pil_gaussian_chihaja_image.png"
gaussian_chihaja_image.save(gaussian_chihaja_image_path)
