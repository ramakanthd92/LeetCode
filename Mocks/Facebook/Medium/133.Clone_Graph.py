"""
# Definition for a Node.
class Node(object):
    def __init__(self, val = 0, neighbors = []):
        self.val = val
        self.neighbors = neighbors
"""
import collections

class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        
        node_hash_map = collections.defaultdict()
        
        if not node:
            return node
        
        def bfs(node):
            dq = collections.deque()
            dq.append(node)
            visited = set()
            visited.add(node.val)
            cnt = 0
            res_node = None
            while(len(dq) > 0):
                node = dq.popleft()
                #print node.val
                new_node = None
                if node.val not in node_hash_map:
                    new_node = Node(node.val)
                    node_hash_map[node.val] = new_node
                else:
                    new_node = node_hash_map[node.val]
                if not cnt:
                    res_node = new_node
                    cnt+=1
                for nei in node.neighbors:
                    if nei.val not in visited:
                        dq.append(nei)
                        visited.add(nei.val)
                        nei_node = Node(nei.val)
                        node_hash_map[nei.val] = nei_node
                        new_node.neighbors.append(nei_node)
                    else:
                        new_node.neighbors.append(node_hash_map[nei.val])
            
            return res_node
           
        output_node = bfs(node)
        #print node_hash_map
        
        #bfs(output_node)
        
        return output_node
            
            
