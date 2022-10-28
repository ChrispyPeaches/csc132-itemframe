API_URL = "http://127.0.0.1:5000"
API_PRESET = "/preset"
API_PRESET_LIST = "/presetlist"
API_GET_PRESET_IMG = "/presetimg"
PIXEL_GRID_HEIGHT = 16
PIXEL_GRID_LENGTH = 16

// Initialize the preset list for search filtering
presets = [];
// Grab the search filtering input
input = document.getElementById('filter-sidebar-input');

// Run when page loads
$(document).ready(function () {
    // Generates grid for assigning colors to pixels
    $("#pixel-grid-container").html(generatePixelGrid());
    // Gets and displays list of presets from 
    getPresetList();
    // Assign the search input to filter the preset list
    // when something is typed inside.
    input.addEventListener('keyup', filterUsers)

});

// Filters the preset list in the sidebar based on the search bar input in real-time
function filterUsers(event) {
    keyword = input.value.toLowerCase();
    presetsShown = presets.filter(function (preset) {
        preset = preset.toLowerCase();
        return preset.indexOf(keyword) > -1;
    });
    presetsHidden = _.reject(presets, function (preset) {
        preset = preset.toLowerCase();
        return preset.indexOf(keyword) > -1;
    });
    console.log(presetsHidden)
    renderFilteredLists(presetsShown, presetsHidden);
}

// Show or hide presets given in list parameters
function renderFilteredLists(presetsShown, presetsHidden) {
    presetsShown.forEach(function (i) {
        $(`#preset-${i}`).css('visibility', 'visible');
    });
    presetsHidden.forEach(function (i) {
        $(`#preset-${i}`).css('visibility', 'hidden');
    });
}

// Generates grid of pixels with dimensions: PIXEL_GRID_HEIGHT x PIXEL_GRID_LENGTH
function generatePixelGrid() {
    htmlString = ``;
    // Loops over and creates each row of pixels
    for (let i = 0; i < PIXEL_GRID_HEIGHT; i++) {
        htmlString += `<div class="row pixel-row" id="matrix-${i}-row">`;
        if (i % 2 == 0) {
            // Loops over and creates each pixel in each row
            for (let j = PIXEL_GRID_LENGTH - 1; j >= 0; j--) {
                htmlString +=
                    `
            <div class="ratio ratio-1x1  col pixel-box pixel">
                <input class="pixel-input" id="pix[${PIXEL_GRID_LENGTH * i + j}]" name="pix[${PIXEL_GRID_LENGTH * i + j}]" type="color" value="#000000">
            </div>
            `;
            };
        }
        else {
            // Loops over and creates each pixel in each row
            for (let j = 0; j < PIXEL_GRID_LENGTH; j++) {
                htmlString +=
                    `
            <div class="ratio ratio-1x1  col pixel-box pixel">
                <input class="pixel-input" id="pix[${PIXEL_GRID_LENGTH * i + j}]" name="pix[${PIXEL_GRID_LENGTH * i + j}]" type="color" value="#000000">
            </div>
            `;
            };
        }

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
        presets.push(keyValPair.presetName)
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
// Sticks the name of the preset into the input field under the create/edit preset form. 
function getPreset(ele) {
    presetName = $(ele).children('p').text();
    $('#preset-name-input').val(presetName)
    $.ajax({
        type: "GET",
        url: `${API_URL}${API_PRESET}?presetName=${presetName}`,
        // On a successful request, do the following.
        success: function (response) {
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

function createOrEditPreset() {
    data =
    {
        presetName: `${$('#preset-name-input')}`,
        pixels: []
    };
    data.pixels = $('#pixel-form').serializeArray();
    $.ajax({
        type: "POST",
        url: API_URL + API_PRESET,
        data: JSON.stringify(data),
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
        },
        // On a failed request, do the following.
        error: function (xhr, resp, text) {
            console.log(text)
        }
    });
}

function clearPixelGrid() {
    $("#pixel-form input").each(function (index) {
        $(this).val("#000000");
    });
}
