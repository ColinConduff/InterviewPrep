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
});

