describe("sorting", function() {
  let sorting = require('../lib/sorting');
  let insertionSort = sorting.insertionSort;

  let testCases;

  beforeEach(function() {
  	testCases = [
	  	{observed: [5,4,3,2,1], expected: [1,2,3,4,5]},
	  	{observed: [5,2,3,4,1], expected: [1,2,3,4,5]},
	  	{observed: [], expected: []},
	  	{observed: [1], expected: [1]},
	  ];
  });

  it("(insertion sort) should sort the sequence in ascending order", function() {
	testCases.forEach(function(testCase, _, _) {
		insertionSort(testCase.observed);
		expect(testCase.observed).toEqual(testCase.expected);
	});
  });
});
