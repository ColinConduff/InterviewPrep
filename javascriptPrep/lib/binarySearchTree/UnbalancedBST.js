#!/usr/bin/env node

"use strict";

class Node {
	constructor(key, value, left=null, right=null, sizeOfSubtree=1) {
		this.key = key;
		this.value = value;
		this.left = left;
		this.right = right;
		this.sizeOfSubtree = sizeOfSubtree;
	}
}

class UnbalancedBST {

	constructor() {
		this._root = null;
	}

	size() {
		return this._size(this._root);
	}

	_size(node) {
		return (node ? node.sizeOfSubtree : 0);
	}

	traversal(traversalType, callback) {
		this._traversal(traversalType, callback, this._root);
	}

	_traversal(traversalType, callback, node) {
		if (!node) return;

		if (traversalType === "pre") 
			callback(node);

		this._traversal(traversalType, callback, node.left);

		if (traversalType === "in") 
			callback(node); 

		this._traversal(traversalType, callback, node.right);

		if (traversalType === "post") 
			callback(node);
	}

	put(key, value) {
		this._root = this._put(key, value, this._root);
	}

	_put(key, value, node) {
		if (!node) { return new Node(key, value); }

		if (key < node.key) {
			node.left = this._put(key, value, node.left);
		} else if (key > node.key) {
			node.right = this._put(key, value, node.right);
		} else {
			node.value = value;
		}

		node.sizeOfSubtree = this._size(node.left) + this._size(node.right) + 1;
		return node;
	}

	remove(key) {
		this._root = this._remove(key, this._root);
	}

	_remove(key, node) {
		if (!node) { return null; }

		if (key < node.key) {
			node.left = this._remove(key, node.left);
		} else if (key > node.key) {
			node.right = this._remove(key, node.right);
		} else {
			if (!node.left) {
				return node.right;

			} else if (!node.right) {
				return node.left;
			
			} else {
				const nodeToDelete = node;
				node = this._floor(key, node.right);
				node.right = this._deleteMin(node.right);
				node.left = nodeToDelete.left;
			}
		}

		node.sizeOfSubtree = this._size(node.left) + this._size(node.right) + 1;
		return node;
	}

	_floor(key, node) {
		if (!node) { return null; }

		if (key < node.key) {
			const leftAttempt = this._floor(key, node.left);
			return (leftAttempt ? leftAttempt : node);
		}
			
		return node;
	}

	_deleteMin(node) {
		if (!node) { return null; }

		if (node.left) {
			node.left = this._deleteMin(node.left);
		} else {
			return node.right;
		}

		node.sizeOfSubtree = this._size(node.left) + this._size(node.right) + 1;
		return node;
	}
}

module.exports = UnbalancedBST;