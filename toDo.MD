# Project To-Do List: Video Camera Control

## Phase 1: Core Functionality (Video Loading & Display)
- [ ] Fix `ui.py` structure and method definitions.
- [ ] Implement video loading mechanism in `MainWindow` and pass it to `VideoCanvas`.
- [ ] Implement `VideoCanvas` to render the current video frame using OpenCV and PySide6.
- [ ] Integrate `Project` model to store video information.

## Phase 2: Camera & Bounding Box (The "Virtual Camera")
- [ ] Implement the visual representation of the bounding box (the "Camera") on the `VideoCanvas`.
- [ ] Implement mouse interaction for moving the bounding box (Left click and drag).
- [ ] Implement mouse wheel interaction for zooming.
- [ ] Implement corner handles for resizing the bounding box.

## Phase 3: Navigation & Playback
- [ ] Add a seek bar (slider) to navigate through the video.
- [ ] Implement frame-by-frame navigation.

## Phase 4: Keyframing System
- [ ] Implement the ability to add keyframes at the current time.
- [ ] Implement interpolation between keyframes to animate the camera.
- [ ] Implement a way to visualize/manage keyframes (e.g., a timeline or list).

## Phase 5: Polish & Refinement
- [ ] Improve UI layout and aesthetics.
- [ ] Add error handling (e.g., for invalid video files).
- [ ] Ensure smooth rendering and interaction.
