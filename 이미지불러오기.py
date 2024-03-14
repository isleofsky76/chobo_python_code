from PIL import Image 

# 이미지 열기
img = Image.open(r"C:\Users\isleo\OneDrive\Desktop\1 컴퓨터배우기\이미지를 text로 변환하기\p1.jpg")

# 결과출력하기
print(img.format, img.size, img.mode)
#결과 : JPEG (370, 220) RGB

# 이미지 보기
img.show()
