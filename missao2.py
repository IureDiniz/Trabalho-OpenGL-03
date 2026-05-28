from ast import If
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


ang = [0, 0, 0]


def configCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(5, 5, 5, 0, 0, 0, 0, 1, 0)


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

def tela():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    configCamera()
    desenhaEixos()
    glRotatef(ang[2], 0, 0, 1)
    glRotatef(ang[1], 0, 1, 0)
    glRotatef(ang[0], 1, 0, 0)
    glColor3f(1, 1, 1)
    glutWireTeapot(1)

    

    glutSwapBuffers()


def teclado(key, x, y):
    global rotX, rotY, rotZ, ang

    
    if key == b'x':
        ang[0] += 45
        glutPostRedisplay()
    if key == b'X':
        ang[0] -= 45
        glutPostRedisplay()
    if key == b'y':
        ang[1] += 45
        glutPostRedisplay()
    if key == b'Y':
        ang[1] -= 45
        glutPostRedisplay()
    if key == b'z':
        ang[2] += 45
        glutPostRedisplay()
    if key == b'Z':
        ang[2] -= 45
        glutPostRedisplay()

def mouse(button, state, x, y):
    global ang

    if button == GLUT_LEFT_BUTTON:
        ang[0] = 0
        ang[1] = 0
        ang[2] = 0
        glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow("Missao 2")

glutKeyboardFunc(teclado)
glutMouseFunc(mouse)
glutDisplayFunc(tela)
glEnable(GL_DEPTH_TEST)

glutMainLoop()
