import cv2
from pyzbar.pyzbar import decode

# Initialize the camera
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Decode QR codes in the frame
    decoded_objects = decode(frame)

    # Iterate over all detected QR codes
    for obj in decoded_objects:
        # Draw a rectangle around the QR code
        points = obj.polygon
        if len(points) == 4:
            cv2.polylines(frame, [points], True, (0, 255, 0), 2)

        # Get the QR code's decoded text
        qr_data = obj.data.decode('utf-8')
        qr_type = obj.type
        qr_bounds = obj.polygon

        # Print the decoded information
        print(f'Type: {qr_type}, Data: {qr_data}')

    # Display the frame with detected QR codes
    cv2.imshow("QR Code Scanner", frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()
