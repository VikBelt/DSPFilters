#imports
import matplotlib as plt
from image_processing import *
import PySimpleGUI as sg
import os.path



sg.theme('LightGrey1') 
#file selection column
file_column = [
    [sg.Text("Select an Image"),sg.In(size=(25, 1), enable_events=True, key="-FOLDER-"),sg.FolderBrowse(),],
    [sg.Listbox(values=[], enable_events=True, size=(40, 20), key="-FILE LIST-")], [sg.Button('Close Program')],
]

#image viewing column
image_column = [
    [sg.Text("Load an image, then press a button below to modify the image.")],
    [sg.Text(size=(40, 1), key="-TOUT-")],
    [sg.Image(key="-IMAGE-")],
    [sg.Button("Add Noise"),sg.Button('Apply Median Filter'),sg.Button('Apply Gaussian Filter'),sg.Button('Edge Detection')],
]

#full layout and window 
fix_dpi()
full_layout = [[sg.Column(file_column),sg.VSeperator(),sg.Column(image_column),]]
window = sg.Window("V.B. Image Processor",full_layout, resizable = False)

#event loop
while True:
    event,values = window.read()
    if event == "-FOLDER-":
        folder = values["-FOLDER-"]
        try:
            # Get list of files in folder
            file_list = os.listdir(folder)
        except:
            file_list = []

        fnames = [
            f
            for f in file_list
            if os.path.isfile(os.path.join(folder, f))
            and f.lower().endswith((".png"))
        ]

        window["-FILE LIST-"].update(fnames)

    elif event == "-FILE LIST-":  # A file was chosen from the listbox
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            window["-TOUT-"].update(filename)   
            window["-IMAGE-"].update(filename=filename)
        except:
            pass

    #Add Gaussian Noise to the image
    if event == 'Add Noise':
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
            cv2.imwrite('noisy.png',salt_and_pepper(image))
            window["-TOUT-"].update('noisy.png')   
            window["-IMAGE-"].update(filename='noisy.png')
        except:
            pass
    
    #Apply 5x5 Median Filter to Noisy Image
    if event == 'Apply Median Filter':
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            #apply median filter
            blurred_image = median_filter(filename)
            cv2.imwrite('blurred.png',blurred_image)
            window["-TOUT-"].update('blurred.png')   
            window["-IMAGE-"].update(filename='blurred.png')
        except:
            pass

    #Apply 5x5 Gaussian Filter to Noisy Image
    if event == 'Apply Gaussian Filter':
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            #apply median filter
            gauss_image = gaussian_filter(filename)
            cv2.imwrite('gaussian.png',gauss_image)
            window["-TOUT-"].update('gaussian.png')   
            window["-IMAGE-"].update(filename='gaussian.png')
        except:
            pass

    #program exit
    if event == sg.WINDOW_CLOSED or event == 'Close Program':
        break  

#close program and quit
window.close()
