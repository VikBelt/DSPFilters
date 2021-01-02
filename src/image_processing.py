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
    [sg.Image(key="-IMAGE-")],[sg.Text('_'*80)], [sg.Text('Noise, Filters and Edge Detection')],
    [sg.Button("Add Noise"),sg.Button('Apply Median Filter'),sg.Button('Apply Gaussian Filter'),sg.Button('Edge Detection')],
    [sg.Text('Color Space Modifications')],
    [sg.Button("Grayscale"),sg.Button("RGB"),sg.Button("HSV"),sg.Button("LUV"),sg.Button("LAB"),sg.Button("XYZ")],
]

#frequency spectrum column
freq_column = [
    [sg.Text("Image FFT - Magnitude Spectrum")],
    [sg.Text(size=(40, 1), key="-FOUT-")],
    [sg.Image(key="-FREQ-")],
]

#full layout and window 
fix_dpi()
full_layout = [[sg.Column(file_column),sg.VSeperator(),sg.Column(image_column),sg.VSeperator(),sg.Column(freq_column),]]
window = sg.Window("PyImageProcessor",full_layout, resizable = True)

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
            freq_mag = generic_fft(filename)
            cv2.imwrite('freq_spec.png',freq_mag)
            window["-FOUT-"].update('freq_spec.png')   
            window["-FREQ-"].update(filename = 'freq_spec.png')
        except:
            pass

    #Add Gaussian Noise to the image
    if event == 'Add Noise':
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            image = cv2.imread(filename,cv2.IMREAD_GRAYSCALE)
            sp_image = salt_and_pepper(image)
            show_image(window,'noisy.png',sp_image)
            freq_mag = noisy_fft()
            cv2.imwrite('noisy_fft.png',freq_mag)
            window["-FOUT-"].update('noisy_fft.png')   
            window["-FREQ-"].update(filename = 'noisy_fft.png')
        except:
            pass
    
    #Apply 5x5 Median Filter to Noisy Image
    if event == 'Apply Median Filter':
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            #apply median filter
            blurred_image = median_filter(filename)
            show_image(window,'blurred.png',blurred_image)
            freq_mag = blurred_fft()
            cv2.imwrite('blurred_fft.png',freq_mag)
            window["-FOUT-"].update('blurred_fft.png')   
            window["-FREQ-"].update(filename = 'blurred_fft.png')
        except:
            pass

    #Apply 5x5 Gaussian Filter to Noisy Image
    if event == 'Apply Gaussian Filter':
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            #apply median filter
            gauss_image = gaussian_filter(filename)
            show_image(window,'gaussian.png',gauss_image)
            freq_mag = gauss_fft()
            cv2.imwrite('gaussian_fft.png',freq_mag)
            window["-FOUT-"].update('gaussian_fft.png')   
            window["-FREQ-"].update(filename = 'gaussian_fft.png')
        except:
            pass
    
    #Apply Canny Edge Detection to Image
    if event == 'Edge Detection':
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            #apply median filter
            edges = edge_detection(filename)
            show_image(window,'edges.png',edges)
            freq_mag = edge_fft()
            cv2.imwrite('edge_fft.png',freq_mag)
            window["-FOUT-"].update('edge_fft.png')   
            window["-FREQ-"].update(filename = 'edge_fft.png')
        except:
            pass
    
    #Grayscale
    if event == 'Grayscale':
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            #apply median filter
            gray = grayscale(filename)
            show_image(window,'gray.png',gray)
            freq_mag = gray_fft()
            cv2.imwrite('gray_fft.png',freq_mag)
            window["-FOUT-"].update('gray_fft.png')   
            window["-FREQ-"].update(filename = 'gray_fft.png')
        except:
            pass
    
    #RGB
    if event == 'RGB':
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            #apply median filter
            rgb = to_rgb(filename)
            show_image(window,'rgb.png',rgb)
            freq_mag = rgb_fft()
            cv2.imwrite('rgb_fft.png',freq_mag)
            window["-FOUT-"].update('rgb_fft.png')   
            window["-FREQ-"].update(filename = 'rgb_fft.png')
        except:
            pass
    
    #HSV
    if event == 'HSV':
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            #apply median filter
            hsv = to_hsv(filename)
            show_image(window,'hsv.png',hsv)
            freq_mag = hsv_fft()
            cv2.imwrite('hsv_fft.png',freq_mag)
            window["-FOUT-"].update('hsv_fft.png')   
            window["-FREQ-"].update(filename = 'hsv_fft.png')
        except:
            pass

    #LUV
    if event == 'LUV':
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            #apply median filter
            luv = to_luv(filename)
            show_image(window,'luv.png',luv)
            freq_mag = lab_fft()
            cv2.imwrite('luv_fft.png',freq_mag)
            window["-FOUT-"].update('luv_fft.png')   
            window["-FREQ-"].update(filename = 'luv_fft.png')
        except:
            pass

    #LAB
    if event == 'LAB':
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            #apply median filter
            lab = to_lab(filename)
            show_image(window,'lab.png',lab)
            freq_mag = lab_fft()
            cv2.imwrite('lab_fft.png',freq_mag)
            window["-FOUT-"].update('lab_fft.png')   
            window["-FREQ-"].update(filename = 'lab_fft.png')
        except:
            pass
        #LAB

    if event == 'XYZ':
        try:
            filename = os.path.join(values["-FOLDER-"], values["-FILE LIST-"][0])
            #apply median filter
            xyz = to_xyz(filename)
            show_image(window,'xyz.png',xyz)
            freq_mag = xyz_fft()
            cv2.imwrite('xyz_fft.png',freq_mag)
            window["-FOUT-"].update('xyz_fft.png')   
            window["-FREQ-"].update(filename = 'xyz_fft.png')
        except:
            pass

    #program exit
    if event == sg.WINDOW_CLOSED or event == 'Close Program':
        break  

#close program and quit
window.close()
