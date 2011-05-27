#import <Foundation/Foundation.h>  
#import "MethodSwizzling.h"

@interface T1 : NSObject { }
- (void)origMethod;
@end
@implementation T1
- (void)origMethod
{
    NSLog(@"T1 Original method called");
}
@end

@interface T1 (altMethod)
- (void)altMethod;
@end

@implementation T1 (altMethod)
- (void)altMethod
{
    NSLog(@"Alternative method called");
    [self altMethod];
}
@end

void test_md5()
{
    NSString *myString = @"test";
    NSString *md5 = [myString MD5]; // returns NSString of the MD5 of test
    NSLog(md5);  
}

void test_swizzle()
{
    T1 *t = [[[T1 alloc] init] autorelease];
    [t origMethod];

    [T1 swizzleMethod:@selector(origMethod) withMethod:@selector(altMethod)];

    [t origMethod];
}

int main (int argc, const char * argv[])
{
    NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];

    test_md5();
    test_swizzle();

    [pool release];

    return 0;
}
