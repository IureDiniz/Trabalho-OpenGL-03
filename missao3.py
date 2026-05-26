from ast import If
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


ang = 0
tran = 0
esca = 1


class Pentagar:
    def __init__(self):
        self.vertices = [
            [-2, 0, -2],
            [-2, 0, 2],
            [2, 0, 2],
            [3, 0, 0],
            [2, 0, -2],
            [0, 5, 0]

        ]
        self.faces = []
        self.cores = [
                        [1.0, 0.0, 0.0],  # vermelho
                        [0.0, 1.0, 0.0],  # verde
                        [0.0, 0.0, 1.0],  # azul
                        [1.0, 1.0, 0.0],  # amarelo
                        [0.0, 1.0, 1.0],  # azul claro
                        [1.0, 1.0, 1.0]   # branco
                      ]

    def definir(self):
        self.faces = [
            # Base
            [   
                self.vertices[0],
                self.vertices[1],
                self.vertices[2],
                self.vertices[3],
                self.vertices[4]
            ],

            # Coluna 1
            [
                self.vertices[0],
                self.vertices[1],
                self.vertices[5]
            ],

            #Coluna 2
            [
                self.vertices[1],
                self.vertices[2],
                self.vertices[5]
            ],
#
            # Coluna 3
            [
                self.vertices[2],
                self.vertices[3],
                self.vertices[5]
            ],
#
            # Coluna 4
            [
                self.vertices[3],
                self.vertices[4],
                self.vertices[5]
            ],

            # Coluna 5
            [
                self.vertices[4],
                self.vertices[0],
                self.vertices[5]
            ]
        ]

    def desenhar(self):
        glBegin(GL_POLYGON)
        glColor3fv(self.cores[0])
        for vertice in self.faces[0]:
            glVertex3fv(vertice)
        glEnd()

        for i in range(len(self.faces) - 1):
            glBegin(GL_TRIANGLES)
            glColor3fv(self.cores[i+1])
            for vertice in self.faces[i+1]:
                glVertex3fv(vertice)
            glEnd()



def configCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 1000)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(10, 10, 10, 0, 3, 0, 0, 1, 0)


def desenhaEixos():
    glBegin(GL_LINES)
    glColor3f(1, 0, 0)
    glVertex3f(-100, 0, 0)
    glVertex3f(100, 0, 0)
    glColor3f(0, 1, 0)
    glVertex3f(0, -100, 0)
    glVertex3f(0, 100, 0)
    glColor3f(0, 0, 1)
    glVertex3f(0, 0, -100)
    glVertex3f(0, 0, 100)
    glEnd()

def tela():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    configCamera()
    desenhaEixos()

    glTranslatef(tran, 0, 0)
    glRotatef(ang, 0, 1, 0)
    glScalef(esca, esca, esca)
    
    glColor3f(1, 1, 1)
    pentegar.desenhar()

    glutSwapBuffers()


def teclado(key, x, y):
    global ang, tran, esca

    if key == b'x':
        tran += 1
        glutPostRedisplay()
    if key == b'X':
        tran -= 1
        glutPostRedisplay()
    
    if key == b'y':
        ang += 45
        glutPostRedisplay()
    if key == b'Y':
        ang -= 45
        glutPostRedisplay()

    if key == b'e':
        esca += 0.1
        glutPostRedisplay()
    if key == b'E':
        if esca <= 0.1:
            esca = 0.1
        else:
            esca -= 0.1
        glutPostRedisplay()


def mouse(button, state, x, y):
    global ang, tran, esca

    if button == GLUT_LEFT_BUTTON:
        ang = 0
        tran = 0
        esca = 1
        glutPostRedisplay()


pentegar = Pentagar()
pentegar.definir()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow("Missao 3")

glutKeyboardFunc(teclado)
glutMouseFunc(mouse)
glutDisplayFunc(tela)
glEnable(GL_DEPTH_TEST)

glutMainLoop()
