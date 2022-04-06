import cv2
import mediapipe as mp

class processer:
    @classmethod
    def holistic(cls, image):
        mp_detector = mp.solutions.holistic
        detector = mp_detector.Holistic(
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5,
            enable_segmentation=True,
            refine_face_landmarks=True
        )
        results = detector.process(image)
        mp.solutions.drawing_utils.draw_landmarks(
            image,
            results.pose_landmarks,
            mp_detector.POSE_CONNECTIONS,
            landmark_drawing_spec=mp.solutions.drawing_styles
                .get_default_pose_landmarks_style())
        print(results.pose_landmarks.landmark[mp_detector.PoseLandmark.NOSE] if results.pose_landmarks else None)

    @classmethod
    def face_mesh(cls, image):
        mp_detector = mp.solutions.face_mesh
        detector = mp_detector.FaceMesh(
            max_num_faces=1,
            refine_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        results = detector.process(image)
        if results.multi_face_landmarks:
            for face_landmarks in results.multi_face_landmarks:
                mp.solutions.drawing_utils.draw_landmarks(
                    image,
                    face_landmarks,
                    mp_detector.FACEMESH_TESSELATION,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp.solutions.drawing_styles
                        .get_default_face_mesh_tesselation_style())
                mp.solutions.drawing_utils.draw_landmarks(
                    image,
                    face_landmarks,
                    mp_detector.FACEMESH_CONTOURS,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp.solutions.drawing_styles
                        .get_default_face_mesh_contours_style())
                mp.solutions.drawing_utils.draw_landmarks(
                    image,
                    face_landmarks,
                    mp_detector.FACEMESH_IRISES,
                    landmark_drawing_spec=None,
                    connection_drawing_spec=mp.solutions.drawing_styles
                        .get_default_face_mesh_iris_connections_style()
                )

cameraid = "http://192.168.2.112:4747/video"
cap = cv2.VideoCapture(cameraid)
while cap.isOpened():
    success, image = cap.read()
    if not success:
        continue
    processer.holistic(image)
    # processer.face_mesh(image)
    # mp_drawing.draw_landmarks(image, results.left_hand_landmarks, mp_holistic.HAND_CONNECTIONS)
    # mp_drawing.draw_landmarks(image, results.right_hand_landmarks, mp_holistic.HAND_CONNECTIONS)

    cv2.imshow("pose", cv2.flip(image, 1))

    if cv2.waitKey(5) & 0xFF == 27:
      break
cap.release()