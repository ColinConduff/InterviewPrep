
fileprivate class Node {
	var data: Int
	var next: Node?
	var prev: Node?

	init(data: Int, next: Node?=nil, prev: Node?=nil) {
		self.data = data
		self.next = next
		self.prev = prev
	}

	static func == (lhs: Node, rhs: Node) -> Bool {
		return lhs.data == rhs.data
	}

	static func != (lhs: Node, rhs: Node) -> Bool {
		return lhs.data != rhs.data
	}

	static func != (lhs: Node, rhs: Node?) -> Bool {
		return lhs.data != rhs?.data
	}
}

struct CircularlyLinkedList {

	private var head: Node? = nil
	var count = 0
	
	init() { }

	mutating func appendFront(data: Int) {

		self.count += 1

		if let oldHead = self.head {
			self.head = Node(data: data, next: oldHead, prev: oldHead.prev)
			self.head!.prev!.next = self.head
			self.head!.next!.prev = self.head

		} else {
			self.head = Node(data: data)
			self.head!.next = self.head
			self.head!.prev = self.head
		}
	}

	mutating func appendBack(data: Int) {
		appendFront(data: data)
		self.head = self.head!.next
	}

	mutating func popFront() -> Int? {
		
		guard let oldHead = self.head else { return nil }

		if self.count == 1 {
			self.head = nil
		} else {
			self.head = oldHead.next
			oldHead.prev!.next = self.head
			self.head!.prev = oldHead.prev
		}

		self.count -= 1

		return oldHead.data
	}

	mutating func popBack() -> Int? {
		self.head = self.head?.prev
		return popFront()
	}

	mutating func clear() {
		self.head = nil
		self.count = 0
	}

	var description: String {
		get {
			var node = self.head
			let tail = self.head?.prev
			var nodeString = ""

			while let currentNode = node {
				nodeString += String(currentNode.data)

				guard currentNode != tail else { break }

				node = currentNode.next
			}

			return nodeString
		}
	}

	static func == (lhs: CircularlyLinkedList, rhs: CircularlyLinkedList) -> Bool {

		var lhsNode = lhs.head
		var rhsNode = rhs.head

		while !(lhsNode == nil && rhsNode == nil) { 
			if lhsNode == nil && rhsNode != nil || 
				lhsNode != nil && rhsNode == nil || 
				lhsNode! != rhsNode! {
				return false
			}

			lhsNode = lhsNode!.next 
			rhsNode = rhsNode!.next
		}

		return true
	}

	static func == (lhs: CircularlyLinkedList, rhs: [Int]) -> Bool {

		guard lhs.count == rhs.count else { return false }

		var lhsNode = lhs.head

		for data in rhs {
			if lhsNode?.data != data {
				return false
			}
			lhsNode = lhsNode!.next
		}

		return true
	}
}