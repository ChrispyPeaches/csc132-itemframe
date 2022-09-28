$(document).ready(function () {
    // Generates grid for assigning colors to pixels
    $(".pixel-grid-container").html(
        `
        ${(function genHTMLString() {
            htmlString = ``;
            // Loops over and creates each row of pixels
            for (let i = 0; i < 16; i++) {
                htmlString += `<div class="row pixel-row" id="matrix-${i}-row">`;
                // Loops over and creates each pixel in each row
                for (let j = 0; j < 16; j++) {
                    htmlString +=
                        `
                    <div class="col pixel-box pixel">
                        <input class="pixel-input" id="color-input-${i}-${j}" type="color">
                    </div>
                    `;
                };
                htmlString +=
                    `
                </div>
                `;
            };
            return htmlString;
        })()}
    `

    );
});

