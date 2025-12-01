import cv2
from cvzone.HandTrackingModule import HandDetector

# 제스처별로 보여줄 이미지들
img_v = cv2.imread("Bears/v_image.jpeg")
img_middle = cv2.imread("Bears/middle_image.jpg")
img_highfive = cv2.imread("Bears/highfive_image.jpg")

# 이미지 로드 확인용 로그
if img_v is None:
    print("v_image.jpeg 를 찾을 수 없습니다.")
if img_middle is None:
    print("middle_image.jpg 를 찾을 수 없습니다")
if img_highfive is None:
    print("highfive_image.jpg 를 찾을 수 없습니다")

# 웹캠 / 손 인시 세팅
cap = cv2.VideoCapture(0) # 0은 기본웹캠
cap.set(3, 1280) # width
cap.set(4, 720) # height

detector = HandDetector(
    detectionCon=0.7, # 감지 confidence
    maxHands = 1 # 한손만 인식 일단
)

def classify_gesture(fingers): 
    """ 
    손꾸락 : [thumb, index, middle, ring, pinky] (각각 0 or 1)
    return : '브이', '빠큐', '하이파이브', 'None'
    """
    t, i, m, r, p = fingers

    # 하이파이브 = 손가락 다 펴짐
    if [t, i, m, r, p] == [1, 1, 1, 1, 1]:
        return "HIGHFIVE"
    # 브이 = 검지/중지 만 펴짐, 약지/새끼 접음 (엄지 상관 X)
    if i == 1 and m == 1 and r == 0 and p == 0:
        return "V"
    # 빠큐 = 중지만 펴고, 나머지 다 접음
    if i == 0 and m == 1 and r == 0 and p == 0:
        return "MIDDLE"
    
    return "NONE"
    # 나중에 다 호출할거니까 대문자로 구분하기 쉽구로

while True:
    success, img = cap.read()
    if not success:
        print("웹캠에서 영상을 읽을 수 없음")
        break

    # 좌우반전 이거 때문에... 띠발
    img = cv2.flip(img, 1)

    # 손 인식 
    hands, img = detector.findHands(img)

    gesture = "NONE" #기본

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand) # [thumb, index, middle, ring, pinky]
        gesture = classify_gesture(fingers)

    cv2.putText(
        img,
        f"Gesture: {gesture}",
        (30, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1.2,
        (0, 255, 0),
        2,
        cv2.LINE_AA
    )

    #제스처에 따라 이미지 오버레이(곰)
    overlay = None
    if gesture == "V":
        overlay = img_v
    elif gesture == "MIDDLE":
        overlay = img_middle
    elif gesture == "HIGHFIVE":
        overlay = img_highfive
    
    if overlay is not None:
        oh, ow, _ = overlay.shape
        h, w, _ = img.shape

        #이미지가 너무 큼 (최대 250px)
        max_size = max(oh, ow)
        scale = 250 / max_size
        new_w = int(ow * scale)
        new_h = int(oh * scale)

        resized = cv2.resize(overlay, (new_w, new_h))

        x1 = w - new_w - 20
        y1 = 20
        x2 = x1 + new_w
        y2 = y1 + new_h
    
        img[y1:y2, x1:x2] = resized

    cv2.imshow("cvzone Hand Gesture Demo", img)

    key = cv2.waitKey(1)
    if key == 27: #ESC 눌러 종료
        break

cap.release()
cv2.destroyAllWindows
