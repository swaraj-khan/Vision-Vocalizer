# Vision-Vocalizer




## Problem Statemnet: 
Developing an inclusive mobile app for the visually impaired, utilizing OpenCV for real-time object recognition through the device camera, empowering users with auditory feedback for enhanced navigation and object identification.

## Background Study: 


[Paper 1](https://arxiv.org/pdf/2212.04745v2.pdf)
[Paper 2](https://www.researchgate.net/publication/355102026_Computer_Vision_for_Supporting_Visually_Impaired_People_A_Systematic_Review)

## Design:
- Real-time Object Recognition: Leverage OpenCV to analyze the camera feed and identify objects in the user's surroundings.
- Auditory Feedback: Convert recognized objects into clear, concise voice descriptions using Text-to-Speech (TTS) functionality.
- Provide turn-by-turn directions through TTS.
- The app will leverage built-in Android accessibility features, like TalkBack and Screen Reader compatibility, to ensure a smooth and informative experience for users with visual impairments.

## Solution:
A real-time object detection system with distance calculation and voice alerts. Key components and technologies include:
- Image/Video Capture: likely through a camera integrated with a mobile device.
- Object Detection Model:  A machine learning model (potentially SSD MobileNet or similar) for real-time identification.
- Distance Calculation:  Algorithmic estimation of the distance between the user and detected objects.
- Voice Output:  Text-to-speech system to provide auditory alerts about object type and proximity.

---

## Team Members and roles:
- **Product Owner** - Swaraj
- **Scrum Master** - Sambram
- **Developer** - Sourabh, Ananya and Shreepaada
- **Quality and compliance** - Soumyo 
- **Operations** - Roshan
