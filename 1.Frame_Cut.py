import cv2
import os

#vc = cv2.VideoCapture('C:\\September_2018_2019\\My_work\\Cybersecurity\\codes\\test_videos\\blink_detection_demo.mp4')  # 读入视频文件

#vc = cv2.VideoCapture('C:\\September_2018_2019\\My_work\\Cybersecurity\\codes\\UOS\\3_result.mp4')  # 读入视频文件
c = 1

path_no=0
path_str=str(path_no)
pathDir='.\Resultsimage\\'+path_str

while (os.path.isdir(pathDir)):
    path_no+=1
    path_str=str(path_no)
    pathDir='.\Resultsimage\\'+path_str

vid_str=path_str+'.mp4'
vc = cv2.VideoCapture('.\\Videos_Test\\'+vid_str)

#HEEEEERRRRREEEEE,
vid_no=0
vid_str=str(vid_no)
prjDir='.\Resultsimage\\'+vid_str

while (os.path.isdir(prjDir)):
    vid_no+=1
    vid_str=str(vid_no)
    prjDir='.\Resultsimage\\'+vid_str

vid_str=str(vid_no)
path_out='.\Resultsimage\\'+vid_str+'\\'
booll=os.path.isdir(os.path.join(path_out))
if not booll:
    os.mkdir(path_out)


if vc.isOpened():  # 判断是否正常打开
    rval, frame = vc.read()
    print("Read Successfully")

else:
    rval = False

# timeF = 2  # 视频帧计数间隔频率
count = 0
name_no = 0
while rval:  # 循环读取视频帧
    rval, frame = vc.read()
    count += 1
    if count >= 0 & count < 500:

        if (count % 3 == 0):  # 每隔timeF帧进行存储操作
            name_no += 1

            # frame = frame[100:380, :]
            #frame = frame[50:480, 100:800]
            cv2.imwrite(path_out + str(name_no) + '.jpg', frame)  # 存储为图像        cv2.waitKey(1)48
vc.release()
