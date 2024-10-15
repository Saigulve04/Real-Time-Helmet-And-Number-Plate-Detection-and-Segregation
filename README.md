Steps for Setting Up the Project:
Install YOLOv7:

Download YOLOv7 from the official repository: WongKinYiu/yolov7.
Open the downloaded YOLOv7 repository in VS Code (or any preferred IDE).
Add Custom Python Files:

Paste the following files into the YOLOv7 folder:
flaskapp.py
flaskaap1.py
flaskaap2.py
flaskaap3.py
hubconfCustom.py
hubconfcustomweb.py
These Python scripts likely set up Flask web services, handle model interactions, and manage object detection requests.
Change Model Weights:

Replace the model weights to epochs80.pt in the custom scripts hubconfCustom.py and hubconfcustomweb.py.
If you have a different trained model (best.pt), you can replace it with your custom dataset.
HTML Files for Web Interface:

Paste the three provided HTML files into the templates folder of the YOLOv7 project (used by Flask to render the web interface).
Customize the HTML as needed (e.g., adding images or modifying the UI).
Run the Flask Application:

Execute the code on a localhost environment.
Ensure Flask and all necessary libraries are installed (YOLOv7 dependencies, Flask, etc.).
Additional Customization:
You can modify the HTML files and Flask scripts to fit your requirements (e.g., adjust the interface, integrate additional functionality).
If you’re training with a new dataset, replace the epochs80.pt file with your own .pt file from your trained YOLOv7 model.
