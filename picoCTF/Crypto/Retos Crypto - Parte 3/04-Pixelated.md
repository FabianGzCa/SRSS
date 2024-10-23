## Objetivo
I have these 2 images, can you make a flag out of them? [scrambled1.png](https://mercury.picoctf.net/static/6e4afb967ef8c865f79f3a8cd7767cca/scrambled1.png) [scrambled2.png](https://mercury.picoctf.net/static/6e4afb967ef8c865f79f3a8cd7767cca/scrambled2.png)

## Solución
Instalamos el módulo de python `pip install PIL --break-system-packages`
Utilizamos el siguiente código de python para fusionar las imágenes:
```python
from PIL import Image  
  
def combine_images(image1_path, image2_path, output_path):  
    # Open the images  
    image1 = Image.open(image1_path)  
    image2 = Image.open(image2_path)  
  
    # Ensure both images have the same size  
    if image1.size != image2.size:  
        raise ValueError("Images must have the same size")  
  
    # Combine the images using a simple averaging technique  
    combined_image = Image.blend(image1, image2, alpha=0.5)  
  
    # Save the combined image  
    combined_image.save(output_path)  
  
if __name__ == "__main__":  
    # Provide the paths of the input images and the desired output path  
    image1_path = "scrambled1.png"  
    image2_path = "scrambled2.png"  
    output_path = "combined_image.png"  
  
    combine_images(image1_path, image2_path, output_path)
```

Nos da la imágen real, la subimos a https://29a.ch/photo-forensics/#luminance-gradient y modificando los valores nos termina mostrando la flag dentro de la imágen
picoCTF{0542dc1d}
## Notas Adicionales


## Referencias
https://29a.ch/photo-forensics/#luminance-gradient