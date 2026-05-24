from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


tranX = 0.0
tranY = 0.0


def configCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 0, 5, 0, 0, 0, 0, 1, 0)


def desenhaTriangulo():
    glBegin(GL_TRIANGLES)
    glColor3f(1, 0, 0)
    glVertex3f(-1, 0, 0)
    glVertex3f(1, 0, 0)
    glVertex3f(0, 1, 0)
    glEnd()

def tela():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    configCamera()
    glTranslatef(tranX, tranY, 0)
    desenhaTriangulo()

    glutSwapBuffers()


def teclado(key, x, y):
    global tranX, tranY

    if key == b'w':
        tranY += 0.1
        glutPostRedisplay()
    if key == b's':
        tranY -= 0.1
        glutPostRedisplay()
    if key == b'd':
        tranX += 0.1
        glutPostRedisplay()
    if key == b'a':
        tranX -= 0.1
        glutPostRedisplay()


glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow("Missao 1")

glutKeyboardFunc(teclado)
glutDisplayFunc(tela)

glutMainLoop()