//
//  Heap.swift
//  Adapted from Python's Heapq module
//
//  Not used by Dijkstra.swift or Prim.swift (See alt implementation under Graph)
//
//  This implements a min heap.
//  A max heap can be implemented by negating the input and output.

/**
Push an item onto the heap while maintaining the heap invariant.
*/
func heappush(_ heap: inout [Int], item: Int) {
  heap.append(item)
  _siftdown(heap: &heap, startIndex: 0, currentIndex: heap.endIndex - 1)
}

/**
Pop the smallest item off of the heap while maintaining the heap invariant.
*/
func heappop(_ heap: inout [Int]) -> Int? {
    
  guard heap.count > 1 else { return nil }
  guard let lastElement = heap.popLast() else { return nil }

  if heap.count == 0 {
    return lastElement
  
  } else {
    let elementToReturn = heap[0]
    heap[0] = lastElement
    _siftup(heap: &heap, currentIndex: 0)
    
    return elementToReturn
  }
}

/**
Transform the sequence into a heap.

Time complexity: O(n)
Space complexity: O(1)
*/
func heapify(_ sequence: inout [Int]) {
  let end = sequence.endIndex / 2
  for index in (0..<end).reversed() {
    _siftup(heap: &sequence, currentIndex: index)
  }
}

/**
Restores the heap invariant for the current index.

Follows the path to the root while moving parents down until finding a place where the currentItem fits.
*/
fileprivate func _siftdown(heap: inout [Int], startIndex: Int, currentIndex: Int) {
  let currentItem = heap[currentIndex]
  var currentIndex = currentIndex
  
  while currentIndex > startIndex {
    let parentIndex = (currentIndex - 1) / 2 
    let parent = heap[parentIndex]

    guard currentItem < parent else { break }

    heap[currentIndex] = parent
    currentIndex = parentIndex
  }

  heap[currentIndex] = currentItem
}

/**
Find the smallest child's index.
*/
fileprivate func _smallestChildIndex(heap: [Int], currentIndex: Int) -> Int {
  
  let leftChildIndex = 2 * currentIndex + 1
  let rightChildIndex = leftChildIndex + 1
  
  if rightChildIndex < heap.count && heap[rightChildIndex] < heap[leftChildIndex] {
    return rightChildIndex
  } else {
    return leftChildIndex
  }
}

/**
Move the smaller child up until hitting a leaf.
*/
fileprivate func _siftup(heap: inout [Int], currentIndex: Int) {

  var currentIndex = currentIndex
  let startIndex = currentIndex
  let startItem = heap[currentIndex]
  var childIndex = _smallestChildIndex(heap: heap, currentIndex: currentIndex)
  
  while childIndex < heap.count { 
    heap[currentIndex] = heap[childIndex]
    currentIndex = childIndex
    childIndex = _smallestChildIndex(heap: heap, currentIndex: currentIndex)
  }
  
  // The leaf at currentIndex is empty now.  
  // Put startItem there, and bubble it up
  // to its final resting place (by sifting its parents down).
  heap[currentIndex] = startItem
  _siftdown(heap: &heap, startIndex: startIndex, currentIndex: currentIndex)
}
