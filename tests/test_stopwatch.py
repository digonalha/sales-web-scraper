import time
from src.app.utils.stopwatch import Stopwatch

def test_stopwatch_elapsed_time():
    #Arrange
    stopwatch = Stopwatch()

    #Act
    stopwatch.start()
    time.sleep(1)
    elapsed_time = stopwatch.stop()

    #Assert
    assert int(elapsed_time) > 0
