
import Foundation
import CModule

/**
A wrapper for circularBuffer.c
*/
class CCircularBuffer {
    private var _ptr: UnsafeMutablePointer<CircularBuffer>

    var count: Int {
        get {
            return Int(circular_buffer_length(_ptr))
        }
    }

    init(container_size: Int = 16) {
        _ptr = create_circular_buffer(UInt32(container_size))
    }

    deinit {
        delete_circular_buffer(_ptr)
    }

    func enqueue(_ data: Int) {
        enqueue_circular_buffer(_ptr, Int32(data))
    }

    func dequeue() -> Int {
        return Int(dequeue_circular_buffer(_ptr))
    }

    func print() {
        print_circular_buffer(_ptr)
    }
}
