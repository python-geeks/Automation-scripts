import cv2
import numpy as np
from PIL import Image
from skimage.metrics import structural_similarity as ssim
from skimage.restoration import denoise_nl_means, estimate_sigma
from skimage import img_as_ubyte, img_as_float

class ImageProc:
    Image.MAX_IMAGE_PIXELS = None

    def pre_processing(imageA, imageB):
        def uniform_dim(imageA, imageB):
            h1, w1 = imageA.shape
            h2, w2 = imageB.shape
            if (h1 != h2) or (w1 != w2):
                imageA = cv2.resize(imageA, (min(w1,w2), min(h1,h2)))
                imageB = cv2.resize(imageB, (min(w1,w2), min(h1,h2)))
            return imageA, imageB

        def de_noise(img):
            float_img = img_as_float(img)
            sigma_est = np.mean(estimate_sigma(float_img, multichannel=True))
            denoise_img = denoise_nl_means(float_img, h=1.15 * sigma_est, fast_mode=True, 
                                           patch_size=5, patch_distance=3, multichannel=True)                               
            return img_as_ubyte(denoise_img)
            
        # noise removal
        imageA = de_noise(imageA)
        imageB = de_noise(imageB)
        
        #clr to grey
        imageA = cv2.cvtColor(imageA, cv2.COLOR_BGR2GRAY)
        imageB = cv2.cvtColor(imageB, cv2.COLOR_BGR2GRAY)
        
        #edge detetction
        imageA = cv2.Canny(imageA, 100, 200)
        imageB = cv2.Canny(imageB, 100, 200)
        
        #uniform dimensions
        imageA, imageB = uniform_dim(imageA, imageB)
        
        """
        #sharpening the images
        kernel = np.array([ [-1,-1,-1],
                            [-1,5,-1],
                            [-1,-1,-1] ])
        imageA = cv2.filter2D(imageA, -1, kernel)
        imageB = cv2.filter2D(imageB, -1, kernel)
        """
        return (imageA, imageB)

    def compare(imageA, imageB):   
        #Structural Similarity Index from skimage
        s = ssim(imageA, imageB, multichannel=True)

        #Mean Sqaure Error 
        m = np.sum((imageA.astype("float") - imageB.astype("float")) ** 2)
        m /= float(imageA.shape[0] * imageA.shape[1])
        
        #Histogram Difference using numpy.histogram
        diff =0.0
        h1,b1 = np.histogram(imageA)
        h2,b2 = np.histogram(imageB)        
        for i in range(len(h1)):
          diff += abs(h1[i] - h2[i])
        maxSum = max(h1.sum(), h2.sum())
        return (s, m, diff/(2*maxSum))
        