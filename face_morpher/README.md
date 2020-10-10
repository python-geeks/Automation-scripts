# Face-Morphing

The script is used to do face morphing of 3 famous USA Presidents by creating a small gif converting one face to another (One can use Delaunay triangulation+ Warp affine and cv2
module for this.The visuals of the script is being provided below , The steps or the approach the script is following is mentioned below : 
```
Step1 : First Download the script 
Step2 : Or you can directly clone the script from here
Step3 : Then directly input your images from this section : 
          if __name__ == '__main__':
    filename1 = r"C:\Users\Anustup\Desktop\Facemorph\hilary_clinton.jpg"
    filename2 = r"C:\Users\Anustup\Desktop\Facemorph\ted_cruz.jpg"
    alpha = 0.5
Step 4 : You can directly add your image files here 
Step 5 : Now simply add some TXT files that have facial landmarks , you can use any prebuild data sets or any online source to extract txt files for extarcting the landmarks
Step 6 : Simply add that TXT files to it 
Step 7 : Run the Script you can see the Output 
```
You can see your output in a pop uped window . 

### How to Run the Script : 

To run the script use the following command line : 
```
python run requirements.txt
```
Or you can use pip or conda command to do so : 
```
pip install sys numpy cv2
conda install sys numpy cv2
```
### Output : 

Here you can see what are the input images in one side and out put face morphed image on the other side 

![alt text](https://github.com/Anustup900/Automation-scripts/blob/main/facemorphing/Assets/abc.PNG)
