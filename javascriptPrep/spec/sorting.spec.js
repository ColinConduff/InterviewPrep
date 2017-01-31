describe("sorting", function() {
  const sortingFunctions = require('../lib/sorting');
  let testCases;

  beforeEach(function() {
  	testCases = [
	  	{observed: [5,4,3,2,1], expected: [1,2,3,4,5]},
	  	{observed: [5,2,3,4,1], expected: [1,2,3,4,5]},
	  	{observed: [], expected: []},
	  	{observed: [1], expected: [1]}
	  ];
  });

  for (let property in sortingFunctions) {
  	const sortingFunction = sortingFunctions[property]

	it(`(${sortingFunction.name}) should sort the sequence in ascending order`, function() {
		testCases.forEach(function(testCase) {
			observed = sortingFunction(testCase.observed);

			if (observed !== undefined) {
				expect(observed).toEqual(testCase.expected);
			} else {
				expect(testCase.observed).toEqual(testCase.expected);
			}
		});
	});
  }
});
