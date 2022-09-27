#! /usr/bin/env python
# -*- coding: utf-8 -*-

# Python標準ライブラリ
import cv2
from cv_bridge import CvBridge, CvBridgeError

# Python追加ライブラリ
import mediapipe as mp

# ROSに関するライブラリ
import rospy
from sensor_msgs.msg import CompressedImage


class HandDetection():
    def __init__(self):
        # MediaPipeが提供しているhandsの値を読み込む
        self.mp_hands = mp.solutions.hands
        self.mp_drawing = mp.solutions.drawing_utils
        self.mesh_drawing_spec = self.mp_drawing.DrawingSpec(thickness=2, color=(0, 255, 0))
        self.mark_drawing_spec = self.mp_drawing.DrawingSpec(thickness=3, circle_radius=3, color=(0, 0, 255))
        self.cv_bridge = CvBridge()
        self.sub = rospy.Subscriber("/hsrb/head_rgbd_sensor/rgb/image_rect_color/compressed", CompressedImage, self.main)

    def main(self, msg):
        observed_img = self.cv_bridge.compressed_imgmsg_to_cv2(msg)
        image = cv2.resize(observed_img, dsize=None, fx=0.3, fy=0.3)
        # 色変換（BGR→RGB）
        rgb_image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        # リサイズ
        height = rgb_image.shape[0]
        width = rgb_image.shape[1]

        # 検出結果を別の画像名としてコピーして作成
        self.annotated_image = image.copy()

        # 認識する手の数と認識精度を設定する (手の数の上限、検出精度、ランドマーク検出)
        with self.mp_hands.Hands(max_num_hands=2, min_detection_confidence=0.5,
                                 static_image_mode=True) as hands_detection:

            # 顔検出の結果をresultsに
            results = hands_detection.process(rgb_image)

            for hand_landmarks in results.multi_hand_landmarks:
                self.mp_drawing.draw_landmarks(
                    image=self.annotated_image,
                    landmark_list=hand_landmarks,
                    connections=self.mp_hands.HAND_CONNECTIONS,
                    landmark_drawing_spec=self.mark_drawing_spec,
                    connection_drawing_spec=self.mesh_drawing_spec
                )
                self.save_data(self.annotated_image)
                cv2.imshow('Detection Result', self.annotated_image)
                cv2.waitKey(1)


    def save_data(self, img):
        cv2.imwrite('../data/result_ros.jpg', img)
        return


if __name__ == "__main__":
    rospy.init_node('mediapipe_ros')
    mediapipe_ros = HandDetection()
    rospy.spin()
