from PIL import Image

# 이미지 파일 경로
image_path = r'C:\Users\isleo\OneDrive\Desktop\1 컴퓨터배우기\이미지를 text로 변환하기\p1.jpg'

# 이미지 저장할 새로운 경로와 파일명
save_path = r'C:\Users\isleo\OneDrive\Desktop\1 컴퓨터배우기\이미지를 text로 변환하기\new_image.jpg'

# 이미지 열기
with Image.open(image_path) as img:
    # 여기서 이미지에 대한 변형 작업을 수행할 수 있음
    # 예: img = img.rotate(90) # 이미지를 90도 회전

    # 이미지 저장
    img.save(save_path)

print(f'Image saved as {save_path}')
