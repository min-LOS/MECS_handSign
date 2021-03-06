import preprocessing as pre
import cv2
import os
import glob

#감사 데이터 부족, 위: 손가락 인식 모누 안됌 존경: 받침 손가락 제대로 인식불가
label = ['THANKYOU', 'POLICE', 'HEAD', 'HELLO', 'DOWN', 'UP', 'HOME', 'RESPECT', 'FRIEND', 'DAD']
index = 9
source_path = 'C:\\Users\\PKNU\\Downloads\\hand_sign_THANKYOU2.mp4'
file_name = 'C:\\Users\\PKNU\\Downloads\\respect02.csv'

csv_index = ['FRAME_NUM',
             'face_X[10]', 'face_X[234]', 'face_X[152]', 'face_X[454]',
             'face_Y[10]', 'face_Y[234]', 'face_Y[152]', 'face_Y[454]',
             'face_Z[10]', 'face_Z[234]', 'face_Z[152]', 'face_Z[454]',

             'body_X[11]', 'body_X[12]', 'body_X[13]', 'body_X[14]', 'body_X[15]', 'body_X[16]', 'body_X[17]',
             'body_X[18]', 'body_X[19]', 'body_X[20]', 'body_X[21]', 'body_X[22]',
             'body_Y[11]', 'body_Y[12]', 'body_Y[13]', 'body_Y[14]', 'body_Y[15]', 'body_Y[16]', 'body_Y[17]',
             'body_Y[18]', 'body_Y[19]', 'body_Y[20]', 'body_Y[21]', 'body_Y[22]',
             'body_Z[11]', 'body_Z[12]', 'body_Z[13]', 'body_Z[14]', 'body_Z[15]', 'body_Z[16]', 'body_Z[17]',
             'body_Z[18]', 'body_Z[19]', 'body_Z[20]', 'body_Z[21]', 'body_Z[22]',

             'R_WRIST_X', 'R_THUMB_CMC_X', 'R_THUMB_MCP_X', 'R_THUMB_IP_X', 'R_THUMB_TIP_X', 'R_INDEX_FINGER_MCP_X',
             'R_INDEX_FINGER_PIP_X', 'R_INDEX_FINGER_DIP_X', 'R_INDEX_FINGER_TIP_X', 'R_MIDDLE_FINGER_MCP_X',
             'R_MIDDLE_FINGER_PIP_X', 'R_MIDDLE_FINGER_DIP_X', 'R_MIDDLE_FINGER_TIP_X', 'R_RING_FINGER_MCP_X',
             'R_RING_FINGER_PIP_X', 'R_RING_FINGER_DIP_X', 'R_RING_FINGER_TIP_X', 'R_PINKY_MCP_X', 'R_PINKY_PIP_X',
             'R_PINKY_DIP_X', 'R_PINKY_TIP_X',
             'R_WRIST_Y', 'R_THUMB_CMC_Y', 'R_THUMB_MCP_Y', 'R_THUMB_IP_Y', 'R_THUMB_TIP_Y', 'R_INDEX_FINGER_MCP_Y',
             'R_INDEX_FINGER_PIP_Y', 'R_INDEX_FINGER_DIP', 'R_INDEX_FINGER_TIP', 'R_MIDDLE_FINGER_MCP',
             'R_MIDDLE_FINGER_PIP_Y', 'R_MIDDLE_FINGER_DIP_Y', 'R_MIDDLE_FINGER_TIP_Y', 'R_RING_FINGER_MCP_Y',
             'R_RING_FINGER_PIP_Y', 'R_RING_FINGER_DIP_Y', 'R_RING_FINGER_TIP_Y', 'R_PINKY_MCP_Y', 'R_PINKY_PIP_Y',
             'R_PINKY_DIP_Y', 'R_PINKY_TIP_Y',
             'R_WRIST_Z', 'R_THUMB_CMC_Z', 'R_THUMB_MCP_Z', 'R_THUMB_IP_Z', 'R_THUMB_TIP_Z', 'R_INDEX_FINGER_MCP_Z',
             'R_INDEX_FINGER_PIP_Z', 'R_INDEX_FINGER_DIP_Z', 'R_INDEX_FINGER_TIP_Z', 'R_MIDDLE_FINGER_MCP_Z',
             'R_MIDDLE_FINGER_PIP_Z', 'R_MIDDLE_FINGER_DIP_Z', 'R_MIDDLE_FINGER_TIP_Z', 'R_RING_FINGER_MCP_Z',
             'R_RING_FINGER_PIP_Z', 'R_RING_FINGER_DIP_Z', 'R_RING_FINGER_TIP_Z', 'R_PINKY_MCP_Z', 'R_PINKY_PIP_Z',
             'R_PINKY_DIP_Z', 'R_PINKY_TIP_Z',

             'L_WRIST_X', 'L_THUMB_CMC_X', 'L_THUMB_MCP_X', 'L_THUMB_IP_X', 'L_THUMB_TIP_X', 'L_INDEX_FINGER_MCP_X',
             'L_INDEX_FINGER_PIP_X', 'L_INDEX_FINGER_DIP_X', 'L_INDEX_FINGER_TIP_X', 'L_MIDDLE_FINGER_MCP_X',
             'L_MIDDLE_FINGER_PIP_X', 'L_MIDDLE_FINGER_DIP_X', 'L_MIDDLE_FINGER_TIP_X', 'L_RING_FINGER_MCP_X',
             'L_RING_FINGER_PIP_X', 'L_RING_FINGER_DIP_X', 'L_RING_FINGER_TIP_X', 'L_PINKY_MCP_X',
             'L_PINKY_PIP_X', 'L_PINKY_DIP_X', 'L_PINKY_TIP_X',
             'L_WRIST_Y', 'L_THUMB_CMC_Y', 'L_THUMB_MCP_Y', 'L_THUMB_IP_Y', 'L_THUMB_TIP_Y', 'L_INDEX_FINGER_MCP_Y',
             'L_INDEX_FINGER_PIP_Y', 'L_INDEX_FINGER_DIP', 'L_INDEX_FINGER_TIP', 'L_MIDDLE_FINGER_MCP',
             'L_MIDDLE_FINGER_PIP_Y', 'L_MIDDLE_FINGER_DIP_Y', 'L_MIDDLE_FINGER_TIP_Y', 'L_RING_FINGER_MCP_Y',
             'L_RING_FINGER_PIP_Y', 'L_RING_FINGER_DIP_Y', 'L_RING_FINGER_TIP_Y', 'L_PINKY_MCP_Y',
             'L_PINKY_PIP_Y', 'L_PINKY_DIP_Y', 'L_PINKY_TIP_Y',
             'L_WRIST_Z', 'L_THUMB_CMC_Z', 'L_THUMB_MCP_Z', 'L_THUMB_IP_Z', 'L_THUMB_TIP_Z', 'L_INDEX_FINGER_MCP_Z',
             'L_INDEX_FINGER_PIP_Z', 'L_INDEX_FINGER_DIP_Z', 'L_INDEX_FINGER_TIP_Z', 'L_MIDDLE_FINGER_MCP_Z',
             'L_MIDDLE_FINGER_PIP_Z', 'L_MIDDLE_FINGER_DIP_Z', 'L_MIDDLE_FINGER_TIP_Z', 'L_RING_FINGER_MCP_Z',
             'L_RING_FINGER_PIP_Z', 'L_RING_FINGER_DIP_Z', 'L_RING_FINGER_TIP_Z', 'L_PINKY_MCP_Z',
             'L_PINKY_PIP_Z', 'L_PINKY_DIP_Z', 'L_PINKY_TIP_Z']

# For local folder input:
targer_video_dir = fr"C:\Users\harby\PycharmProjects\MECS_handSign\video\{label[index]}"
videofiles = glob.glob(targer_video_dir+"\*.avi") + glob.glob(targer_video_dir+"\*.mp4")

targer_csv_dir = fr"C:\Users\harby\Desktop\csv_data\{label[index]}"
os.makedirs(targer_csv_dir, exist_ok=True)

#print(videofiles)
for i, file in enumerate(videofiles):
    pre.save_3csv_landmarks(videofiles[i], targer_csv_dir + f'\{label[index]}_{i}.csv', csv_index)