# Drill #10 제출 - 2022184007 김성민
# 새 크기: 30cm x 30cm, 비행 속도: 2m/s, 날갯짓 속도: 초당 20회/s

from pico2d import open_canvas, delay, close_canvas
import game_framework

import play_mode as start_mode

open_canvas(1600, 600)
game_framework.run(start_mode)
close_canvas()

