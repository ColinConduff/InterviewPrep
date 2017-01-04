
fileprivate class Node {
	var key: Int
	var value: Int
	var left: Node?
	var right: Node?
	var sizeOfSubtree: Int
	
	init(key: Int, value: Int, left: Node?=nil, right: Node?=nil, sizeOfSubtree: Int=1) {

		self.key = key
		self.value = value
		self.left = left
		self.right = right
		self.sizeOfSubtree = sizeOfSubtree
	}
}

struct BST {

	fileprivate var root: Node?
	
	init() {}

	var size: Int {
		get { 
			return _size(node: self.root) 
		}
	}

	var description: String {
		get {
			var result = ""
			self._traverse(type: .inorder, node: self.root) {
				node in result += String(node.key)
			}
			return result
		}
	}

	subscript(index: Int) -> Int?  {
	    get {
	        if let node = self._get(key: index, node: self.root) {
	        	return node.value
	        } else {
	        	return nil
	        }
	    }
	    set(newValue) {
	    	if let newValue = newValue { 
	        	self.root = self._put(key: index, value: newValue, node: self.root)
	        } else {
	        	self.root = self._delete(key: index, node: self.root)
	        }
	    }
	}

	func contains(key: Int) -> Bool {
		return _get(key: key, node: self.root) != nil
	}

	private func _size(node: Node?) -> Int {
		guard let node = node else { return 0 }

		return node.sizeOfSubtree
	}

	private func _get(key: Int, node: Node?) -> Node? {

		guard let node = node else { return nil }

		if key < node.key {
			return _get(key: key, node: node.left)
		} else if key > node.key {
			return _get(key: key, node: node.right)
		} else {
			return node
		}
	}

	mutating private func _put(key: Int, value: Int, node: Node?) -> Node {

		guard let node = node else { 
			return Node(key: key, value: value) 
		}

		if key < node.key {
			node.left = _put(key: key, value: value, node: node.left)

		} else if key > node.key {
			node.right = _put(key: key, value: value, node: node.right)
		
		} else {
			node.value = value
		} 

		node.sizeOfSubtree = _size(node: node.left) + _size(node: node.right) + 1
		return node
	}

	mutating private func _delete(key: Int, node: Node?) -> Node? {

		guard var node = node else { return nil }

		if key < node.key {
			node.left = _delete(key: key, node: node.left)

		} else if key > node.key {
			node.right = _delete(key: key, node: node.right)
		
		} else {
			let oldNode = node
			node = _floorNode(key: key, node: oldNode.right)!
			node.right = _deleteMin(node: oldNode.right)
			node.left = oldNode.left
		} 

		node.sizeOfSubtree = _size(node: node.left) + _size(node: node.right) + 1
		return node
	}

	private func _floorNode(key: Int, node: Node?) -> Node? {

		guard let node = node else { return nil }

		if key < node.key {
			return _floorNode(key: key, node: node.left) ?? node
		} else {
			return node
		}
	}

	mutating private func _deleteMin(node: Node?) -> Node? {

		guard let node = node else { return nil }

		if node.left == nil {
			return node.right
		} else {
			node.left = _deleteMin(node: node.left)
		}

		node.sizeOfSubtree = _size(node: node.left) + _size(node: node.right) + 1
		return node
	}

	private enum TraversalType {
		case preorder, inorder, postorder, levelorder
	}

	private func _traverse(type: TraversalType, node: Node?, callback: (Node) -> ()) {
		
		guard let node = node else { return }

		if type == .levelorder {
			_levelOrderTraversal(node: node, callback: callback)
		}

		if type == .preorder {
			callback(node)
		}

		_traverse(type: type, node: node.left, callback: callback)

		if type == .inorder {
			callback(node)
		}

		_traverse(type: type, node: node.right, callback: callback)

		if type == .postorder {
			callback(node)
		}
	}

	private func _levelOrderTraversal(node: Node?, callback: (Node) -> ()) {
		
		guard let node = node else { return }
		
		var currentLevel = [node]
		callback(node)

		while currentLevel.count > 0 {
			var nextLevel = [Node]()

			for currentNode in currentLevel {
				if let leftNode = currentNode.left {
					nextLevel.append(leftNode)
					callback(leftNode)
				} 
				if let rightNode = currentNode.right {
					nextLevel.append(rightNode)
					callback(rightNode)
				}
			}

			currentLevel = nextLevel
		}
	}
}