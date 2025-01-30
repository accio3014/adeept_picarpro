# 후륜 바퀴 제어 server/move.py
# 서보 모터 제어 server/servo.py

import time
import RPi.GPIO as GPIO
from server.move import *
from server.servo import *
from Adafruit_PCA9685 import PCA9685


setup()                         # 뒷 바퀴 모터 초기화
SPEED = 50                      # 뒷 바퀴 모터 속더

pwm = PCA9685()                 # PCA9685 초기화
pwm.set_pwm_freq(50)            # 50Hz 설정 (서보 모터에 적합)

##############
# 모터의 초기 세팅
##############
# 0번 핀 서보 모터(앞 바퀴) 방향 조정
pwm0_center = 330               # 중앙 위치(330)
pwm.set_pwm(0, 0, pwm0_center)  # 0번 채널에 중앙 값 설정

# 1번 핀 서보 모터(헤드 좌우) 방향 조정
pwm1_center = 130               # 중앙 위치(130)
pwm.set_pwm(1, 0, pwm1_center)  # 1번 채널에 중앙 값 설정

# 2번 핀 서보 모터(헤드 위 아래) 방향 조정
pwm2_center = 355               # 중앙 위치(355)
pwm.set_pwm(2, 0, pwm2_center)  # 2번 채널에 중앙 값 설정

time.sleep(2)


move(SPEED, 'forward', 'no')    # forward, backward
time.sleep(2)                   # 2초 동안 이동
motorStop()                     # 정지




#############################
# 로봇 이동 후 다시 중앙으로 위치 고정
#############################
# 0번 핀 서보 모터(앞 바퀴) 방향 조정
pwm0_center = 330               # 중앙 위치(330)
pwm.set_pwm(0, 0, pwm0_center)  # 0번 채널에 중앙 값 설정

# 1번 핀 서보 모터(헤드 좌우) 방향 조정
pwm1_center = 130               # 중앙 위치(130)
pwm.set_pwm(1, 0, pwm1_center)  # 1번 채널에 중앙 값 설정

# 2번 핀 서보 모터(헤드 위 아래) 방향 조정
pwm2_center = 355               # 중앙 위치(355)
pwm.set_pwm(2, 0, pwm2_center)  # 2번 채널에 중앙 값 설정