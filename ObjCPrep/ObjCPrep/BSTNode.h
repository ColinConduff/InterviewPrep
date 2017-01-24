//
//  BSTNode.h
//  ObjCPrep
//
//  Created by Colin Conduff on 1/24/17.
//  Copyright © 2017 Colin Conduff. All rights reserved.
//

#import <Foundation/Foundation.h>

/**
 Interface for a node to be used in a binary search tree.
 */
@interface BSTNode : NSObject

# pragma mark - Properties

@property (nonatomic) int key;

/**
 The value associated with the node's key.
 
 The type of "value" could be replaced with with a generic value.
 */
@property (nonatomic) int value;

/**
 A reference to the current node's left child.
 
 The left child's key should be less than the current node's key.
 */
@property (nonatomic, strong) BSTNode *left;

/**
 A reference to the current node's right child.
 
 The right child's key should be greater than the current node's key.
 */
@property (nonatomic, strong) BSTNode *right;

/**
 The size of the subtree rooted at the current node.
 */
@property (nonatomic) int sizeOfSubtree;

# pragma mark - Initializers

/**
 Designated initializer
 */
- (instancetype)initWithKey:(int)key
                      value:(int)value
                       left:(BSTNode *)left
                      right:(BSTNode *)right
              sizeOfSubtree:(int)sizeOfSubtree;

/**
 Sets default values for left, right, and sizeOfSubtree.
 */
- (instancetype)initWithKey:(int)key value:(int)value;
@end
