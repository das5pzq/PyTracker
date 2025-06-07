from PyTracker import ReadROOT
import matplotlib.pyplot as plt
try:
    reader = ReadROOT("JPsi_dump.root")
except Exception as e:
    print(e)

tree = reader.get_tree("tree")

tree.branch_info()

tree.HitMatrix(10)

