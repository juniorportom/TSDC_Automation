const compareImages = require("resemblejs/compareImages");
const fs = require("mz/fs");

async function getDiff(img1, img2, img_diff) {
    const options = {
        output: {
            errorColor: {
                red: 255,
                green: 0,
                blue: 255
            },
            errorType: "movement",
            transparency: 0.3,
            largeImageThreshold: 1200,
            useCrossOrigin: false,
            outputDiff: true
        },
        scaleToSameSize: true,
        ignore: "antialiasing"
    };

    // The parameters can be Node Buffers
    // data is the same as usual with an additional getBuffer() function
    const data = await compareImages(
        await fs.readFile(img1),
        await fs.readFile(img2),
        options
    );

    await fs.writeFile(img_diff, data.getBuffer());
}

module.exports = {
    getDiff
}