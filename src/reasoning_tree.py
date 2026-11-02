"""
Reasoning Tree and DFS Anomaly Traversal Module.
Demonstrates paper's concept of representing reasoning as a tree and using DFS to backtrack anomalous nodes.
"""
from typing import List, Dict, Any, Optional

class TreeNode:
    def __init__(self, node_id: int, step_text: str, similarity_from_parent: float = 1.0):
        self.node_id = node_id  # 1-indexed step number
        self.step_text = step_text
        self.similarity_from_parent = similarity_from_parent
        self.anomaly_value = 1.0 - similarity_from_parent
        self.is_anomalous = False
        self.children: List['TreeNode'] = []

class ReasoningTree:
    def __init__(self, steps: List[str], step_similarities: List[Dict[str, Any]], threshold: float = 0.40):
        self.steps = steps
        self.similarities = step_similarities
        self.threshold = threshold
        self.root = self._build_tree()
        
    def _build_tree(self) -> TreeNode:
        """
        Builds a sequential reasoning tree from linear step sequence.
        Root node represents prompt/start.
        """
        root = TreeNode(node_id=0, step_text="Root Prompt")
        curr = root
        
        sim_map = {s["curr_step_idx"]: s["similarity"] for s in self.similarities}
        
        for idx, step_text in enumerate(self.steps, start=1):
            sim = sim_map.get(idx, 1.0)
            child = TreeNode(node_id=idx, step_text=step_text, similarity_from_parent=sim)
            curr.children.append(child)
            curr = child
            
        return root

    def dfs_backtracking(self) -> Dict[str, Any]:
        """
        Performs Depth-First Search traversal to identify and backtrack anomalous nodes.
        
        Returns:
            Dict[str, Any]: DFS search summary containing visited_nodes, anomalous_nodes,
                            path_anomaly_score, and final_prediction.
        """
        visited_nodes = []
        anomalous_nodes = []
        
        def _dfs(node: TreeNode):
            if node.node_id != 0:
                visited_nodes.append({
                    "node_id": node.node_id,
                    "step_text": node.step_text,
                    "anomaly_value": float(node.anomaly_value),
                    "similarity": float(node.similarity_from_parent)
                })
                
                if node.anomaly_value >= self.threshold:
                    node.is_anomalous = True
                    anomalous_nodes.append({
                        "node_id": node.node_id,
                        "step_text": node.step_text,
                        "anomaly_value": float(node.anomaly_value),
                        "status": "ANOMALOUS"
                    })
                    
            for child in node.children:
                _dfs(child)
                
        _dfs(self.root)
        
        max_anomaly = max([n["anomaly_value"] for n in visited_nodes]) if visited_nodes else 0.0
        prediction = "PROMPT_INJECTION" if len(anomalous_nodes) > 0 or max_anomaly >= self.threshold else "SAFE"
        
        return {
            "visited_nodes": visited_nodes,
            "anomalous_nodes": anomalous_nodes,
            "path_max_anomaly": float(max_anomaly),
            "final_prediction": prediction
        }
