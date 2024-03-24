import sys

N = int(sys.stdin.readline().strip())
layer = 1  
layer_end_room_number = 1

while N > layer_end_room_number:
    layer_end_room_number += 6 * layer  
    layer += 1 

print(layer)

