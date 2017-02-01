describe("linkedLists", function() {
	const linkedListsModule = require('../lib/linkedLists');

	for (let property in linkedListsModule) {
  		const LinkedListSubClass = linkedListsModule[property];

		var linkedList;

		beforeEach(function() {
	    	linkedList = new LinkedListSubClass();
		});

		describe("#insert", function() {
			it("should throw an exception if index is out of bounds", function() {
				expect(function() {
					linkedList.insert(5, -1);
				}).toThrowError("Index Out of Range");

				expect(function() {
					linkedList.insert(5, 1);
				}).toThrowError("Index Out of Range");
			});
		});

		describe("#remove", function() {
			it("should throw an exception if index is out of bounds", function() {
				expect(function() {
					linkedList.insert(5, -1);
				}).toThrowError("Index Out of Range");
				
				expect(function() {
					linkedList.insert(5, 1);
				}).toThrowError("Index Out of Range");
			});
		});

		it("should appendFront", function() {
			linkedList.appendFront(1);

			expect(linkedList.length).toEqual(1);
			expect(linkedList.toArray).toEqual([1]);

			linkedList.appendFront(2);

			expect(linkedList.length).toEqual(2);
			expect(linkedList.toArray).toEqual([2,1]);
	  	});

	  	it("should append", function() {
			linkedList.append(1);
			linkedList.append(2);

			expect(linkedList.length).toEqual(2);
			expect(linkedList.toArray).toEqual([1,2]);
	  	});

	  	it("should popFront", function() {
			linkedList.append(1);
			linkedList.append(2);

			expect(linkedList.popFront()).toEqual(1);
			expect(linkedList.length).toEqual(1);

			expect(linkedList.popFront()).toEqual(2);
			expect(linkedList.length).toEqual(0);
	  	});

	  	it("should popLast", function() {
			linkedList.append(1);
			linkedList.append(2);

			expect(linkedList.popLast()).toEqual(2);
			expect(linkedList.length).toEqual(1);

			expect(linkedList.popLast()).toEqual(1);
			expect(linkedList.length).toEqual(0);
	  	});
	}
});

