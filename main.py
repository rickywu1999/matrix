from display import *
from draw import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix()

print("Matrix:")
print_matrix(matrix)
print("")

print("Added an edge:")
add_edge(matrix,0,0,0,250,250,0)
print_matrix(matrix)
print("")

print("Added an edge:")
add_edge(matrix,0,500,0,250,250,0)
print_matrix(matrix)
print("")

matrix2 = new_matrix()
ident(matrix2)
print("Identity matrix:")
print_matrix(matrix2)
print("")

print("Multiply matrix by identity")
matrix3 = matrix_mult(matrix,matrix2)
print("Result:")
print_matrix(matrix3)
print("")

print("Multiply identity by matrix")
matrix4 = matrix_mult(matrix2,matrix)
print("Result:")
print_matrix(matrix4)
print("")

#actual picture
matrixA = new_matrix()

for i in range(100):
    add_edge(matrixA,500-5*i,500-5*i,0,5*i,0,0)
    add_edge(matrixA,500-5*i,500-5*i,0,0,5*i,0)
    add_edge(matrixA,5*i,5*i,0,500-5*i,500,0)
    add_edge(matrixA,5*i,5*i,0,500,500-5*i,0)
    add_edge(matrixA,500-5*i,5*i,0,0,500-5*i,0)
    add_edge(matrixA,500-5*i,5*i,0,5*i,500,0)
    add_edge(matrixA,5*i,500-5*i,0,500-5*i,0,0)
    add_edge(matrixA,5*i,500-5*i,0,500,5*i,0)

draw_lines( matrixA, screen, color )
display(screen)
