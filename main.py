pip install torch-dreamsAlso 
pip install ipywidgets

import web
import talib
from pandasgui import show
import #other required packages
import a pre-trained vision-based model to visualize the internal features.
import inception v3 model.
import numpy as np
import matplotlib.pyplot as plt
from torch_dreams.dreamer import dreamer
import torchvision.models as models



#Load data

load timeseries(asset)



#Importing the model
model = models.inception_v3(pretrained=True)

dreamy_boi = dreamer(model, device = 'cuda', quiet =  False)

#Displaying the layer image
image_param = dreamy_boi.render(
layers = [model.Mixed_5d],
)
plt.imshow(image_param)
plt.show()

#############With your own features############


from torch_dreams.custom_image_param import custom_image_param

my_custom_func = make_custom_func(layer_number = 0, channel_number = 19)
layers_to_use = [model.Mixed_6d]

param = custom_image_param(filename = 'animals.jpg', device= 'cuda')

image_param = dreamy_boi.render(
    image_parameter= param,
    layers = [model.Mixed_6d],
    lr = 2e-4,
    grad_clip = 0.1,
    weight_decay= 1e-1,
    iters = 120
)

import cv2
fig, ax = plt.subplots(nrows= 1, ncols= 2, figsize=(10,5))
ax.flat[0].imshow(cv2.cvtColor(cv2.imread('animals.jpg'), cv2.COLOR_BGR2RGB))
ax.flat[1].imshow(image_param)


######Customize the DATAFRAME  height & width using additional parameters########

layers_to_use = [model.Mixed_6b.branch1x1.conv]

def make_custom_func(layer_number = 0, channel_number= 0): 
    def custom_func(layer_outputs):
        loss = layer_outputs[layer_number][channel_number].mean()
        return -loss
    return custom_func
    
my_custom_func = make_custom_func(layer_number= 0, channel_number = 110)
    
image_param = dreamy_boi.render(
    layers = layers_to_use,
    custom_func = my_custom_func,width=512,height=512
    iters = 200
)
plt.imshow(image_param)
plt.axis('off')
plt.savefig("modified_art1.jpg", dpi=1500,, bbox_inches='tight')
plt.show()
