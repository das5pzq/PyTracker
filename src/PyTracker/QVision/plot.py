import matplotlib.pyplot as plt
import numpy as np
import matplotlib.colors as mcolors

def HitMatrix(self, event_number: int, show_plot: bool = False) -> plt.Figure:
    """
    Plot the hit matrix for a specific event.
    
    Args:
        event_number (int): The event number to plot
        show_plot (bool): Whether to display the plot immediately. Default is False.
        
    Returns:
        plt.Figure: The matplotlib figure object containing the plot
    """

    detector_id = self.read_branch("detectorID")[event_number]
    element_id = self.read_branch("elementID")[event_number]
        
    if len(detector_id) == 0 or len(element_id) == 0:
        print(f"No data found for event {event_number}")
        return None
    
    # Prepare a 2D matrix (201 x 62), shifting indices to start from 1
    matrix = np.zeros((201, 62))
    for det_id, elem_id in zip(detector_id, element_id):
        det_index = det_id - 1  # Shift detector ID to start from 1
        elem_index = elem_id - 1  # Shift element ID to start from 1
        if 0 <= det_index < 62 and 0 <= elem_index < 201:
            matrix[elem_index, det_index] = 1  # Mark seen hits
    
    colors = [(0, 0, 1), (1, 1, 0.8)]  # Blue for 0, Light Yellow for 1
    cmap = mcolors.LinearSegmentedColormap.from_list("custom_cmap", colors, N=2)
        
    # Create and return the figure
    fig = plt.figure(figsize=(10, 8))
    plt.imshow(matrix, aspect="auto", cmap=cmap, origin="lower")
    plt.title(f"Event {event_number}")
    plt.xlabel("Detector ID (1 to 62)")
    plt.ylabel("Element ID (1 to 201)")
    plt.xticks(np.arange(0, 62, 10))
    plt.yticks(np.arange(0, 201, 20))

    plt.show()

    return fig
