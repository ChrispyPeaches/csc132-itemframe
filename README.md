# LED Minecraft Item Frame
**Python Version: 3.9.12**
## First Time Setup
**Note: Setup designed for Raspberry Pi**
### App
1. Clone repo
2. Create and activate virtual environment
   i. Navigate to parent folder of the cloned repository 
   ii. Run the following commands 
        ```python3 -m venv csc132-itemframe```
            ```. csc132-itemframe/bin/activate```
3. Install dependencies
   - ```Flask```
   - ```flask_cors``` 
   - ```neopixel```
   - ```RPi.GPIO```
   - ```time```
   - ```unicodedata```
   - ```json```

### Circuitry
- Insert image of circuitry
## Run the app
#### Guide to interact with app locally
- **Linux (RPi)**
    1. Copy the file path to your ```index.html``` in the repository & paste it into the URL bar in the browser just opened. The should show you the webpage with the pixel grid
    2. Start the API with either of these commands:
    ```
    flask --app {Path to local repo}/csc132-itemframe/API/app run
    ```
    ```
    flask --app {Path to local repo}/csc132-itemframe/API/app run
    ```
    3. Hit the "Send to Matrix" button on the website

## About the App
### Website
- Contains a by default (variable size) 16 x 16 pixel grid with assignable color values
- A left sidebar containing a buttons:
  - One sends the grid of pixels to the item frame
  - The other opens a form to upload the grid of pixels as a preset with the given name

### API
##### Matrix Program
-The Matrix convert uses the adafruit neopixel library specifically for python
-In order to install the library you must use the command in the terminal 'pip3 install neopixel' and 'pip3 install pillow'
-Afterwards import the board module to initialize the pins on the bread-board
-The global variable is created based on the pin of the data wire and the number of led on the matrix
-There is a hex converter converter function takes RGB values and changes them to hex
- Then the main function runs through a for loop of all the pix values sent through json request parse the string to find the digit
-and turns the RGB to hex and and sends it to the matrix light it up
-The LTU Matrix converter is the program the api sends all of the presets and json request through to light up the board
##### Filesystem Program
