import cv2
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
##First CROP
img_raw=cv2.imread("cancha.jpg")
img_raw = cv2.resize(img_raw, (416, 416))
roi = cv2.selectROI(img_raw)
roi_cropped=img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
a, b , c, d = int(roi[1]),int(roi[1]+roi[3]), int(roi[0]),int(roi[0]+roi[2])
print(f"Puntos de mostrador 1 : {[a,b,c,d]}")
cv2.imshow("ROI",roi_cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
##Second CROP
img_raw=cv2.imread("cancha.jpg")
img_raw = cv2.resize(img_raw, (416, 416))
roi = cv2.selectROI(img_raw)
roi_cropped_1=img_raw[int(roi[1]):int(roi[1]+roi[3]), int(roi[0]):int(roi[0]+roi[2])]
#a, b , c, d = int(roi[1]),int(roi[1]+roi[3]), int(roi[0]),int(roi[0]+roi[2])
#print([a,b,c,d])
cv2.imshow("ROI",roi_cropped_1)
cv2.waitKey(0)
cv2.destroyAllWindows()
## First CROP Analysis
crop_array = np.array([roi_cropped,roi_cropped_1])
myimg = roi_cropped
avg_color_per_row = np.average(myimg, axis=0)
avg_color = np.average(avg_color_per_row, axis=0)
## Second CROP Analysis
myimg = roi_cropped_1
avg_color_per_row = np.average(myimg, axis=0)
avg_color_1 = np.average(avg_color_per_row, axis=0)

df = pd.DataFrame(np.array([avg_color,avg_color_1]),columns=["b","g","r"])

print(df)
import seaborn as sns
sns.set()

plt.subplot(1, 2, 1)
plt.title("Mostrador 1")
df.iloc[0].plot(kind='bar',color=["blue","green","red"])
plt.ylim(top=255)
plt.subplot(1, 2, 2)
plt.title("Mostrador 2")
df.iloc[1].plot(kind='bar',color=["blue","green","red"])
plt.ylim(top=255)
plt.show()
