# Vision-Vocalizer




## Problem Statemnet: 
Developing an inclusive mobile app for the visually impaired, utilizing OpenCV for real-time object recognition through the device camera, empowering users with auditory feedback for enhanced navigation and object identification.

## Background Study: 
- *Seeing AI by Microsoft:* Provides audio descriptions of the surroundings, reads handwritten notes, and identifies products through barcode scanning. Limited to smartphone or tablet use and specific tasks like object recognition and text reading.
- *Microsoft Soundscape:* Creates audio maps of the environment for outdoor navigation, primarily relying on smartphone GPS capabilities.
- *Braille Displays and Keyboards:* Enable tactile reading of digital content but are limited by availability, affordability, and hardware requirements.
- *Bluetooth Beacons:* Offer precise indoor navigation in specific locations but require infrastructure deployment and are limited to certain venues.

Challenges and trends in the field include the increasing prevalence of visual impairment due to aging populations, the affordability and accessibility of smartphone-based solutions, and the need for further research to improve the quality of life for visually impaired individuals.

[Paper 1](https://arxiv.org/pdf/2212.04745v2.pdf)
[Paper 2](https://www.researchgate.net/publication/355102026_Computer_Vision_for_Supporting_Visually_Impaired_People_A_Systematic_Review)

## Design:
- Real-time Object Recognition: Leverage OpenCV to analyze the camera feed and identify objects in the user's surroundings.
- Auditory Feedback: Convert recognized objects into clear, concise voice descriptions using Text-to-Speech (TTS) functionality.
- Provide turn-by-turn directions through TTS.
- The app will leverage built-in Android accessibility features, like TalkBack and Screen Reader compatibility, to ensure a smooth and informative experience for users with visual impairments.


![Diagram 1](https://github.com/swaraj-khan/Vision-Vocalizer/assets/94361805/9b7a46be-a751-4e53-9a43-3c3030f7ded6)


![Diagram 2](https://github.com/swaraj-khan/Vision-Vocalizer/assets/94361805/f0e2deeb-035d-49b2-922f-86955014281b)

detection model to classify objects in the images and TensorFlow APIs to implement it. The model is based on the COCO dataset which requires additional libraries like OpenCV, Pyttsx3 and Tesseract for image processing, voice generation and optical character recognition respectively.


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
