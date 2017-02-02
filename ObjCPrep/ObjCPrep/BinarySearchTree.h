//
//  BinarySearchTree.h
//  ObjCPrep
//
//  Created by Colin Conduff on 1/24/17.
//  Copyright © 2017 Colin Conduff. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "BSTNode.h"

@class BinarySearchTree;

/**
 Used for specifying the type of traversal (pre-, in-, or post-).
 */
typedef NS_ENUM(NSUInteger, TraversalType)
{
    PreOrderTraversalType,
    InOrderTraversalType,
    PostOrderTraversalType
};

/**
 Interface for a binary search tree.
 */
@interface BinarySearchTree : NSObject {
    /**
     Private reference to the root of the tree.
     */
    BSTNode *_root;
}

# pragma mark - Class Methods

+ (nullable instancetype)loadFromFile:(nonnull NSString *)fileName;

/**
 Creates a new binary search tree by deserializing a string.
 
 @param preOrderTraversalString String obtained from a pre order traversal of a binary search tree.
 */
+ (nonnull instancetype)buildFrom:(nonnull NSString *)preOrderTraversalString;

/**
 Deserialize a JSON string into a dictionary.
 
 May return nil if an error occurs.
 */
+ (nullable NSArray *)deserializeTraversal:(nonnull NSString *)traversal;

# pragma mark - Instance Methods

/**
 Returns the size of the tree in O(1) time.
 */
- (int)size;

/**
 Recursively search for the value associated with the key.
 
 @return If found, NSNumber containing "value".  Otherwise, nil.
 */
- (nullable NSNumber *)search:(int)key;

/**
 Insert a new node with "key" and "value" into the tree, or update the "value" of an existing node.
 */
- (void)put:(int)key value:(int)value;

/**
 Delete the node containing the given key.
 */
- (void)remove:(int)key;

/**
 Perform pre order, in order, or post order traversal on the tree.
 */
- (nonnull NSArray *)traversal:(TraversalType)type;

/**
 Serialize the traversal to a JSON string.
 
 May return nil if an error occurs.
 */
- (nullable NSString *)serializeTraversal:(TraversalType)type;

- (void)saveToFile:(nonnull NSString *)fileName;

@end
