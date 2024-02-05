// Load the CSV File using AJAX
function loadCSV() {
    $.ajax({
      url: 'C:\Users\sam\Desktop\DSR Ex try\test.csv',
      dataType: 'text',
      success: function(data) {
        processData(data);
      }
    });
  }
  
  // Process the CSV Data and Create Marker Points on the Globe
  function processData(csvData) {
    var csvRows = csvData.split('\n');
    for (var i = 1; i < csvRows.length; i++) {
      var rowData = csvRows[i].split(',');
      var wtuName = rowData[0];
      var latitude = parseFloat(rowData[1]);
      var longitude = parseFloat(rowData[2]);
      var altitude = parseFloat(rowData[3]);
  
      // Create Marker Point on the Globe
      var placemark = ge.createPlacemark('');
      placemark.setName(wtuName);
      var point = ge.createPoint('');
      point.setLatitude(latitude);
      point.setLongitude(longitude);
      point.setAltitude(altitude);
      placemark.setGeometry(point);
      ge.getFeatures().appendChild(placemark);
  
      // Attach Click Event Listener to the Marker Point
      google.earth.addEventListener(placemark, 'click', function(event) {
        showDetails(rowData);
      });
    }
  }
  
  // Show the Details Page with the Selected Row Data
  function showDetails(rowData) {
    var detailsContainer = document.getElementById('details-container');
    var details = document.getElementById('details');
    details.innerHTML = '<p>WTU Name: ' + rowData[0] + '</p>' +
                        '<p>Details: ' + rowData[4] + '</p>';
    detailsContainer.style.display = 'block';
  }
  
  // Load the Google Earth API and Initialize the Globe
  google.load('earth', '1', {'other_params':'sensor=false'}, function() {
    var ge = new google.earth.GEPlugin(document.getElementById('globe'));
    ge.getWindow().setVisibility(true);
    loadCSV();
  });
  