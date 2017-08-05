#!/usr/bin/python2
# CC0 by leandro@tia.mat.br

import socket
import pygame

def set_pixel(conn, x, y, color):
  cmd = "PX %d %d %06x\n" % (x, y, color)
  conn.send(cmd)

def encode_color(r, g, b):
  return r << 16 | g << 8 | b

def set_surface(conn, surface):
  cmds = []

  for x in range(240):
    for y in range(180):
      pixel = surface.get_at((x, y))
      cmds.append("PX %d %d %06x\n" % (x, y, encode_color(pixel.r, pixel.g, pixel.b)))
  
  conn.send(''.join(cmds))

if __name__ == '__main__':
  conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  conn.connect(('barflood.sha2017.org', 2342))

  msx = pygame.image.load("msx.gif")

  set_surface(conn, msx)
