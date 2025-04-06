class GraphApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Visualizer")

        # Initialize an empty graph
        self.graph = None

        # Set up the tkinter GUI elements
        self.setup_gui()

    def setup_gui(self):
        # Create Buttons
        self.button_show_example = tk.Button(self.root, text="Show Example Graph", command=self.show_example_graph)
        self.button_show_example.pack(pady=5)

        self.button_show_invented = tk.Button(self.root, text="Show Invented Graph", command=self.show_invented_graph)
        self.button_show_invented.pack(pady=5)

        self.button_load_graph = tk.Button(self.root, text="Load Graph from File", command=self.load_graph_from_file)
        self.button_load_graph.pack(pady=5)

        self.button_select_node = tk.Button(self.root, text="Select Node and Show Neighbors", command=self.select_node)
        self.button_select_node.pack(pady=5)

        # Node name input field for selecting a node
        self.node_name_entry = tk.Entry(self.root)
        self.node_name_entry.pack(pady=5)

        # Create a placeholder for the plot
        self.canvas_frame = tk.Frame(self.root)
        self.canvas_frame.pack(pady=5)

    def plot_graph(self, graph):
        """ Plot the graph using matplotlib """
        fig, ax = plt.subplots(figsize=(8, 6))
        ax.set_title("Graph Visualization")

        # Nodes and edges
        for node in graph.nodes:
            ax.scatter(node.x, node.y, label=node.name, color='blue', zorder=5)
            ax.text(node.x + 0.1, node.y + 0.1, node.name, fontsize=10, zorder=10)

        for segment in graph.segments:
            ax.plot([segment.origin.x, segment.destination.x], [segment.origin.y, segment.destination.y],
                    color='black', linewidth=1)
            midpoint_x = (segment.origin.x + segment.destination.x) / 2
            midpoint_y = (segment.origin.y + segment.destination.y) / 2
            ax.text(midpoint_x + 0.1, midpoint_y + 0.1, f"{segment.cost:.2f}", fontsize=8, color='red')

        ax.set_xlabel("X Coordinate")
        ax.set_ylabel("Y Coordinate")
        ax.set_aspect('equal')

        # Embed the plot into tkinter
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack()

    def show_example_graph(self):
        """ Display the example graph created in CreateGraph_1 """
        self.graph = CreateGraph_1()  # Use the function that returns the graph
        self.plot_raph(self.graph)

    def show_invented_graph(self):
        """ Display a custom graph created by the user """
        # Define a custom graph (You can modify this)
        self.graph = CreateGraph_2()  # Assuming you have CreateGraph_2 defined somewhere
        self.plot_graph(self.graph)

    def load_graph_from_file(self):
        """ Load a graph from a text file and display it """
        filename = filedialog.askopenfilename(title="Select Graph File",
                                              filetypes=(("Text Files", "*.txt"), ("All Files", "*.*")))
        if filename:
            try:
                self.graph = LoadGraphFromFile(filename)  # Load the graph from file
                self.plot_graph(self.graph)
            except Exception as e:
                messagebox.showerror("Error", f"Failed to load graph from file: {e}")

    def select_node(self):
        """ Select a node from the entry field and show its neighbors """
        node_name = self.node_name_entry.get()
        if self.graph:
            # Find the node by name
            node = next((n for n in self.graph.nodes if n.name == node_name), None)
            if node:
                neighbors = [neighbor.name for neighbor in node.neighbors]
                messagebox.showinfo("Neighbors", f"Neighbors of {node_name}: {', '.join(neighbors)}")
            else:
                messagebox.showwarning("Node Not Found", f"Node {node_name} not found in the graph.")
        else:
            messagebox.showwarning("No Graph Loaded", "Please load or create a graph first.")


# Run the tkinter application
if __name__ == "__main__":
    root = tk.Tk()
    app = GraphApp(root)
    root.mainloop()
