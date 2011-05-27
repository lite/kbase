#import <Foundation/Foundation.h>  
#import <CommonCrypto/CommonDigest.h>

void test_string_md5()
{
    // Convert and print the MD5 value to the console
    unsigned char md5Buffer[CC_MD5_DIGEST_LENGTH];
    NSMutableString *output = [NSMutableString stringWithCapacity:CC_MD5_DIGEST_LENGTH * 2];
    NSString *str = @"String to convert to MD5";
    int i = 0;

    NSData* hashed = [str dataUsingEncoding:NSUTF8StringEncoding];
    // Create 16 byte MD5 hash value, store in buffer
    CC_MD5([hashed bytes], [hashed length], md5Buffer);

    // Convert unsigned char buffer to NSString of hex values
    for(; i < CC_MD5_DIGEST_LENGTH; i++) {
        [output appendFormat:@"%02x",md5Buffer[i]];
    }
    
    NSLog(@"%@", output);
}

int main(int argc, const char *argv[])  
{  
    NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];
    
    test_string_md5();

    // NSLog(@"Hello, World!");  
    [pool release];
    return 0; 
}