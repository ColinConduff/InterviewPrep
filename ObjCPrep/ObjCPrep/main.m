//
//  main.m
//  ObjCPrep
//
//  Created by Colin Conduff on 1/24/17.
//  Copyright © 2017 Colin Conduff. All rights reserved.
//

#import <Foundation/Foundation.h>
#import "BinarySearchTree.h"

int main(int argc, const char * argv[]) {
    @autoreleasepool {
        
        NSArray *values = @[@5, @3, @7, @2, @4, @6, @8];
        
        BinarySearchTree *bst = [[BinarySearchTree alloc] init];
        
        for (NSNumber *value in values) {
            [bst put:value.intValue value:value.intValue];
        }
        
        for (NSNumber *value in values) {
            NSLog(@"searched for %@ found %@", value, [bst search:value.intValue]);
        }
        
        NSString *preOrderTraversal = [bst serializeTraversal:PreOrderTraversalType];
        
        NSLog(@"%@", bst);
        NSLog(@"pre order:%@", preOrderTraversal);
        NSLog(@"post order:%@", [bst serializeTraversal:PostOrderTraversalType]);
        
        NSLog(@"Size %i", [bst size]);
        
        [bst saveToFile:@"binarySearchTree.json"];
        
        BinarySearchTree *bst2 = [BinarySearchTree loadFromFile:@"binarySearchTree.json"];
        
        NSLog(@"bst2: %@", bst2);
        NSLog(@"pre order:%@", [bst2 serializeTraversal:PreOrderTraversalType]);
        NSLog(@"post order:%@", [bst2 serializeTraversal:PostOrderTraversalType]);
        
        [bst remove:5];
        NSLog(@"%@", bst);
        [bst remove:2];
        NSLog(@"%@", bst);
        [bst remove:8];
        NSLog(@"%@", bst);
        [bst remove:4];
        NSLog(@"%@", bst);
        [bst remove:6];
        NSLog(@"%@", bst);
        
        NSLog(@"Size %i", [bst size]);
    }
    return 0;
}
