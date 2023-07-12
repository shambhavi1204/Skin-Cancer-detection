# Skin-Cancer-detection
A model to classify skin cancer RGB images into malignant and benign
The modified VGG-16 architecture incorporates several important differences compared to the original model. Firstly, instead of using a softmax layer for classification, a sigmoid layer is employed, which enables multi-label prediction. Secondly, batch normalization is added after each convolutional layer activation, which helps stabilize and accelerate the training process. Thirdly, the flattening layer in the original VGG-16 is replaced with a global max pooling layer. This global max pooling layer is inspired by the global average pooling layer, as it reduces overfitting and allows labeling of tissues regardless of their spatial extent.

To further regularize the network and prevent overfitting, dropout is applied between the normalization and convolutional layers. The last two convolutional blocks and two fully-connected layers from the original VGG-16 are removed in this modified architecture.

The modified architecture consists of a single convolutional layer, followed by a ReLU activation layer and a batch normalization layer in each convolutional block. After the last convolutional block, batch normalization is added, followed by a global max pooling layer. A single fully-connected layer is then employed, followed by a sigmoid layer for the final prediction.

Preprocessinbg -Histogram Matching

Histogram matching is a technique used in image processing to align the histograms of two different images. It aims to make the histogram of one image match or resemble the histogram of another image.

The process involves adjusting the pixel intensities of an image to match the cumulative distribution function (CDF) of a reference image. By mapping the pixel intensities in this way, the overall contrast and brightness of the image can be adjusted to achieve a desired visual effect.

Histogram matching is commonly used in various applications, such as image enhancement, color correction, and image registration. It can be particularly useful in scenarios where images need to be visually consistent or when transferring characteristics from one image to another (e.g., applying the color style of a reference image to a target image).
