#import <Foundation/Foundation.h>  

void test_string()
{
    NSString* str=@"这是一个字符串。";
    NSLog(@"%@", str);
    
    const char *utf8_str = [str UTF8String];
    NSLog(@"%s", utf8_str);
    
    NSString* dup_str = [[[NSString alloc] initWithUTF8String : utf8_str] autorelease];
    NSLog(@"%@ length is %d.", dup_str, [dup_str length]);
    NSLog(@"the 1st character is %C.", [dup_str characterAtIndex: 0]);
    
    NSString* str_fmt = [NSString stringWithFormat : @"%d < %.02f", 3, 300.0];
    NSLog(@"%@", str_fmt);
    
    NSString *list = @"Norman, Stanley, Fletcher, Forlet";
    NSArray *items = [list componentsSeparatedByString:@", "];
    for(NSString* t in items){
        // if([t isEqualToString: @"Forlet"]){
        if([t caseInsensitiveCompare: @"forlet"] == 0){
            NSLog(@"%@, %@ %@", t, t.uppercaseString, t.lowercaseString);   
        }
    }
    
    NSRange range = [list rangeOfString:@"or"];
    NSLog(@"%d, %d", range.location, range.length);
    
    NSString* int_str = @"3000";
    NSString* double_str = @"0.200";
    NSLog(@"%d, %.03f", int_str.intValue, double_str.doubleValue);
    
    NSString *tmp = @"Nate went to the store.";
    NSMutableString* mut_str= [NSMutableString stringWithString:tmp];
    [mut_str appendString: @"How about Nate's sisters?"]; 
    NSLog(@"%@", mut_str);

    [mut_str replaceOccurrencesOfString:@"Nate"
        withString:@"Lite"
        options:NSLiteralSearch
        range:NSMakeRange(0,mut_str.length)];
    NSLog(@"%@", mut_str);
       
    [mut_str insertString:@" and Nate" atIndex:4];
    NSLog(@"%@", mut_str);
    
    [mut_str deleteCharactersInRange: NSMakeRange(0, 9)];
    NSLog(@"%@", mut_str);
}

int main(int argc, const char *argv[])  
{  
    NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];
    
    test_string();

    [pool release];
    return 0; 
}