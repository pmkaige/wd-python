#!/usr/bin/python
# -*- coding: utf-8 -*-
#闻到 http://wendao123.cn
#使用gifmaze这个库制作gif迷宫
#github地址：https://github.com/neozhaoliang/gifmaze


import gifmaze as gm
from gifmaze.algorithms import prim
#首先我们需要构建一个GIFSurface对象（类似cairo的ImageSurface类），
# 我们的动画将会画在这个对象上。同时，我们需要指定图片的大小
#这里bg_color=0意味着全局颜色表中的第0个颜色被用作背景颜色。
surface = gm.GIFSurface(width=600, height=400, bg_color=0)

#只要你还没有最后保存图片，您可以随时定义全局颜色表格，并且必须至少指定一个RGB三元组。
surface.set_palette([0, 0, 0, 255, 255, 255])

#然后我们构建一个环境，生成的动画基于这个环境构建（类似cairo的Context类）
anim = gm.Animation(surface)

#然后我们设置这个动画的控制参数,
#这定义了一个尺寸为149x99的迷宫，缩放为4（所以它占据了596x396像素），
# 并且向右平移了2个像素，向底部平移了2个像素，使其位于图像的中心。
maze = gm.Maze(149, 99, None).scale(4).translate((2, 2))

#这里speed控制动画的速度，
# delay控制连续帧之间的延迟，
# trans_index是透明色彩索引，
# min_code_length是将动画编码成帧的最小代码长度，
# start是运行的Prim算法的起始单元格（它是单元格的位置迷宫，而不是图像中的像素）。
# cmap控制细胞如何映射到颜色，即{细胞：颜色} cmap={0: 0, 1: 1}意味着单元格的值为0（墙壁）用0索引颜色（黑色）着色，单元格的值为1（树）用1索引颜色（白色）着色。
#我加了两个延迟帧，以便我们能够看清楚动画的过程。
# anim.pause(200)
anim.run(prim, maze, speed=30, delay=5, trans_index=None, cmap={0: 0, 1: 1}, min_code_length=2, start=(0, 0))
# anim.pause(500)

#把这个动画保存到GIF文件。
surface.save('prim.gif')
surface.close()

