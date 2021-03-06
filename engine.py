import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *

#from cube import *

from shapes import *


if __name__ == "__main__":
    pygame.init()
    display = (700, 700)

    pygame.display.set_mode(display, DOUBLEBUF|OPENGL)
    #glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    # Pode utilizar o Perspective
    gluPerspective(45, display[0]/display[1], 0.1, 500.0 )
    glTranslate(0.0, 0.0, -50)

    #glEnable(GL_BLEND)
    #glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)


    # quad2 = Square(0, 0, 7)
    # quad = Rectangle(0, 0, 5,5)



    linex = Line(-100,0,0,100,0,0,color=(1,0,0))
    liney = Line(0,-100,0,0,100,0,color=(0,1,0))
    linez = Line(0,0,-100,0,0,100,color=(0,0,1))
    triangulo = Triangle(1, 6, 5)
    quadrado = Square(0,0,2)
    circulo = Circle(5,5,5,20)
    cubo = Cube(0,0,0,5)
    ponto = Vertex(2,2)
    esfera = Sphere(5,5,0,5,20)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    print("clicado")
                    #quad2.draw()


        mouseMove = pygame.mouse.get_rel()

        glRotate(mouseMove[0] * 0.2, 0.0, 1.0, 0.0)
        glRotate(mouseMove[1] * 0.2, 1.0, 0.0, 0.0)

        # glRotate(1,0,0,1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)


        #triangulo.draw() #Ok
        #triangulo.reflection() #ok
        #triangulo.translation(1,0,0) #ok
        #triangulo.rotation(1,'y') #ok
        #triangulo.scale(1.1,1.1,1.1) #ok
        #quadrado.draw() # OK
        #quadrado.reflection() #OK
        #quadrado.rotation(1,'y') #Ok
        #quadrado.translation(1,0) #OK
        #circulo.draw() #OK
        #circulo.reflection() #OK
        #circulo.rotation(1,'z') #OK
        #circulo.translation(1,0) #OK
        #cubo.draw() #OK
        #cubo.reflection(2) #NOT OK
        #cubo.translation(1,0,0) #OK
        #cubo.rotation(1,'y') #OK
        #esfera.draw() #OK
        #esfera.reflection(2)   #ok
        #esfera.rotation(1,'y')  #ok
        #esfera.translation(0,0,0) #ok



        linex.draw()
        liney.draw()
        linez.draw()



        pygame.display.flip()
        pygame.time.wait(10)
