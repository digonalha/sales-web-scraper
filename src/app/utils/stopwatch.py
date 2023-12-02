from datetime import datetime
import logging

logger = logging.getLogger(__name__)

class Stopwatch:
    def __init__(self):
        self.start_time = None

    def start(self) -> None:
        self.start_time = datetime.now()
        logger.info("starting at %s", self.start_time.strftime("%d/%m/%y %H:%M:%S"))

    def stop(self) -> int:
        if self.start_time is not None:
            self.end_time = datetime.now()

            elapsed_time = (self.end_time-self.start_time).total_seconds()

            hours = int(elapsed_time // 3600)
            minutes = int((elapsed_time % 3600) // 60)
            seconds = int(elapsed_time % 60)

            logger.info("finished at %s (elapsed time: %s)", self.end_time.strftime("%d/%m/%y %H:%M:%S"), f"{hours}h {minutes}m {seconds}s")
            
            return elapsed_time