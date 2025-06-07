import uproot
import numpy as np
from typing import Optional, Dict, Any
from PyTracker.QVision.plot import HitMatrix

### In this version of ReadROOT, we will only be using UpRoot and PyROOT to read in ROOT files and perform basic operations.

class TreeWrapper:
    def __init__(self, tree: uproot.behaviors.TTree.TTree):
        self.tree = tree
    
    def branch_info(self) -> None:
        """Get all branches from the tree."""
        return print(f"{'Branch':<15} {'Type':<15}\n{'-'*30}\n" + 
                    "\n".join([f"{branch:<15} {self.tree[branch].typename:<15}" 
                              for branch in self.tree.keys()]))
    
    def get_branches(self) -> dict[str, Any]:
        """Get all branches from the tree."""
        return {branch: self.tree[branch].array() for branch in self.tree.keys()}
    
    def read_branch(self, branch_name: str) -> np.ndarray:
        """Read data from a specific branch."""
        try:
            return self.tree[branch_name].array()
        except KeyError:
            raise KeyError(f"Branch '{branch_name}' not found in tree")
    
    def HitMatrix(self, event_number: int) -> HitMatrix:
        """
        Create a HitMatrix object for visualizing hits in a specific event.
        
        Args:
            event_number (int): The event number to visualize
            
        Returns:
            HitMatrix: A HitMatrix object that can be used to plot the hit pattern
        """
        return HitMatrix(self, event_number)


class ReadROOT:
    def __init__(self, file_path: str):
        """
        Initialize the ReadROOT class with a ROOT file path.
        
        Args:
            file_path (str): Path to the ROOT file
        """
        self.file_path = file_path
        try:
            self.file = uproot.open(file_path)
        except Exception as e:
            raise FileNotFoundError(f"Could not open ROOT file: {file_path}. Error: {str(e)}")
    
    def get_tree(self, tree_name: str) -> TreeWrapper:
        """
        Get a specific tree from the ROOT file.
        
        Args:
            tree_name (str): Name of the tree to access
            
        Returns:
            TreeWrapper: A wrapper around the requested tree object
            
        Raises:
            KeyError: If the tree name doesn't exist in the file
        """
        try:
            return TreeWrapper(self.file[tree_name])
        except KeyError:
            raise KeyError(f"Tree '{tree_name}' not found in file: {self.file_path}")
    
    def close(self):
        """Close the ROOT file."""
        if hasattr(self, 'file'):
            self.file.close()

        
    
    

        


