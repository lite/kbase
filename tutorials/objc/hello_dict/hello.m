#import <Foundation/Foundation.h>  

void show_dict(NSDictionary* d)
{
    NSLog(@"total count is %d", d.count);
    NSLog(@"keys: %@", [[d allKeys] componentsJoinedByString: @"; "]);
    NSLog(@"vals: %@", [[d allValues] componentsJoinedByString: @"; "]);
}

void test_dict()
{
    NSArray* keys = [NSArray arrayWithObjects:@"Name", @"Hair Color", nil];
    NSArray* vals = [NSArray arrayWithObjects:@"Nate", @"Brown", nil];
    NSMutableDictionary *d = [NSMutableDictionary dictionaryWithObjects:vals forKeys:keys];
    show_dict(d);
    
    NSLog(@"%@", [d objectForKey:@"Hair Color"]);
    
    [d setObject:@"Pizza" forKey:@"Favorite Food"];
    show_dict(d);
    
    [d removeObjectForKey:@"Name"];
    show_dict(d);
}

int main(int argc, const char *argv[])  
{  
    NSAutoreleasePool * pool = [[NSAutoreleasePool alloc] init];
    
    test_dict();

    [pool release];
    return 0; 
}