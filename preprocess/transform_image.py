import cv2
import os
import numpy as np


def transform(image_path,dest_dir):
    """
    Creates multiple versions of the same image and stores them in the dataset folder.
    First grayscales the image
    Then creates 6 rotated images, 3 for the original one and 3 for the grayscaled image
    The rotation are performed around the center
    with angles of 90deg, 180deg, 270deg

    In the end, the final dataset, built as explained, will contain 8 version of the same image
    """
    #load the image
    image = cv2.imread(image_path)
    #get the image name and saves it
    name = os.path.basename(os.path.normpath(image_path))
    cv2.imwrite(dest_dir+'/'+name, image)

    #converts the original image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(dest_dir+'/gray'+name,gray)

    #get the centre of the image (to rotate around it)
    height, width = image.shape[:2]

    for i in range(1,4):
        #set the rotation matrix
        angle = i*90
        rotation_matrix = cv2.getRotationMatrix2D((width/2, height/2), angle,1)

        #get the cos and sin to determine the rotated image dimension
        cos = np.abs(rotation_matrix[0, 0])
        sin = np.abs(rotation_matrix[0, 1])

        # compute the new bounding dimensions of the image
        nW = int((height * sin) + (width * cos))
        nH = int((height * cos) + (width * sin))

        #adjust the rotation matrix
        rotation_matrix[0, 2] += (nW / 2) - width/2
        rotation_matrix[1, 2] += (nH / 2) - height/2

        #creates the rotated images
        rotated_image = cv2.warpAffine(image, rotation_matrix, (nW,nH))
        rotated_grayscaled_image = cv2.warpAffine(gray, rotation_matrix, (nW,nH))
        #save the images
        cv2.imwrite(dest_dir+'/'+ str(angle)+ name, rotated_image )
        cv2.imwrite(dest_dir+'/'+ str(angle)+'gray'+ name, rotated_grayscaled_image )
