#!/usr/bin/python2
# CC0 by leandro@tia.mat.br

import socket
import pygame
import pygame.camera
import pygame.transform
from pygame.locals import *

def set_pixel(conn, x, y, color):
  cmd = "PX %d %d %06x\n" % (x, y, color)
  conn.send(cmd)

def set_surface(conn, surface):
  cmds = []

  for x in range(240):
    for y in range(180):
      pixel = surface.get_at((x, y))
      cmds.append("PX %d %d %06x\n" % (x, y, encode_color(pixel.r, pixel.g, pixel.b)))
  
  conn.send(''.join(cmds))

def encode_color(r, g, b):
  return r << 16 | g << 8 | b

if __name__ == '__main__':
  pygame.init()
  pygame.camera.init()

  camlist = pygame.camera.list_cameras()
  if camlist:
    cam = pygame.camera.Camera(camlist[0], (640, 480), "RGB")
    cam.start()
  else:
    raise "No camera"
    
  conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  conn.connect(('barflood.sha2017.org', 2342))

  while True:
    img = pygame.transform.smoothscale(cam.get_image(), (240, 180))
    set_surface(conn, img)

