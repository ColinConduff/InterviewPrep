//
//  Heap.swift
//  Adapted from Python's Heapq module
//
//  Not used by Dijkstra.swift or Prim.swift (See alt implementation under Graph)
//
//  Implements heap and priority queue.

// Tuples do not conform to Comparable, so 
// using a generic type T constrained by Comparable does not work 
// and a struct of type T, along with a closure for comparison, are necessary 
// to enable the heap to function as a priority queue.

// Preferably a struct would not be required

// Heap<(Int, String, String)>(orderedBy: <)

// Heap<(Int, String)>(sequence: [(0, "A")], orderedBy: <)

public struct Heap<T> {

  private var heap: [T] 
  private var compare: (T, T) -> Bool

  /**
  Min priority queue:
  Heap<(Int, String)>(compare: <) { }
  */
  public init(orderedBy: @escaping (T,T) -> Bool) {
    compare = orderedBy
    heap = []
  }

  public init(sequence: [T], orderedBy: @escaping (T,T) -> Bool) {
    compare = orderedBy
    heap = sequence
    heapify(&heap)
  }

  /**
  Push an item onto the heap while maintaining the heap invariant.
  */
  public mutating func push(_ item: T) {
    heap.append(item)
    _siftdown(startIndex: 0, currentIndex: heap.endIndex - 1)
  }

  /**
  Pop the smallest item off of the heap while maintaining the heap invariant.
  */
  public mutating func pop() -> T? {
      
    guard heap.count > 0 else { return nil }
    guard let lastElement = heap.popLast() else { return nil }

    if heap.count == 0 {
      return lastElement
    
    } else {
      let elementToReturn = heap[0]
      heap[0] = lastElement
      _siftup(currentIndex: 0)
      
      return elementToReturn
    }
  }

  public var description: [T] {
    get {
      return heap
    }
  }

  /**
  Transform the sequence into a heap.

  Time complexity: O(n)
  Space complexity: O(1)
  */
  mutating private func heapify(_ sequence: inout [T]) {
    let middleIndex = sequence.endIndex / 2
    for index in stride(from: middleIndex, through: 0, by: -1) {
      _siftup(currentIndex: index)
    }
  }

  /**
  Restores the heap invariant for the current index.

  Follows the path to the root while moving parents down until finding a place where the currentItem fits.
  */
  mutating private func _siftdown(startIndex: Int, currentIndex: Int) {
    let currentItem = heap[currentIndex]
    var currentIndex = currentIndex
    
    while currentIndex > startIndex {
      let parentIndex = (currentIndex - 1) / 2 
      let parent = heap[parentIndex]

      guard compare(currentItem, parent) else { break }

      heap[currentIndex] = parent
      currentIndex = parentIndex
    }

    heap[currentIndex] = currentItem
  }

  /**
  Find the smallest child's index.
  */
  private func _smallestChildIndex(currentIndex: Int) -> Int {
    
    let leftChildIndex = 2 * currentIndex + 1
    let rightChildIndex = leftChildIndex + 1
    
    if rightChildIndex < heap.count && compare(heap[rightChildIndex], heap[leftChildIndex]) {
      return rightChildIndex
    } else {
      return leftChildIndex
    }
  }

  /**
  Move the smaller child up until hitting a leaf.
  */
  mutating private func _siftup(currentIndex: Int) {

    var currentIndex = currentIndex
    let startIndex = currentIndex
    let startItem = heap[currentIndex]
    var childIndex = _smallestChildIndex(currentIndex: currentIndex)
    
    while childIndex < heap.count { 
      heap[currentIndex] = heap[childIndex]
      currentIndex = childIndex
      childIndex = _smallestChildIndex(currentIndex: currentIndex)
    }
    
    // The leaf at currentIndex is empty now.  
    // Put startItem there, and bubble it up
    // to its final resting place (by sifting its parents down).
    heap[currentIndex] = startItem
    _siftdown(startIndex: startIndex, currentIndex: currentIndex)
  }  
}
