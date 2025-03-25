## 📌 목차

- [진행 사항](#진행-사항)
- [KITTI GIF 출력 결과 (전체)](#kitti-gif출력-결과모든-오브젝트-포함)
- [KITTI GIF 출력 결과 (보행자)](#kitti-gif출력-결과보행자만)
- [이미지 데이터 시각화](#이미지-데이터-시각화left-img---p2)
- [라이다 데이터 시각화](#라이다-데이터-시각화)
- [라이다와 카메라 캘리브레이션](#라이다-데이터와-카메라-켈리브레이션-통해-이미지에서-라이다-정보-가져오기)
- [YOLO-Pose 결과](#yolo-pose-와-그냥-yolo-kitti-데이터셋)
- [YOLO 베이스라인](#욜로-베이스-라인-잡아둠아직-미공개)


## 진행 사항
1. 각 데이터 별 시각화
2. 이미지, 라이다 정보를 사용하여 실제 좌표 체크

## KITTI GIF출력 결과(모든 오브젝트 포함)

<table>
  <tr>
    <td align="center">
      <img src="outputM/kitti_0000_topview.gif" width="300"/><br/>
      <p>kitti_0000_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputM/kitti_0001_topview.gif" width="300"/><br/>
      <p>kitti_0001_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputM/kitti_0002_topview.gif" width="300"/><br/>
      <p>kitti_0002_topview.gif</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="outputM/kitti_0003_topview.gif" width="300"/><br/>
      <p>kitti_0003_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputM/kitti_0004_topview.gif" width="300"/><br/>
      <p>kitti_0004_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputM/kitti_0005_topview.gif" width="300"/><br/>
      <p>kitti_0005_topview.gif</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="outputM/kitti_0006_topview.gif" width="300"/><br/>
      <p>kitti_0006_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputM/kitti_0007_topview.gif" width="300"/><br/>
      <p>kitti_0007_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputM/kitti_0008_topview.gif" width="300"/><br/>
      <p>kitti_0008_topview.gif</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="outputM/kitti_0009_topview.gif" width="300"/><br/>
      <p>kitti_0009_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputM/kitti_0010_topview.gif" width="300"/><br/>
      <p>kitti_0010_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputM/kitti_0011_topview.gif" width="300"/><br/>
      <p>kitti_0011_topview.gif</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="outputM/kitti_0012_topview.gif" width="300"/><br/>
      <p>kitti_0012_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputM/kitti_0013_topview.gif" width="300"/><br/>
      <p>kitti_0013_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputM/kitti_0014_topview.gif" width="300"/><br/>
      <p>kitti_0014_topview.gif</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="outputM/kitti_0015_topview.gif" width="300"/><br/>
      <p>kitti_0015_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputM/kitti_0016_topview.gif" width="300"/><br/>
      <p>kitti_0016_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputM/kitti_0017_topview.gif" width="300"/><br/>
      <p>kitti_0017_topview.gif</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="outputM/kitti_0018_topview.gif" width="300"/><br/>
      <p>kitti_0018_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputM/kitti_0019_topview.gif" width="300"/><br/>
      <p>kitti_0019_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputM/kitti_0020_topview.gif" width="300"/><br/>
      <p>kitti_0020_topview.gif</p>
    </td>
  </tr>
</table>

## KITTI GIF출력 결과(보행자만)

<table>
  <tr>
    <td align="center">
      <img src="outputP/kitti_0000_topview.gif" width="300"/><br/>
      <p>kitti_0000_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputP/kitti_0001_topview.gif" width="300"/><br/>
      <p>kitti_0001_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputP/kitti_0002_topview.gif" width="300"/><br/>
      <p>kitti_0002_topview.gif</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="outputP/kitti_0003_topview.gif" width="300"/><br/>
      <p>kitti_0003_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputP/kitti_0004_topview.gif" width="300"/><br/>
      <p>kitti_0004_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputP/kitti_0005_topview.gif" width="300"/><br/>
      <p>kitti_0005_topview.gif</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="outputP/kitti_0006_topview.gif" width="300"/><br/>
      <p>kitti_0006_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputP/kitti_0007_topview.gif" width="300"/><br/>
      <p>kitti_0007_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputP/kitti_0008_topview.gif" width="300"/><br/>
      <p>kitti_0008_topview.gif</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="outputP/kitti_0009_topview.gif" width="300"/><br/>
      <p>kitti_0009_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputP/kitti_0010_topview.gif" width="300"/><br/>
      <p>kitti_0010_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputP/kitti_0011_topview.gif" width="300"/><br/>
      <p>kitti_0011_topview.gif</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="outputP/kitti_0012_topview.gif" width="300"/><br/>
      <p>kitti_0012_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputP/kitti_0013_topview.gif" width="300"/><br/>
      <p>kitti_0013_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputP/kitti_0014_topview.gif" width="300"/><br/>
      <p>kitti_0014_topview.gif</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="outputP/kitti_0015_topview.gif" width="300"/><br/>
      <p>kitti_0015_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputP/kitti_0016_topview.gif" width="300"/><br/>
      <p>kitti_0016_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputP/kitti_0017_topview.gif" width="300"/><br/>
      <p>kitti_0017_topview.gif</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="outputP/kitti_0018_topview.gif" width="300"/><br/>
      <p>kitti_0018_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputP/kitti_0019_topview.gif" width="300"/><br/>
      <p>kitti_0019_topview.gif</p>
    </td>
    <td align="center">
      <img src="outputP/kitti_0020_topview.gif" width="300"/><br/>
      <p>kitti_0020_topview.gif</p>
    </td>
  </tr>
</table>

## 이미지 데이터 시각화(left img - p2)

<div align="center">
  <p>imgoutput.gif[용량때문에 이미지 사이즈 절반]</p>
  <img src="imgoutput.gif" width="600"/><br/>
</div>

## 라이다 데이터 시각화

<div align="center">
  <p>lidar_animation.gif </p>
  <img src="lidar_animation.gif" width="600"/><br/>
</div>

## 라이다 데이터와 카메라 켈리브레이션 통해 이미지에서 라이다 정보 가져오기
<img width="800" alt="image" src="https://github.com/user-attachments/assets/4d946b98-302c-4a1b-ae7a-de60990847c0" />

## yolo-pose 와 그냥 yolo kitti 데이터셋
<table>
  <tr>
    <td align="center">
      <img src="yolov8x.png" width="300"/><br/>
      <p>yolo v8x pose</p>
    </td>
    <td align="center">
      <img src="yolov8x-p6.png" width="300"/><br/>
      <p>yolo v8x p6 pose</p>
    </td>
    <td align="center">
      <img src="yolo11x.png" width="300"/><br/>
      <p>yolo v11x pose</p>
    </td>
  </tr>
  <tr>
    <td align="center">
      <img src="yolo11n.png" width="300"/><br/>
      <p>yolo v11n </p>
    </td>
  </tr>
</table>

## 욜로 베이스 라인 잡아둠.(아직 미공개)

대략 구조 공개
<table>
  <img width="200" alt="image" src="https://github.com/user-attachments/assets/8406081e-d696-45ef-929d-644d2e49dd49" />
</table>
