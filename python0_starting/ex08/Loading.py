import os
import time


def formatTime(time: float) -> str:
    """
    Take float of time and transform it to time format as minuts:seconds MM:SS
    """
    minuts, seconds = divmod(time, 60)
    return f"{int(minuts):02d}:{int(seconds):02d}"


def ft_tqdm(lst: range) -> None:  # type: ignore
    """
    Print a loading bar from range statement with progress time, eta and speed
    """
    # Save the total of the range to reach
    i_totalPackets = len(lst)
    # Store the time when the function is called
    f_startTime = time.time()

    for i in lst:
        # Increment i to start from 1 and end at len(lst) and not len(lst - 1)
        i += 1

        # Store the progress percentage
        i_percentageProgress = int(i * 100 / i_totalPackets)
        s_percentageProgress = ' ' * (3 - len(str(i_percentageProgress)))
        s_percentageProgress += f"{i_percentageProgress}%"

        # Store the progress time to show
        f_progressTime = time.time() - f_startTime
        s_progressTime = formatTime(f_progressTime)

        # Store the progress speed
        f_progressSpeed = i / f_progressTime
        s_progressSpeed = f"{f_progressSpeed:.2f}it/s"

        # Store the eta time
        f_etaTime = (i_totalPackets - i) / f_progressSpeed
        s_etaTime = formatTime(f_etaTime)

        # Get the terminal width and calculate the place that stuff will take
        #  - The len of the packets progress
        #  - Len of progress time
        #  - Len of eta
        #  - Len of progress speed
        #  - 14 chars to complete format as : / \ ...
        i_terminalWidth = os.get_terminal_size().columns \
            - (len(str(i_totalPackets)) * 2) \
            - len(s_progressTime) \
            - len(s_etaTime) \
            - len(s_progressSpeed) \
            - 14

        # Store the chars for the progress bar
        i_progressBarSize = int(i / i_totalPackets * i_terminalWidth)
        s_progressBar = '█' * i_progressBarSize \
            + ' ' * (i_terminalWidth - i_progressBarSize)

        print(f"{s_percentageProgress}|{s_progressBar}|",
              f"{i}/{i_totalPackets}",
              f"[{s_progressTime}<{s_etaTime}, {s_progressSpeed}]", end='\r')

        yield
