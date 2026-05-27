from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

escX = 1
escY = 1

def configCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 30, 0, 2, 0, 0, 1, 0)

def desenhaEixos():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(-10, 0, 0)
    glVertex3f(10, 0, 0)
    glColor3f(0, 1, 0)
    glVertex3f(0, -10, 0)
    glVertex3f(0, 10, 0)
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, -10)
    glVertex3f(0, 0, 10)
    glEnd()

class Forma:
    vertices = [
        [2, 0, 0],
        [2, 2, 0],
        [6, 2, 0],
        [6, 0, 0],

        [3, 2, 0],
        [3, 8, 0],
        [5, 8, 0],
        [5, 2, 0],

        [2, 8, 0],
        [2, 10, 0],
        [6, 10, 0],
        [6, 8, 0]
    ]
        

    def desenha(self):
        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)
        glVertex3f(self.vertices[0][0], self.vertices[0][1], self.vertices[0][2])
        glVertex3f(self.vertices[1][0], self.vertices[1][1], self.vertices[1][2])
        glVertex3f(self.vertices[2][0], self.vertices[2][1], self.vertices[2][2])
        glVertex3f(self.vertices[3][0], self.vertices[3][1], self.vertices[3][2])
        glEnd()

        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)
        glVertex3f(self.vertices[4][0], self.vertices[4][1], self.vertices[4][2])
        glVertex3f(self.vertices[5][0], self.vertices[5][1], self.vertices[5][2])
        glVertex3f(self.vertices[6][0], self.vertices[6][1], self.vertices[6][2])
        glVertex3f(self.vertices[7][0], self.vertices[7][1], self.vertices[7][2])
        glEnd()

        glColor3f(1, 1, 1)
        glBegin(GL_QUADS)
        glVertex3f(self.vertices[8][0], self.vertices[8][1], self.vertices[8][2])
        glVertex3f(self.vertices[9][0], self.vertices[9][1], self.vertices[9][2])
        glVertex3f(self.vertices[10][0], self.vertices[10][1], self.vertices[10][2])
        glVertex3f(self.vertices[11][0], self.vertices[11][1], self.vertices[11][2])
        glEnd()

        

def tela():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    configCamera()
    desenhaEixos()
    
    glScalef(escX, escY, 1)
    
    forma.desenha()
    
    
    

    glutSwapBuffers()


def teclado(key, x, y):
    global escX, escY
    
    if key == b'x':
        escY *= -1
        escX = 1
        
        glutPostRedisplay()

    if key == b'y':
        escX *= -1
        escY = 1
    
        glutPostRedisplay()
        

    

forma = Forma()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow("Missao 5")

glutKeyboardFunc(teclado)
glutDisplayFunc(tela)
glEnable(GL_DEPTH_TEST)

glutMainLoop()
