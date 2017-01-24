//
//  BSTNode.m
//  ObjCPrep
//
//  Created by Colin Conduff on 1/24/17.
//  Copyright © 2017 Colin Conduff. All rights reserved.
//

#import "BSTNode.h"

/**
 Implementation for a node to be used in a binary search tree.
 */
@implementation BSTNode : NSObject

# pragma mark - Initializers

/**
 Designated initializer.
 */
- (instancetype)initWithKey:(int)key
                      value:(int)value
                       left:(BSTNode *)left
                      right:(BSTNode *)right
              sizeOfSubtree:(int)sizeOfSubtree
{
    self = [super init];
    
    if (self) {
        _key = key;
        _value = value;
        _left = left;
        _right = right;
        _sizeOfSubtree = sizeOfSubtree;
    }
    
    return self;
}

/**
 Used to set default values of left, right, and sizeOfSubtree.
 */
- (instancetype)initWithKey:(int)key value:(int)value
{
    return [self initWithKey:key
                       value:value
                        left:nil
                       right:nil
               sizeOfSubtree:1 ];
}

# pragma mark - Description

/**
 Override description with a string of the form "([key], [value])", e.g. "(5, 5)".
 */
- (NSString *)description
{
    return [[NSString alloc] initWithFormat:@"(%i,%i)", self.key, self.value];
}

@end
