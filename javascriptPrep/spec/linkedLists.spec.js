describe("linkedLists", function() {
	const linkedListsModule = require('../lib/linkedLists');
	const SinglyLinkedList = linkedListsModule.SinglyLinkedList;

	var singlyLinkedList;

	beforeEach(function() {
    	singlyLinkedList = new SinglyLinkedList();
	});

	describe("#insert", function() {
		it("should throw an exception if index is out of bounds", function() {
			expect(function() {
				singlyLinkedList.insert(5, -1);
			}).toThrowError("Index Out of Range");

			expect(function() {
				singlyLinkedList.insert(5, 1);
			}).toThrowError("Index Out of Range");
		});
	});

	describe("#remove", function() {
		it("should throw an exception if index is out of bounds", function() {
			expect(function() {
				singlyLinkedList.insert(5, -1);
			}).toThrowError("Index Out of Range");
			
			expect(function() {
				singlyLinkedList.insert(5, 1);
			}).toThrowError("Index Out of Range");
		});
	});

	it("should appendFront", function() {
		singlyLinkedList.appendFront(1);

		expect(singlyLinkedList.length).toEqual(1);
		expect(singlyLinkedList.array).toEqual([1]);

		singlyLinkedList.appendFront(2);

		expect(singlyLinkedList.length).toEqual(2);
		expect(singlyLinkedList.array).toEqual([2,1]);
  	});

  	it("should append", function() {
		singlyLinkedList.append(1);
		singlyLinkedList.append(2);

		expect(singlyLinkedList.length).toEqual(2);
		expect(singlyLinkedList.array).toEqual([1,2]);
  	});

  	it("should popFront", function() {
		singlyLinkedList.append(1);
		singlyLinkedList.append(2);

		expect(singlyLinkedList.popFront()).toEqual(1);
		expect(singlyLinkedList.length).toEqual(1);

		expect(singlyLinkedList.popFront()).toEqual(2);
		expect(singlyLinkedList.length).toEqual(0);
  	});

  	it("should popLast", function() {
		singlyLinkedList.append(1);
		singlyLinkedList.append(2);

		expect(singlyLinkedList.popLast()).toEqual(2);
		expect(singlyLinkedList.length).toEqual(1);

		expect(singlyLinkedList.popLast()).toEqual(1);
		expect(singlyLinkedList.length).toEqual(0);
  	});
});

