from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

escala = [1, 1, 1]

def configCamera():
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, 1, 0.1, 100)

    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    gluLookAt(5, 5, 20, 0, 0, 0, 0, 1, 0)

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

class Triangulo:
    vertices = [
        [-6, 0, 0],
        [-4, 0, 0],
        [-5, 3, 0]
    ]

    min = [-6, 0, 0]
    max = [-4, 3, 0]
        

    def desenha(self):
        glColor3f(1, 1, 1)

        glPushMatrix()
        glTranslatef(-5, 1 , 0)
        glScalef(escala[0], escala[0], 1)
        glTranslatef(5, -1, 0)
        
        glBegin(GL_TRIANGLES)
        glVertex3f(self.vertices[0][0], self.vertices[0][1], self.vertices[0][2])
        glVertex3f(self.vertices[1][0], self.vertices[1][1], self.vertices[1][2])
        glVertex3f(self.vertices[2][0], self.vertices[2][1], self.vertices[2][2])
        glEnd()

        glPopMatrix()

class Cubo:
    cores = [[1, 1, 1], [1, 1, 0], [1, 0, 1], [0, 1, 1], [0, 0, 1], [1, 0, 0]]
    vertices = [
        [2, 0, -2],
        [-2, 0, -2],
        [-2, 0, 0],
        [2, 0, 0],
        [2, 2, -2],
        [-2, 2, -2],
        [-2, 2, 0],
        [2, 2, 0]
    ]
    faces = [
        [ vertices[0], vertices[1], vertices[2], vertices[3] ],
        [ vertices[2], vertices[3], vertices[7], vertices[6] ],
        [ vertices[0], vertices[3], vertices[7], vertices[4] ],
        [ vertices[1], vertices[0], vertices[4], vertices[5] ],
        [ vertices[1], vertices[2], vertices[6], vertices[5] ],
        [ vertices[4], vertices[5], vertices[6], vertices[7] ]
    ]
    
    min = [-2, 0, -2]
    max = [2, 2, 0]
        
    
    def desenha(self):
        glPushMatrix()
        glTranslatef(0, 1, -1)
        glScalef(escala[1], escala[1], escala[1])
        glTranslatef(0, -1, 1)
        
        for i in range(6):
            glColor3f(self.cores[i][0], self.cores[i][1], self.cores[i][2])
            glBegin(GL_QUADS)
            for j in range(4):
                glVertex3f(self.faces[i][j][0], self.faces[i][j][1], self.faces[i][j][2])
            glEnd()
    
        glPopMatrix()

class Quadrado:
    vertices = [
        [5, 0, -2],
        [7, 0, -2],
        [7, 0, 2],
        [5, 0, 2]
    ]

    min = [5, 0, -2]
    max = [7, 0, 2]
    
    def desenha(self):
        glColor3f(1, 1, 1)

        glPushMatrix()
        glTranslatef(6, 0, 0)
        glScalef(escala[2], escala[2], escala[2])
        glTranslatef(-6, 0, 0)
        
        glBegin(GL_QUADS)
        glVertex3f(self.vertices[0][0], self.vertices[0][1], self.vertices[0][2])
        glVertex3f(self.vertices[1][0], self.vertices[1][1], self.vertices[1][2])
        glVertex3f(self.vertices[2][0], self.vertices[2][1], self.vertices[2][2])
        glVertex3f(self.vertices[3][0], self.vertices[3][1], self.vertices[3][2])
        glEnd()

        glPopMatrix()
        

def tela():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)

    configCamera()
    desenhaEixos()
    triangulo.desenha()
    cubo.desenha()
    quadrado.desenha()

    glutSwapBuffers()


# Função fornecida por IA
def ray_intersects_box(origin, direction, min_b, max_b):
    tmin = -1e9
    tmax =  1e9

    for i in range(3):
        if direction[i] != 0:
            t1 = (min_b[i] - origin[i]) / direction[i]
            t2 = (max_b[i] - origin[i]) / direction[i]

            tmin = max(tmin, min(t1, t2))
            tmax = min(tmax, max(t1, t2))

    return tmax >= max(tmin, 0)


def escalaEstatica(min_v, max_v, centro, escala):
    novo_min = []
    novo_max = []

    for i in range(3):
        novo_min.append(
            centro[i] + escala * (min_v[i] - centro[i])
        )

        novo_max.append(
            centro[i] + escala * (max_v[i] - centro[i])
        )

    return novo_min, novo_max


def mouse(button, state, x, y):
    global escala
    escalaMin = [0, 0, 0]
    escalaMax = [0, 0, 0]

    model = glGetDoublev(GL_MODELVIEW_MATRIX)
    proj = glGetDoublev(GL_PROJECTION_MATRIX)
    view = glGetIntegerv(GL_VIEWPORT)
    y = view[3] - y

    perto = gluUnProject(x, y, 0.0, model, proj, view)
    longe = gluUnProject(x, y, 1.0, model, proj, view)
    direcao = [longe[0] - perto[0], longe[1] - perto[1], longe[2] - perto[2]]

    escalaMin[0], escalaMax[0] = escalaEstatica(triangulo.min, triangulo.max, [-5, 1, 0], escala[0] )
    escalaMin[1], escalaMax[1] = escalaEstatica(cubo.min, cubo.max, [0, 1, -1], escala[1] )
    escalaMin[2], escalaMax[2] = escalaEstatica(quadrado.min, quadrado.max, [6, 0, 0], escala[2] )

    if ray_intersects_box(perto, direcao, escalaMin[0], escalaMax[0]):

            if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
                escala[0] += 0.2

            if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN and escala[0] > 0.5:
                escala[0] -= 0.2

            glutPostRedisplay()

    if ray_intersects_box(perto, direcao, escalaMin[1], escalaMax[1]):
    
        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            escala[1] += 0.2
    
        if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN and escala[1] > 0.5:
            escala[1] -= 0.2

        glutPostRedisplay()

    if ray_intersects_box(perto, direcao, escalaMin[2], escalaMax[2]):

        if button == GLUT_LEFT_BUTTON and state == GLUT_DOWN:
            escala[2] += 0.2

        if button == GLUT_RIGHT_BUTTON and state == GLUT_DOWN and escala[2] > 0.5:
            escala[2] -= 0.2

        glutPostRedisplay()

    
triangulo = Triangulo()
cubo = Cubo()
quadrado = Quadrado()

glutInit()
glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
glutInitWindowSize(800, 600)
glutCreateWindow("Missao 4")

glutMouseFunc(mouse)
glutDisplayFunc(tela)
glEnable(GL_DEPTH_TEST)

glutMainLoop()