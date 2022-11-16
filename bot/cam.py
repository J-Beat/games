# Python program to capture a single image
# using pygame library
  
# importing the pygame library
import pygame
import pygame.camera
  
def get_photo(filename: str) -> None:
    # initializing  the camera
    pygame.camera.init()
    
    # make the list of all available cameras
    camlist = pygame.camera.list_cameras()
    print(camlist)
    
    # if camera is detected or not
    if camlist:
    
        # initializing the cam variable with default camera
        cam = pygame.camera.Camera(camlist[0], (1920, 1080))
    
        # opening the camera
        cam.start()
    
        # capturing the single image
        image = cam.get_image()
    
        # saving the image
        pygame.image.save(image, f'image/{filename}.jpg')
        cam.stop()
    
    # if camera is not detected the moving to else part
    else:
        print("No camera on current device")