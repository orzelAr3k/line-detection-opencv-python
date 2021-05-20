# line-detection-opencv-python

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install opencv-python.

```bash
pip install opencv-python
```
Set up the environment.
```bash
conda env create -f environment.yml
```

To activate the environment:

Window: ```bash
        conda activate carnd```

Linux, MacOS: ```bash  
                source activate carnd```


### 1. Gaussian Blur
Used to reduce noise and smoothen out the image. We generally use a kernel of some specific size(say 5x5) and a deviation

![Gradient](https://i.ibb.co/zNNtJYp/Gradient.png)

The above image shows a **Strong gradient** on the left and a **Weak Gradient** on the right.

Gradient : Change in brightness over a series of pixels.
### 2. Canny Edge Detection
As the name suggests, it is an algorithm to detect edges in our image.
A change in intensity of pixels will give us an edge.

Small change will imply small change in intensity whereas a Large derivative is a large change. 

```python
cv2.Canny(image,low_threshold,high_threshhold)
```

If a gradient is larger than the **high_threshold**, then it is accepted as an edge pixel. If it is below the **low_threshold**, it is rejected. Always use a ratio of 1:3 or 1:2.

**NOTE : Line 34 in the code is optional and can be omitted, since the Canny function automaticallyapplies a Gaussian Blur with a kernel of 5x5.**

Example : 
```python
cv2.Canny(image,50,150)
```

### 3. Hough Transform
After we have successfully detected edges in our image, it's time to detect lane lines in our image, for which we can use the Hough transform.

Before that, we need to find the **Region on interest** in our image. For that, we use Matplotlib to get a fair enough idea about the coordinate values of the image. <br>
Once we are done, we create a mask with a polygon over it as shown :
![Mask](https://i.ibb.co/DrLNSJR/Mask.png)

0000 represents the black pixels and 11111111 represents the white pixels, denoting the polygon. Now, we apply the **bitwise_and** in the original image and the mask to obtain the **masked_image**, which essentially will contain only the region on interest.

![Masked Image](https://i.ibb.co/LJFykXC/Masked-Image.png)  
### Ultimate Result <br>
![Final Masked Image](https://i.ibb.co/711SBhW/Final-Masked-Image.png)

Finally, now when we have only the Region of interest in our image, we will use Hough Transform to detect Straight lines in our image. 


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)