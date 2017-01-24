//
//  BinarySearchTree.m
//  ObjCPrep
//
//  Created by Colin Conduff on 1/24/17.
//  Copyright © 2017 Colin Conduff. All rights reserved.
//

#import "BinarySearchTree.h"

@implementation BinarySearchTree : NSObject

# pragma mark - Class Methods

+ (instancetype)loadFromFile:(NSString *)fileName
{
    NSString *preOrderTraversal = [NSString stringWithContentsOfFile:[self getFilePath:fileName]
                                                            encoding:NSUTF8StringEncoding
                                                               error:nil];
    return [self buildFrom:preOrderTraversal];
}

/**
 Build a new binary search tree using a string representation of a pre order traversal.
 */
+ (instancetype)buildFrom:(NSString *)preOrderTraversalString
{
    NSArray *array = [self deserializeTraversal:preOrderTraversalString];
    BinarySearchTree *bst = [[self alloc] init];
    
    for (NSDictionary *dictionary in array) {
        NSString *keyString = [dictionary allKeys][0];
        NSNumber *value = dictionary[keyString];
        int key = (int)[keyString integerValue];
        
        [bst put:key value:value.intValue];
    }
    
    return bst;
}

+ (NSArray *)deserializeTraversal:(NSString *)traversal
{
    NSData *jsonData = [traversal dataUsingEncoding:NSUTF8StringEncoding];
    return [NSJSONSerialization JSONObjectWithData:jsonData
                                           options:kNilOptions
                                             error:nil];
}

+ (NSString *)getFilePath:(NSString *)fileName
{
    NSString *filePath = [NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, true) objectAtIndex:0];
    NSString *fileAtPath = [filePath stringByAppendingPathComponent:fileName];
    
    if (![[NSFileManager defaultManager] fileExistsAtPath:fileAtPath]) {
        [[NSFileManager defaultManager] createFileAtPath:fileAtPath contents:nil attributes:nil];
    }
    
    return fileAtPath;
}

# pragma mark - Public Instance Methods

- (int)size
{
    return [self _size:_root];
}

- (nullable NSNumber*)search:(int)key
{
    return [self _search:key node:_root];
}

- (void)put:(int)key
      value:(int)value
{
    _root = [self _put:key value:value node:_root];
}

- (void)remove:(int)key
{
    _root = [self _remove:key node:_root];
}

- (NSArray *)traversal:(TraversalType)type
{
    NSMutableArray *result = [[NSMutableArray alloc] init];
    [self _traversal:type node:_root result:result];
    return result;
}

- (NSString *)serializeTraversal:(TraversalType)type
{
    NSArray *array = [self traversal:type];
    NSData *jsonData = [NSJSONSerialization dataWithJSONObject:array
                                                       options:0
                                                         error:nil];
    return [[NSString alloc] initWithData:jsonData
                                 encoding:NSUTF8StringEncoding];
}

- (void)saveToFile:(NSString *)fileName
{
    NSString *preOrderTraversal = [self serializeTraversal:PreOrderTraversalType];
    [preOrderTraversal writeToFile:[BinarySearchTree getFilePath:fileName]
                        atomically:false
                          encoding:NSUTF8StringEncoding
                             error:nil];
}

- (NSString *)description
{
    return [self serializeTraversal:InOrderTraversalType];
}

# pragma mark - Private Instance Methods

- (int)_size:(BSTNode *)node
{
    if (node) {
        return node.sizeOfSubtree;
    } else {
        return 0;
    }
}

- (nullable NSNumber*)_search:(int)key
                         node:(BSTNode *)node
{
    if (!node) { return nil; }
    
    if (key < node.key) {
        return [self _search:key node:node.left];
    } else if (key > node.key) {
        return [self _search:key node:node.right];
    } else {
        return [NSNumber numberWithInt:node.value];
    }
}

- (BSTNode *)_put:(int)key
            value:(int)value
             node:(BSTNode *)node
{
    if (!node) {
        return [[BSTNode alloc] initWithKey:key value:value];
    }
    
    if (key < node.key) {
        node.left = [self _put:key value:value node:node.left];
    } else if (key > node.key) {
        node.right = [self _put:key value:value node:node.right];
    } else {
        node.value = value;
    }
    
    node.sizeOfSubtree = [self _size:node.left] + [self _size:node.right] + 1;
    
    return node;
}

- (BSTNode *)_remove:(int)key
                node:(BSTNode *)node
{
    if (!node) { return nil; }
    
    if (key < node.key) {
        node.left = [self _remove:key node:node.left];
    } else if (key > node.key) {
        node.right = [self _remove:key node:node.right];
        
    } else {
        if (!node.left) {
            return node.right;
            
        } else if (!node.right) {
            return node.left;
            
        } else {
            BSTNode * oldNode = node;
            node = [self _floorNode:key node:oldNode.right];
            node.right = [self _deleteMin:oldNode.right];
            node.left = oldNode.left;
        }
    }
    
    node.sizeOfSubtree = [self _size:node.left] + [self _size:node.right] + 1;
    
    return node;
}

- (BSTNode *)_floorNode:(int)key
                   node:(BSTNode *)node
{
    if (!node) { return nil; }
    
    if (key < node.key) {
        BSTNode *leftAttempt = [self _floorNode:key node:node.left];
        
        if (leftAttempt) {
            return leftAttempt;
        } else {
            return node;
        }
    } else {
        return [self _floorNode:key node:node.right];
    }
}

- (BSTNode *)_deleteMin:(BSTNode *)node
{
    if (node.left) {
        node.left = [self _deleteMin:node.left];
    } else {
        return node.right;
    }
    
    node.sizeOfSubtree = [self _size:node.left] + [self _size:node.right] + 1;
    
    return node;
}

- (void)_traversal:(TraversalType)type
              node:(BSTNode *)node
            result:(NSMutableArray *) result
{
    if (!node) { return; }
    
    NSString *keyString = [NSString stringWithFormat:@"%i", node.key];
    NSString *valueString = [NSString stringWithFormat:@"%i", node.value];
    
    if (type == PreOrderTraversalType) {
        [result addObject:@{keyString: valueString}];
    }
    
    [self _traversal:type node:node.left result:result];
    
    if (type == InOrderTraversalType) {
        [result addObject:@{keyString: valueString}];
    }
    
    [self _traversal:type node:node.right result:result];
    
    if (type == PostOrderTraversalType) {
        [result addObject:@{keyString: valueString}];
    }
}

@end
