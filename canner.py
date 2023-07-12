import matplotlib.pyplot as plt
import cv2
from skimage import data
from skimage import exposure
from skimage.exposure import match_histograms
  
# loading data
reference =cv2.imread(r"C:\Users\hp\Downloads\reference.jpg")
reference_m = cv2.cvtColor(reference, cv2.COLOR_BGR2RGB)
image = cv2.imread(r"C:\Users\hp\Downloads\real.jpg")
image_m = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
  
# matching histograms
matched = match_histograms(image_m, reference_m, 
                          channel_axis=2,)
  
fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, 
                                    ncols=3, 
                                    figsize=(8, 3),
                                    sharex=True, 
                                    sharey=True)
for aa in (ax1, ax2, ax3):
    aa.set_axis_off()
  
# displaying images
ax1.imshow(image_m)
ax1.set_title('Source image')
ax2.imshow(reference_m)
ax2.set_title('Reference image')
ax3.imshow(matched)
ax3.set_title('Matched image')
  
plt.tight_layout()
plt.show()

#cv2.imread
