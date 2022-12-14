from math import floor
from typing import NoReturn

import cv2
import numpy as np

from utils import CFEVideoConfig


def open_video(path: str) -> cv2.VideoCapture:
    """Opens a video file.

    Args:
        path: the location of the video file to be opened

    Returns:
        An opencv video capture file.
    """
    video_capture = cv2.VideoCapture(path)
    if not video_capture.isOpened():
        raise RuntimeError(f'Video at "{path}" cannot be opened.')
    return video_capture


def get_frame_dimensions(video_capture: cv2.VideoCapture) -> tuple[int, int]:
    """Returns the frame dimension of the given video.

    Args:
        video_capture: an opencv video capture file.

    Returns:
        A tuple containing the height and width of the video frames.

    """
    return video_capture.get(cv2.CAP_PROP_FRAME_WIDTH), video_capture.get(
        cv2.CAP_PROP_FRAME_HEIGHT
    )


def get_frame_display_time(video_capture: cv2.VideoCapture) -> int:
    """Returns the number of milliseconds each frame of a VideoCapture should be displayed.

    Args:
        video_capture: an opencv video capture file.

    Returns:
        The number of milliseconds each frame should be displayed for.
    """
    frames_per_second = video_capture.get(cv2.CAP_PROP_FPS)
    return floor(1000 / frames_per_second)


def is_window_open(title: str) -> bool:
    """Checks to see if a window with the specified title is open."""

    # all attempts to get a window property return -1 if the window is closed
    return cv2.getWindowProperty(title, cv2.WND_PROP_VISIBLE) >= 1


def main(video_path: str, title: str) -> NoReturn:
    """Displays a video at half size until it is complete or the 'q' key is pressed.

    Args:
        video_path: the location of the video to be displayed
        title: the title to display in the video window
    """

    video_capture = open_video(video_path)
    width, height = get_frame_dimensions(video_capture)
    wait_time = get_frame_display_time(video_capture)

    try:
        # read the first frame
        success, frame = video_capture.read()

        # create the window
        cv2.namedWindow(title, cv2.WINDOW_AUTOSIZE)

        # run whilst there are frames and the window is still open
        while success and is_window_open(title):

            print(frame[0, 0]) #numpyarray
            start_cord_x = 0
            start_cord_y = 0
            color = (255, 0, 0) #BGR
            stroek = 2
            w = 200
            h = 150
            end_cord_x = start_cord_x + w
            end_cord_y = start_cord_y + h
            cv2.rectangle(frame, (start_cord_x, start_cord_y), (end_cord_x, end_cord_y), colour
            print(frame[start_cord_x:end_cord_x, start_cord_y:end_cord_y])
            cv2.inshow('frame', frame)
            if cv2.waitkey(20) & 0xFF == ord('q')
                break

            #when everything's done release the capture
    
    finally:
        video_capture.release()
        cv2.destroyAllWindows()

    
        frame_h, frame_w, frame_c = frame.shape
        overlay = np.zeros(frame_h, frame_w, 4), dtype = 'uint8'
        overlay[0:5, 0:5] = (255, 255, 0, 1) #B,G,R,Alpha
        #overlay[start_y:end_y, start_x:end_x]
               
        # shrink it
        smaller_image = cv2.resize(frame, (floor(width // 2), floor(height // 2)))

        # display it
        cv2.imshow(title, smaller_image)

        # test for quit key
        if cv2.waitKey(wait_time) == ord("q"):
            break

        # read the next frame
        success, frame = video_capture.read()


if __name__ == "__main__":
    VIDEO_PATH = "resources/video_1.mp4"
    main(VIDEO_PATH, "My Video")
