import face_recognition
import cv2

def recognize():
    result = False

    # init videocam
    vc = cv2.VideoCapture(0)

    # load image to compare
    image = face_recognition.load_image_file('faces/user.jpg')

    # get face encoding
    known_face_encoding = face_recognition.face_encodings(image)

    # define counter
    counter = 0

    while True:
        # get single frame
        _, frame = vc.read()

        # resize frame for faster recognition
        small_frame = cv2.resize(frame, (0, 0), fx=0.5, fy=0.5)

        # convert frame from BGR (opencv) to RGB (face_recognition)
        rgb_small_frame = small_frame[:, :, ::-1]

        # detect face
        face_locations = face_recognition.face_locations(rgb_small_frame)
        face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

        for face_encoding in face_encodings:
            # find matches between encodings
            matches = face_recognition.compare_faces(known_face_encoding, face_encoding)

            if True in matches:
                index = matches.index(True)
                return not result

        # if can not detect face
        if counter > 200:
            return result

        counter += 1

# get image for encryption
def get_image():
    # init videocam
    vc = cv2.VideoCapture(0)

    # define counter
    counter = 0


    while True:
        # get single frame
        _, frame = vc.read()

        # convert frame from BGR (opencv) to RGB (face_recognition)
        rgb_frame = frame[:,:,::-1]

        # detect face
        face_locations = face_recognition.face_locations((rgb_frame))
        face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)


        # if face is detected save image
        if face_encodings:
            cv2.imwrite('faces/user.jpg', rgb_frame)
            break

        # if can not detect face for long time
        if counter > 200:
            return False

        counter += 1

    return True







