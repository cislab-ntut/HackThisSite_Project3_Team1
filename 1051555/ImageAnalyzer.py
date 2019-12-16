import cv2

img = cv2.imread('3.bmp')
print("type: ", type(img))
print("shape: ", img.shape)
counter = 0
print(img[0][0])

print("type=", type(img[1][1]))
whitePixel = [255, 255, 255]

for i in range(0, img.shape[0]):
    for j in range(0, img.shape[1]):
        for k in range(0, img.shape[2]):
            if img[i][j][k] != 62:
                print(img[i][j])
                img[i][j] = whitePixel
                j += 1
                counter += 1
cv2.imwrite('output.bmp', img)

print(counter)

