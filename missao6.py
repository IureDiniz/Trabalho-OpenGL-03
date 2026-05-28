from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

cisX = 0.0


def cisalha(cisX):
    matrizCis = [
        1.0, 0.0, 0.0, 0.0,
        cisX, 1.0, 0.0, 0.0,
        0.0, 0.0, 1.0, 0.0,
        0.0, 0.0, 0.0, 1.0
    ]

    glMultMatrixf(matrizCis)


def configCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(0, 5, 10, 0, 2, 0, 0, 1, 0)


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
    cores = [[1, 1, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1], [1, 0, 0]]
    vertices = [
        [2, 0, -2],
        [-2, 0, -2],
        [-2, 0, 0],
        [2, 0, 0],
        [2, 2, -2],
        [-2, 2, -2],
        [-2, 2, 0],
        [2, 2, 0],
    ]
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[0], vertices[3], vertices[7], vertices[4]],
        [vertices[1], vertices[0], vertices[4], vertices[5]],
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
    ]

    def desenha(self):
        for i in range(6):
            glColor3f(self.cores[i][0], self.cores[i][1], self.cores[i][2])
            glBegin(GL_QUADS)
            for j in range(4):
                glVertex3f(
                    self.faces[i][j][0], self.faces[i][j][1], self.faces[i][j][2]
                )
            glEnd()


def tela():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    configCamera()
    desenhaEixos()

    cisalha(cisX)

    forma.desenha()

    glutSwapBuffers()


def teclado(key, x, y):
    global cisX

    if key == b"z":
        cisX = 0.0

        glLoadIdentity()
        glutPostRedisplay()

    if key == b"h":
        cisX += 0.1

        glutPostRedisplay()

    if key == b"H":
        cisX -= 0.1

        glutPostRedisplay()


forma = Forma()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow("Missao 6")

glutKeyboardFunc(teclado)
glutDisplayFunc(tela)
glEnable(GL_DEPTH_TEST)

glutMainLoop()
