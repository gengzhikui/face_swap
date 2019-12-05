# -*- coding: utf-8 -*-

import json
import os

import requests
import numpy as np

"""
FACE_POINTS = list(range(0, 83))
JAW_POINTS = list(range(0, 19))
LEFT_EYE_POINTS = list(range(19, 29))
LEFT_BROW_POINTS = list(range(29, 37))
MOUTH_POINTS = list(range(37, 55))
NOSE_POINTS = list(range(55, 65))
RIGHT_EYE_POINTS = list(range(65, 75))
RIGHT_BROW_POINTS = list(range(75, 83))
"""
FACE_POINTS = list(range(0, 94))
JAW_POINTS = list(range(0, 33))
LEFT_EYE_POINTS = list(range(33, 41))
LEFT_BROW_POINTS = list(range(41, 50))
NOSE_POINTS = list(range(50, 65))
RIGHT_EYE_POINTS = list(range(65, 73))
RIGHT_BROW_POINTS = list(range(73, 82))
MOUTH_POINTS = list(range(82, 94))

LEFT_FACE = list(range(0, 17)) + list(range(42, 46))
RIGHT_FACE = list(range(16, 33)) + list(range(74, 78))

JAW_END = 33
FACE_START = 0
FACE_END = 94

OVERLAY_POINTS = [
    LEFT_FACE,
    RIGHT_FACE,
    JAW_POINTS,
]


def face_points(image):
    points = []
    txt = image + '.txt'

    if os.path.isfile(txt):
        with open(txt) as file:
            for line in file:
                points = line
    elif os.path.isfile(image):
        points = landmarks_by_face__(image)
        with open(txt, 'w') as file:
            file.write(str(points))

    faces = json.loads(points)['faces']

    matrix_list = np.matrix(matrix_marks(faces[0]['landmark']))

    point_list = []
    for p in matrix_list.tolist():
        point_list.append((int(p[0]), int(p[1])))

    face_area = [faces[0]["face_rectangle"]["top"], faces[0]["face_rectangle"]["left"], faces[0]["face_rectangle"]["width"], faces[0]["face_rectangle"]["height"]]

    return matrix_list, point_list, face_area


def landmarks_by_face__(image):
    url = 'https://api-cn.faceplusplus.com/facepp/v3/detect'
    params = {
        'api_key': 'oVnmrGYMAqUnGSSMf01mOW3rfRmWj52U',
        'api_secret': 'pumbBbjNuDUXY18H2r4kQkuoOQLpI3nQ',
        'return_landmark': 2,
    }
    file = {'image_file': open(image, 'rb')}

    r = requests.post(url=url, files=file, data=params)

    if r.status_code == requests.codes.ok:
        return r.content.decode('utf-8')
    else:
        return r.content


def matrix_rectangle(left, top, width, height):
    pointer = [
        (left, top),
        (left + width / 2, top),
        (left + width - 1, top),
        (left + width - 1, top + height / 2),
        (left, top + height / 2),
        (left, top + height - 1),
        (left + width / 2, top + height - 1),
        (left + width - 1, top + height - 1)
    ]

    return pointer


def matrix_marks(res):
    pointer=[
        [res['contour_left1']['x'],res['contour_left1']['y']],
        [res['contour_left2']['x'],res['contour_left2']['y']],
        [res['contour_left3']['x'],res['contour_left3']['y']],
        [res['contour_left4']['x'],res['contour_left4']['y']],
        [res['contour_left5']['x'],res['contour_left5']['y']],
        [res['contour_left6']['x'],res['contour_left6']['y']],
        [res['contour_left7']['x'],res['contour_left7']['y']],
        [res['contour_left8']['x'],res['contour_left8']['y']],
        [res['contour_left9']['x'],res['contour_left9']['y']],
        [res['contour_left10']['x'],res['contour_left10']['y']],
        [res['contour_left11']['x'],res['contour_left11']['y']],
        [res['contour_left12']['x'],res['contour_left12']['y']],
        [res['contour_left13']['x'],res['contour_left13']['y']],
        [res['contour_left14']['x'],res['contour_left14']['y']],
        [res['contour_left15']['x'],res['contour_left15']['y']],
        [res['contour_left16']['x'],res['contour_left16']['y']],
        [res['contour_chin']['x'],res['contour_chin']['y']],
        [res['contour_right16']['x'],res['contour_right16']['y']],
        [res['contour_right15']['x'],res['contour_right15']['y']],
        [res['contour_right14']['x'],res['contour_right14']['y']],
        [res['contour_right13']['x'],res['contour_right13']['y']],
        [res['contour_right12']['x'],res['contour_right12']['y']],
        [res['contour_right11']['x'],res['contour_right11']['y']],
        [res['contour_right10']['x'],res['contour_right10']['y']],
        [res['contour_right9']['x'],res['contour_right9']['y']],
        [res['contour_right8']['x'],res['contour_right8']['y']],
        [res['contour_right7']['x'],res['contour_right7']['y']],
        [res['contour_right6']['x'],res['contour_right6']['y']],
        [res['contour_right5']['x'],res['contour_right5']['y']],
        [res['contour_right4']['x'],res['contour_right4']['y']],
        [res['contour_right3']['x'],res['contour_right3']['y']],
        [res['contour_right2']['x'],res['contour_right2']['y']],
        [res['contour_right1']['x'],res['contour_right1']['y']],
        [res['left_eye_left_corner']['x'],res['left_eye_left_corner']['y']],
        [res['left_eye_upper_left_quarter']['x'],res['left_eye_upper_left_quarter']['y']],
        [res['left_eye_top']['x'],res['left_eye_top']['y']],
        [res['left_eye_upper_right_quarter']['x'],res['left_eye_upper_right_quarter']['y']],
        [res['left_eye_right_corner']['x'],res['left_eye_right_corner']['y']],
        [res['left_eye_lower_right_quarter']['x'],res['left_eye_lower_right_quarter']['y']],
        [res['left_eye_bottom']['x'],res['left_eye_bottom']['y']],
        [res['left_eye_lower_left_quarter']['x'],res['left_eye_lower_left_quarter']['y']],
        [res['left_eyebrow_left_corner']['x'],res['left_eyebrow_left_corner']['y']],
        [res['left_eyebrow_upper_left_quarter']['x'],res['left_eyebrow_upper_left_quarter']['y']],
        [res['left_eyebrow_upper_middle']['x'],res['left_eyebrow_upper_middle']['y']],
        [res['left_eyebrow_upper_right_quarter']['x'],res['left_eyebrow_upper_right_quarter']['y']],
        [res['left_eyebrow_upper_right_corner']['x'],res['left_eyebrow_upper_right_corner']['y']],
        [res['left_eyebrow_lower_right_corner']['x'],res['left_eyebrow_lower_right_corner']['y']],
        [res['left_eyebrow_lower_right_quarter']['x'],res['left_eyebrow_lower_right_quarter']['y']],
        [res['left_eyebrow_lower_middle']['x'],res['left_eyebrow_lower_middle']['y']],
        [res['left_eyebrow_lower_left_quarter']['x'],res['left_eyebrow_lower_left_quarter']['y']],
        [res['nose_bridge1']['x'],res['nose_bridge1']['y']],
        [res['nose_bridge2']['x'],res['nose_bridge2']['y']],
        [res['nose_bridge3']['x'],res['nose_bridge3']['y']],
        [res['nose_tip']['x'],res['nose_tip']['y']],
        [res['nose_left_contour1']['x'],res['nose_left_contour1']['y']],
        [res['nose_left_contour2']['x'],res['nose_left_contour2']['y']],
        [res['nose_left_contour3']['x'],res['nose_left_contour3']['y']],
        [res['nose_left_contour4']['x'],res['nose_left_contour4']['y']],
        [res['nose_left_contour5']['x'],res['nose_left_contour5']['y']],
        [res['nose_middle_contour']['x'],res['nose_middle_contour']['y']],
        [res['nose_right_contour1']['x'],res['nose_right_contour1']['y']],
        [res['nose_right_contour2']['x'],res['nose_right_contour2']['y']],
        [res['nose_right_contour3']['x'],res['nose_right_contour3']['y']],
        [res['nose_right_contour4']['x'],res['nose_right_contour4']['y']],
        [res['nose_right_contour5']['x'],res['nose_right_contour5']['y']],
        [res['right_eye_right_corner']['x'],res['right_eye_right_corner']['y']],
        [res['right_eye_upper_right_quarter']['x'],res['right_eye_upper_right_quarter']['y']],
        [res['right_eye_top']['x'],res['right_eye_top']['y']],
        [res['right_eye_upper_left_quarter']['x'],res['right_eye_upper_left_quarter']['y']],
        [res['right_eye_left_corner']['x'],res['right_eye_left_corner']['y']],
        [res['right_eye_lower_left_quarter']['x'],res['right_eye_lower_left_quarter']['y']],
        [res['right_eye_bottom']['x'],res['right_eye_bottom']['y']],
        [res['right_eye_lower_right_quarter']['x'],res['right_eye_lower_right_quarter']['y']],
        [res['right_eyebrow_right_corner']['x'],res['right_eyebrow_right_corner']['y']],
        [res['right_eyebrow_upper_right_quarter']['x'],res['right_eyebrow_upper_right_quarter']['y']],
        [res['right_eyebrow_upper_middle']['x'],res['right_eyebrow_upper_middle']['y']],
        [res['right_eyebrow_upper_left_quarter']['x'],res['right_eyebrow_upper_left_quarter']['y']],
        [res['right_eyebrow_upper_left_corner']['x'],res['right_eyebrow_upper_left_corner']['y']],
        [res['right_eyebrow_lower_left_corner']['x'],res['right_eyebrow_lower_left_corner']['y']],
        [res['right_eyebrow_lower_left_quarter']['x'],res['right_eyebrow_lower_left_quarter']['y']],
        [res['right_eyebrow_lower_middle']['x'],res['right_eyebrow_lower_middle']['y']],
        [res['right_eyebrow_lower_right_quarter']['x'],res['right_eyebrow_lower_right_quarter']['y']],
        [res['mouth_left_corner']['x'],res['mouth_left_corner']['y']],
        [res['mouth_upper_lip_left_contour2']['x'],res['mouth_upper_lip_left_contour2']['y']],
        [res['mouth_upper_lip_left_contour4']['x'],res['mouth_upper_lip_left_contour4']['y']],
        [res['mouth_upper_lip_top']['x'],res['mouth_upper_lip_top']['y']],
        [res['mouth_upper_lip_right_contour3']['x'],res['mouth_upper_lip_right_contour3']['y']],
        [res['mouth_upper_lip_right_contour2']['x'],res['mouth_upper_lip_right_contour2']['y']],
        [res['mouth_right_corner']['x'],res['mouth_right_corner']['y']],
        [res['mouth_lower_lip_right_contour2']['x'],res['mouth_lower_lip_right_contour2']['y']],
        [res['mouth_lower_lip_right_contour3']['x'],res['mouth_lower_lip_right_contour3']['y']],
        [res['mouth_lower_lip_bottom']['x'],res['mouth_lower_lip_bottom']['y']],
        [res['mouth_lower_lip_left_contour3']['x'],res['mouth_lower_lip_left_contour3']['y']],
        [res['mouth_lower_lip_left_contour2']['x'],res['mouth_lower_lip_left_contour2']['y']],
    ]

    return pointer
