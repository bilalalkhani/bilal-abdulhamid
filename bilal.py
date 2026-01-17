import cv2
import numpy as np

def process_frame(frame, mode):
    if mode == 1:  # Grayscale
        return cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    elif mode == 2:  # Blur
        return cv2.GaussianBlur(frame, (15, 15), 0)

    elif mode == 3:  # Edge Detection
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        return cv2.Canny(gray, 50, 150)

    elif mode == 4:  # Invert colors
        return cv2.bitwise_not(frame)

    else:
        return frame


def image_mode():
    path = input("أدخل مسار الصورة: ")
    img = cv2.imread(path)

    if img is None:
        print("لم يتم تحميل الصورة!")
        return

    while True:
        print("""
اختر العملية:
1 - Grayscale
2 - Blur
3 - Edge Detection
4 - Invert Colors
0 - خروج
        """)
        choice = int(input("اختيارك: "))

        if choice == 0:
            break

        result = process_frame(img, choice)

        cv2.imshow("Original Image", img)
        cv2.imshow("Processed Image", result)

        cv2.waitKey(0)

    cv2.destroyAllWindows()


def video_mode():
    cap = cv2.VideoCapture(0)
    mode = 0

    print("""
اضغط:
1 - Grayscale
2 - Blur
3 - Edge Detection
4 - Invert Colors
0 - Original
q - خروج
    """)

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        processed = process_frame(frame, mode)
        cv2.imshow("Video Processing", processed)

        key = cv2.waitKey(1) & 0xFF

        if key == ord('q'):
            break
        elif key == ord('1'):
            mode = 1
        elif key == ord('2'):
            mode = 2
        elif key == ord('3'):
            mode = 3
        elif key == ord('4'):
            mode = 4
        elif key == ord('0'):
            mode = 0

    cap.release()
    cv2.destroyAllWindows()


def main():
    print("""
برنامج معالجة الصور باستخدام OpenCV
1 - تحميل صورة
2 - تشغيل كاميرا
    """)

    choice = int(input("اختيارك: "))

    if choice == 1:
        image_mode()
    elif choice == 2:
        video_mode()
    else:
        print("خيار غير صحيح")


main()
