# Playing with Machine Learning

This week, we're going to use ml5.js, a user-friendly browser-based machine learning library to draw emojis on our faces.

![mask](images/mask.gif).

## ml5.js?

ml5 is a javascript library that's tries to make using pre-trained machine learning models in the browser as simple as possible. It's built on top of tensorflow.js, the most performant low-level machine learning library out there, so it's fast. But, it has a user-friendly API, and it doesn't require you to know much about machine learning at all to use it. Hooray!

## Prereqs

Your favorite browser and text editor. Make sure your browser has permission to access your webcam. We'll start from an empty text editor, so you can follow along from scratch, if you like.

## Agenda

Our goal is to make the video above: a webpage that draws emojis over faces it detects in the scene. In order to do that, we'll have to:

1. Install two third-party libraries! We'll get `jquery` and `ml5` from a CDN.

2. Interact with our webcams! We'll use the `UserMedia` API to connect to your computer's webcam. More on [UserMedia](https://developer.mozilla.org/en-US/docs/Web/API/MediaDevices/getUserMedia) here.

3. Set up `poseNet` model (learn more about it [here](https://ml5js.org/reference/api-PoseNet/)). We'll use an ml5 model that's pre-trained to detect human poses to help us identify keypoints on our faces that we'll anchor our emojis to.

4. We'll draw the keypoints to the screen to verify that everything's working properly using jQuery.

5. We'll need to do some very light math to figure out a way to scale our emoji's so that they get smaller when our heads are farther away.

6. Finally, We'll draw the emoji to the screen using our keypoints and our scale calculation.

Thats it for this week. Hope you'll join us!
