
import cv2

# Open default webcam
cap = cv2.VideoCapture(0)

while True:
    ok, frame = cap.read()

    if not ok:
        print("Could not access camera!")
        break

    # Mirror the camera image
    frame = cv2.flip(frame, 1)

    # Display camera feed
    cv2.imshow("Camera test (press q to quit)", frame)

    # Press q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release camera and close windows
cap.release()
cv2.destroyAllWindows()
