def main():
    sideLength = float(input("Enter the side length of the cube: "))
    print(cubeVolume(sideLength))

def cubeVolume(sideLength) :
    if sideLength >= 0:
        volume = sideLength ** 3
    else:
        volume = 0
    return volume

main()
