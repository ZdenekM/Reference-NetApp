import time
from abc import ABC

from era_5g_object_detection_common.image_detector import ImageDetector


class FpsTestDetector(ImageDetector, ABC):
    """
    Debug detector which returns the framerate of received stream.
    """

    def __init__(self, **kw):
        """
        Constructor

        Args:
            name (str): The name of the thread.
        """

        super().__init__(**kw)
        print("fps_test_detector")
        self.start_time = time.time()
        self.frames = 0

    def process_image(self, frame):
        """
        Counts the number of frames per seconds and returns the value
        each second.

        Args:
            frame (_type_): The received image

        Returns:
            list(tuple(bbox[], fps_value, class_id, class_name)): Number of received
                frames per second (once per second, empty list otherwise)
        """

        # Detect the faces
        self.frames += 1
        if time.time() - self.start_time > 1:
            fps = self.frames / (time.time() - self.start_time)
            print(f"FPS: {fps}")
            self.frames = 0
            self.start_time = time.time()
            return [([0, 0, 0, 0], fps, 0, "fps")]
