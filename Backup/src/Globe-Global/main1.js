// obtain the canvas element and its context
const canvas = document.getElementById("globe");
const context = canvas.getContext("2d");

// obtain the map image
const mapImage = new Image();
mapImage.src = "https://maps.googleapis.com/maps/api/staticmap?center=40.714728,-73.998672&zoom=12&size=600x600&maptype=roadmap&key=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";

// wait for the map image to load
mapImage.onload = function () {
  // draw the map image onto the canvas
  context.drawImage(mapImage, 0, 0, canvas.width, canvas.height);
};

// add event listener for clicks on the canvas
canvas.addEventListener("click", function (event) {
  // obtain the click coordinates
  const rect = canvas.getBoundingClientRect();
  const x = event.clientX - rect.left;
  const y = event.clientY - rect.top;

  // obtain the latitude and longitude values from the click coordinates
  const latitude = // TODO: implement logic to obtain latitude value from click coordinates
  const longitude = // TODO: implement logic to obtain longitude value from click coordinates

  // redirect to a new page with the coordinates as a parameter in the URL
  window.location.href = `newpage.html?lat=${latitude}&lng=${longitude}`;
});
