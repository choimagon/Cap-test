import cv2
import numpy as np
import glob
import os

# KITTI 캘리브레이션 파일 읽기
def read_calib_file(filepath):
    with open(filepath, 'r') as f:
        lines = f.readlines()
    P0_line = [line for line in lines if line.startswith('P0:')][0]
    P0 = np.array(list(map(float, P0_line.strip().split()[1:]))).reshape(3, 4)
    K = P0[:, :3]  # Intrinsic matrix
    return K

# SIFT + BFMatcher + RANSAC VO 함수
def estimate_motion(img1, img2, K):
    sift = cv2.SIFT_create()

    kp1, des1 = sift.detectAndCompute(img1, None)
    kp2, des2 = sift.detectAndCompute(img2, None)

    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    pts1 = np.float32([kp1[m.queryIdx].pt for m in matches])
    pts2 = np.float32([kp2[m.trainIdx].pt for m in matches])

    E, mask = cv2.findEssentialMat(pts1, pts2, K, method=cv2.RANSAC, prob=0.999, threshold=1.0)
    _, R, t, mask_pose = cv2.recoverPose(E, pts1, pts2, K)

    return R, t

# KITTI 폴더 경로
seq = '05'
dataset_dir = '/path/to/KITTI/sequences/'  # <-- 본인 폴더에 맞게 수정
img_dir = os.path.join(dataset_dir, seq, 'image_0')
calib_file = os.path.join(dataset_dir, seq, 'calib.txt')

# 이미지 경로 로드
img_paths = sorted(glob.glob(os.path.join(img_dir, '*.png')))

# 캘리브레이션 읽기
K = read_calib_file(calib_file)
print("Intrinsic K:\n", K)

# VO & 속도 추정 시작
fps = 10
delta_time = 1 / fps

for i in range(len(img_paths)-1):
    img1 = cv2.imread(img_paths[i], cv2.IMREAD_GRAYSCALE)
    img2 = cv2.imread(img_paths[i+1], cv2.IMREAD_GRAYSCALE)

    R, t = estimate_motion(img1, img2, K)

    # 상대 이동 방향
    delta_t_vector = t.ravel()  # scale은 현재 없음 (scale unknown)

    # 속도 방향만 출력 (scale 없이 방향만)
    velocity_direction = delta_t_vector / delta_time
    direction_norm = np.linalg.norm(velocity_direction)

    print(f"Frame {i} -> {i+1}")
    print("Translation (normalized):", delta_t_vector)
    print("Velocity direction:", velocity_direction)
    print("Direction norm (m/s if scale known):", direction_norm)
    print("-" * 50)
