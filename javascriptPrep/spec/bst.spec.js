describe("binarySearchTree", function() {
	const binarySearchTreeModule = require('../lib/binarySearchTree');
	const UnbalancedBST = binarySearchTreeModule.UnbalancedBST;

	var bst;

	beforeEach(function() {
    	bst = new UnbalancedBST();
	});

	it("should insert new nodes", function() {
		expect(bst.size()).toEqual(0);

		bst.put(2, 2);
		expect(bst._root.key).toEqual(2);
		expect(bst.size()).toEqual(1);

		bst.put(3, 3);
		expect(bst._root.right.key).toEqual(3);
		expect(bst.size()).toEqual(2);

		bst.put(1, 1);
		expect(bst._root.left.key).toEqual(1);
		expect(bst.size()).toEqual(3);
	});

	it("should update node values", function() {
		bst.put(2, 2);
		expect(bst._root.value).toEqual(2);
		bst.put(2, 3);
		expect(bst._root.value).toEqual(3);
	});

	it("should remove nodes", function() {
		bst.put(2, 2);
		bst.put(3, 3);
		bst.put(1, 1);

		bst.remove(2);
		expect(bst._root.key).toEqual(3);
		expect(bst.size()).toEqual(2);

		bst.remove(1);
		expect(bst._root.left).toEqual(null);
		expect(bst.size()).toEqual(1);

		bst.remove(3);
		expect(bst._root).toEqual(null);
		expect(bst.size()).toEqual(0);
	});

	it("should perform pre, in, and post traversals", function() {
		bst.put(2, 2);
		bst.put(3, 3);
		bst.put(1, 1);

		let data1 = [];

		bst.traversal("pre", (node) => data1.push(node.key));
		expect(data1).toEqual([2,1,3]);

		let data2 = [];

		bst.traversal("in", (node) => data2.push(node.key));
		expect(data2).toEqual([1,2,3]);

		let data3 = [];

		bst.traversal("post", (node) => data3.push(node.key));
		expect(data3).toEqual([1,3,2]);
	});
});

