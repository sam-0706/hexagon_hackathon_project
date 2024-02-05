<!DOCTYPE html>
<html>
<head>
	<meta charset="utf-8">
	<title>Google Earth API Example</title>
	<style type="text/css">
		#map {
			height: 500px;
			width: 100%;
		}
	</style>
	<script type="text/javascript" src="https://www.google.com/jsapi?key = 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
  "></script>
	<script type="text/javascript">
		google.load("earth", "1");

		function init() {
			google.earth.createInstance('map', initCB, failureCB);
		}

		function initCB(instance) {
			var placemark = instance.createPlacemark('');
			placemark.setName('WTU_name');
			var point = instance.createPoint('');
			point.setLatitude(37.7793);
			point.setLongitude(-122.4192);
			placemark.setGeometry(point);
			instance.getFeatures().appendChild(placemark);

			google.earth.addEventListener(instance.getView(), 'viewchange', function() {
				var lat = instance.getView().copyAsLookAt(google.earth.ALTITUDE_RELATIVE_TO_GROUND).getLatitude();
				var lng = instance.getView().copyAsLookAt(google.earth.ALTITUDE_RELATIVE_TO_GROUND).getLongitude();
				console.log(lat + ", " + lng);
			});

			google.earth.addEventListener(placemark, 'click', function(event) {
				window.location.href = "details.html?WTU_id=" + encodeURIComponent(WTU_id);
			});

			instance.getNavigationControl().setVisibility(google.earth.VISIBILITY_SHOW);
			instance.getLayerRoot().enableLayerById(instance.LAYER_BORDERS, true);
			instance.getLayerRoot().enableLayerById(instance.LAYER_ROADS, true);
		}

		function failureCB(errorCode) {
		}

		google.setOnLoadCallback(init);
	</script>
</head>
<body>
	<div id="map"></div>
</body>
</html>
