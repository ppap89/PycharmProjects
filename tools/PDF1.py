import camelot.io as camelot
import os
os.chdir('D:/Desktop/')
import cv2
data1= camelot.read_pdf("微信支付转账电子凭证", pages='12',flavor='stream')
data1[0].to_csv('data1.csv',encoding='utf_8_sig')