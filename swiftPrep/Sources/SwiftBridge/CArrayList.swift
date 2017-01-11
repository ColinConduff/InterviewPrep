
import Foundation
import CModule

/**
A wrapper for arrayList.c
*/
class CArrayList {
    private var _ptr: UnsafeMutablePointer<ArrayList>

    var count: Int {
        get {
            return Int(array_length(_ptr))
        }
    }

    init() {
        _ptr = create_array()
    }

    deinit {
        delete_array(_ptr)
    }

    func insert(_ data: Int, atIndex index: Int) {
        array_insert(_ptr, UInt32(index), Int32(data))
    }

    func append(_ data: Int) {
        array_append(_ptr, Int32(data))
    }

    func pop() -> Int {
        return Int(array_pop(_ptr))
    }

    func print() {
        array_print(_ptr)
    }
}