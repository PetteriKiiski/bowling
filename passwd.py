import pygame, sys
from pygame.locals import *
pygame.init()
canvas = pygame.display.set_mode((100, 100), 0, 0)
pygame.display.set_caption('Password')
print ("Enter password(esc to quit)")
passwd = 'adventures50Five'
end = False
enter = ''
shifted = False
while True:
	for event in pygame.event.get():
		if event.type == KEYDOWN:
			if event.key == K_RETURN:
				if enter == passwd:
					print ('correct')
					pygame.quit()
					end = True
					break
				else:
					print ('wrong')
					pygame.quit()
					sys.exit()
			if event.key == K_ESCAPE:
				pygame.quit()
				sys.exit()
			if event.key == K_RSHIFT or event.key == K_LSHIFT:
				shifted = True
				continue
			if shifted == False:
				if event.key == K_a:
					enter += 'a'
				if event.key == K_b:
					enter += 'b'
				if event.key == K_c:
					enter += 'c'
				if event.key == K_d:
					enter += 'd'
				if event.key == K_e:
					enter += 'e'
				if event.key == K_f:
					enter += 'f'
				if event.key == K_g:
					enter += 'g'
				if event.key == K_h:
					enter += 'h'
				if event.key == K_i:
					enter += 'i'
				if event.key == K_j:
					enter += 'j'
				if event.key == K_k:
					enter += 'k'
				if event.key == K_l:
					enter += 'l'
				if event.key == K_m:
					enter += 'm'
				if event.key == K_n:
					enter += 'n'
				if event.key == K_o:
					enter += 'o'
				if event.key == K_p:
					enter += 'p'
				if event.key == K_q:
					enter += 'q'
				if event.key == K_r:
					enter += 'r'
				if event.key == K_s:
					enter += 's'
				if event.key == K_t:
					enter += 't'
				if event.key == K_u:
					enter += 'u'
				if event.key == K_v:
					enter += 'v'
				if event.key == K_w:
					enter += 'w'
				if event.key == K_x:
					enter += 'x'
				if event.key == K_y:
					enter += 'y'
				if event.key == K_z:
					enter += 'z'
				if event.key == K_1:
					enter += '1'
				if event.key == K_1:
					enter += '1'
				if event.key == K_2:
					enter += '2'
				if event.key == K_3:
					enter += '3'
				if event.key == K_4:
					enter += '4'
				if event.key == K_5:
					enter += '5'
				if event.key == K_6:
					enter += '6'
				if event.key == K_7:
					enter += '7'
				if event.key == K_8:
					enter += '8'
				if event.key == K_9:
					enter += '9'
				if event.key == K_0:
					enter += '0'
			else:
				if event.key == K_a:
					enter += 'A'
				if event.key == K_b:
					enter += 'B'
				if event.key == K_c:
					enter += 'C'
				if event.key == K_d:
					enter += 'D'
				if event.key == K_e:
					enter += 'E'
				if event.key == K_f:
					enter += 'F'
				if event.key == K_g:
					enter += 'G'
				if event.key == K_h:
					enter += 'H'
				if event.key == K_i:
					enter += 'I'
				if event.key == K_j:
					enter += 'F'
				if event.key == K_k:
					enter += 'K'
				if event.key == K_l:
					enter += 'L'
				if event.key == K_m:
					enter += 'M'
				if event.key == K_n:
					enter += 'N'
				if event.key == K_o:
					enter += 'O'
				if event.key == K_p:
					enter += 'P'
				if event.key == K_q:
					enter += 'Q'
				if event.key == K_r:
					enter += 'R'
				if event.key == K_s:
					enter += 'S'
				if event.key == K_t:
					enter += 'T'
				if event.key == K_u:
					enter += 'U'
				if event.key == K_v:
					enter += 'V'
				if event.key == K_w:
					enter += 'W'
				if event.key == K_x:
					enter += 'X'
				if event.key == K_y:
					enter += 'Y'
				if event.key == K_z:
					enter += 'Z'
				if event.key == K_1:
					enter += '1'
				if event.key == K_1:
					enter += '1'
				if event.key == K_2:
					enter += '2'
				if event.key == K_3:
					enter += '3'
				if event.key == K_4:
					enter += '4'
				if event.key == K_5:
					enter += '5'
				if event.key == K_6:
					enter += '6'
				if event.key == K_7:
					enter += '7'
				if event.key == K_8:
					enter += '8'
				if event.key == K_9:
					enter += '9'
				if event.key == K_0:
					enter += '0'
		if event.type == KEYUP:
			if event.key == K_RSHIFT or event.key == K_LSHIFT:
				shifted = False
	if end:
		break
