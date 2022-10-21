# csc132-itemframe
Test for Github Discord update integration


## GUI
- Contains a (variable) 16 x 16 pixel grid with assignable color values
#### Guide to Interact with API locally
- **Linux (RPi)**
    1. Make sure Google Chrome is installed
    2. Paste and run  in terminal
    ```
    google-chrome  --disable-web-security --user-data-dir="[some directory here]
    ```
    4. This should open up a new browser with the security that prevents local HTTP requests disabled
    5. Copy the file path to your ```index.html``` in the repository & paste it into the URL bar in the browser just opened. The should show you the webpage with the pixel grid
    6. Start the API with either of these commands:
    ```
    flask --app {Path to repo}/csc132-itemframe/API/main run
    ```
    ```
    flask --app {Path to repo}/csc132-itemframe/API/main run
    ```
    7. Hit the "Submit" button on the website
    8. You should get a message in the terminal you started the API in saying "POST" and "204"
    9. Go into the launch.json configurations change sudo to true in order run the rasp pi