var emoji = "🤖";

$(document).ready(function() {
  var WIDTH = 640;
  var HEIGHT = 480;
  var constraints = {video: {width: WIDTH, height: HEIGHT}};
  var video = document.getElementById("video") // $("#id")
  var videoWrapper = document.getElementById("video-wrapper");

  setupWebcam(video, constraints);

  var posenet = ml5.poseNet(video, function() {
    posenet.on("pose", function(results) {
      if (results.length > 0) {
        var result = results[0];
        console.log(result);
        // drawKeypoint('nose', result.pose.nose);
        // drawKeypoint('leftEar', result.pose.leftEar);
        var scale = getScale(result.pose.leftEar, result.pose.rightEar);
        drawEmoji('hamburger', result.pose.nose, scale);
        // drawKeypoint('rightEar', result.pose.rightEar);
        // drawKeypoint('leftEar', result.pose.leftEar);
        // drawKeypoint('rightEye', result.pose.rightEye);
      }
    })
  });
})



function getScale(left, right) {
  var distance = Math.sqrt(Math.pow(right.x - left.x, 2) + Math.pow(right.y - left.y, 2));
  var scaleFactor = distance / 135;

  return (scaleFactor * 10) + "em";
}



function drawEmoji(name, keypoint, scale) {
  var element = $('#emoji-' + name);

  if (element.length == 0) {
    element = $('<div>')
      .addClass('detection')
      .addClass('emoji')
      .attr('id', 'emoji-' + name)
      .text(emoji);

    $('#video-wrapper').append(element);
  }

  element
    .css('top', keypoint.y)
    .css('left', keypoint.x)
    .css('font-size', scale); // TODO: update this to handle scale
}



function drawKeypoint(name, keypoint) {
  var element = $('.keypoint-' + name);

  if (element.length == 0) {

    element = $('<div>')
      .addClass('detection')
      .addClass('keypoint')
      .addClass('keypoint-' + name);

    $('#video-wrapper').append(element);
  }

  element
    .css('top', keypoint.y)
    .css('left', keypoint.x);
}























function setupWebcam(video, constraints) {
  navigator.mediaDevices.getUserMedia(constraints)
    .then(function(stream) {
      video.width = constraints.video.width;
      video.height = constraints.video.height;
      video.srcObject = stream;
    })
    .catch(function(err) {
      console.error("No Webcam!");
    });
}
