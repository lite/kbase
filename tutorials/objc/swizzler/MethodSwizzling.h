#import <Foundation/Foundation.h>

@interface  NSObject(Swizzle) 

+ (BOOL)swizzleMethod:(SEL)origSelector withMethod:(SEL)newSelector;

@end