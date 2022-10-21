API_URL = "http://127.0.0.1:5000"
API_PRESET = "/preset"
API_PRESET_LIST = "/presetlist"
API_GET_PRESET_IMG = "/presetimg"
PIXEL_GRID_HEIGHT = 16
PIXEL_GRID_LENGTH = 16

// Run when page loads
$(document).ready(function () {
    // Generates grid for assigning colors to pixels
    $("#pixel-grid-container").html(generatePixelGrid());
    // Gets and displays list of presets from 
    getPresetList();

});

// Generates grid of pixels with dimensions: PIXEL_GRID_HEIGHT x PIXEL_GRID_LENGTH
function generatePixelGrid() {
    htmlString = ``;
    // Loops over and creates each row of pixels
    for (let i = 0; i < PIXEL_GRID_HEIGHT; i++) {
        htmlString += `<div class="row pixel-row" id="matrix-${i}-row">`;
        // Loops over and creates each pixel in each row
        for (let j = 0; j < PIXEL_GRID_LENGTH; j++) {
            htmlString +=
                `
            <div class="ratio ratio-1x1  col pixel-box pixel">
                <input class="pixel-input" id="pix[${PIXEL_GRID_LENGTH * i + j}]" name="pix[${PIXEL_GRID_LENGTH * i + j}]" type="color" value="#923a3a">
            </div>
            `;
        };
        htmlString +=
            `
        </div>
        `;
    };
    return htmlString;
}

// Get's list of presets from API
function getPresetList() {
    $.ajax({
        type: "GET",
        url: API_URL + API_PRESET_LIST,
        data: JSON.stringify("None"),
        dataType: "json",
        contentType: 'application/json;charset=UTF-8',
        // On a successful request, do the following.
        success: function (response) {
            loadPresetList(response);
        },
        // On a failed request, do the following.
        error: function (xhr, resp, text) {
            console.log(text)
        }
    });
}

// Insert presets from API into preset list sidebar
// Retrieves image from API
function loadPresetList(response) {
    htmlString = ``;
    $.each(response, function (index, keyValPair) {
        htmlString +=
            `
            <a class="preset-container list-group-item-action py-2 ripple" aria-current="true" id="preset-${keyValPair.presetName}" onmousedown="getPreset(this)">
                <img src="${API_URL}${API_GET_PRESET_IMG}?presetName=${keyValPair.presetName}" />
                <p>${keyValPair.presetName}</p>
            </a>
            `;
    });
    $('#preset-list-container').html(htmlString);
}

// Get function called when a preset is selected and calls
// loadPreset() so the values of that preset can be attached
// to the pixel inputs.
function getPreset(ele) {
    dataString = `[{"presetName" : "${$(ele).children('p').text()}"}]`;
    $.ajax({
        type: "GET",
        url: API_URL + API_PRESET,
        data: dataString,
        dataType: "json",
        contentType: 'application/json;charset=UTF-8',
        // On a successful request, do the following.
        success: function (response) {
            console.log(response)
            loadPreset(response)
        },
        // On a failed request, do the following.
        error: function (xhr, resp, text) {
            console.log(text)
        }
    });
}

// Given a set of values, it'll change the pixel inputs to the
// specified values.
// The paramenter "data" is essentially a JSON string detailing
// the name of the input element intended to be changed and the
// value that it is intended to be changed to.
function loadPreset(response) {
    $.each(response, function (index, keyValPair) {
        $(`input[name="${keyValPair.name}"]`).val(keyValPair.value);
    });
}

// Submits the HTTP Request of the pixels' colors to API
function submitPixelValues() {
    // Sends the request and gets a response without refreshing the web page.
    $.ajax({
        type: "POST",
        url: API_URL,
        data: JSON.stringify($('#pixel-form').serializeArray()),
        dataType: "json",
        contentType: 'application/json;charset=UTF-8',
        // On a successful request, do the following.
        success: function (response) {
            console.log(response)
        },
        // On a failed request, do the following.
        error: function (xhr, resp, text) {
            console.log(text)
        }
    });
}