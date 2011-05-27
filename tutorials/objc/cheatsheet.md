Objective-C cheat sheet
----

Declaring, defining and calling methods
====

### Declaring:
    //in a .h file
    -(id)addObject:(id)object toArray:(NSArray)array; 
        //Method is called addObject:toArray:
        //Takes two arguments, a pointer to an NSObject and a pointer to an NSArray
        //(id is the same as NSObject *)
        //Returns a pointer to an NSObject
        //Is an instance method, not a class/static method (the - means instance.)

### Defining:
    //in a .m file
    -(id)addObject:(id)object toArray:(NSArray *)array{
        //Add the object to the array
    }
### Calling:
    //in the same .m file
    NSArray *arr = [NSArray array];
    NSString *name = @"Nate";
    [self addObject:name toArray:arr];
    
Memory Management
====

    Objective-C has objects and primitives.
    Objects are anything that starts with "NS" or "UI" or is a subclass of one of those
        NSArray, UILabel, Person, Recipe, etc.
    Primitives are numbers, enumerations
        int, NSInteger, UITableViewStylePlain, etc.
    Structures that start with CG or are actually structs (like NSRrange) act like primitives
        NSRange, CGSize, CGRect, etc.
    There are also C structures that are neither objects nor primitives
        sqlite3 *, char *, etc.
    You don't need to worry about memory for primitives.
    C structures have a different memory management scheme
        sqlite3_close, free, etc.
    Objects use a reference-counting scheme.

Reference Counting
====
    Every object has a retainCount.  
    When it's retainCount is zero, it IMMEDIATELY calls its own -dealloc method.
        NSObject's dealloc method actually frees the memory backup, you just have to clear your own variables and call [super dealloc]
    You increase an object's retain count by one by calling -retain on it.
        [obj retain];
    You decrease an object's retain count by one by calling -release on it.
        [obj release];
    If you need an object, it is your responsibility to make sure it is not deallocated, by calling -retain on it.
    When you no longer need it, it is your responsibility to tell it that by calling -release.
    You can also call -autorelease on an object.  This is roughly like saying, "When this current stack of functions complete, call release on yourself."
    There are two main ways of creating new objects: alloc/init, or with static initializers.
    Alloc/init
        NSArray *arr = [[NSArray alloc] init];
    static initializers
        NSArray *arr = [NSArray array];
    Most of the alloc/init initializers also have a static initializer form
    ([][NSArray alloc] initWithObjects] is like [NSArray arrayWithObjects])
    Any object that is returned by a function whose name starts with init or copy is guaranteed to have a retainCount of one, and an autorelease count of 0.  This means that you DO NOT need to retain it to keep it around, but when you're done, you DO need to release it.
    -(id)init {
        //NSArray *arr is declared in our .h
        arr = [[NSArray alloc] init];
        //we can use arr in any of our methods, it won't go away.
    }
    -(void)dealloc {
        [arr release]; //we need to release it
        [super dealloc];
    }

    Any object returned by a function whose names does NOT start with init or copy has a retainCount of 1 AND an autorelease count of 1.  This means that you do not need to release it when you are done with it (because the autorelease count will drop the retainCount to 0 and be deallocated when the current stack of functions complete.)  If you want it to not be freed, you DO need to retain it.
    -(id)init {
        //NSArray *arr is declared in our .h
        arr = [NSArray array];
        [arr retain];  //If we didn't explicitly retain it, it would dealloc after the current functions complete
    }
    -(void)doSomething {
        NSArray *arr2 = [NSArray arrayWithObjects:@"Foo", @"Bar", @"Baz", nil];
        //do stuff with arr2
        //We do NOT need to release arr2, it will be deallocated automatically.
    }
    -(void)dealloc {
        [arr release]; //because we retained it in our init, we need to release it here.
        [super dealloc];
    }

    Remember create retain @properties for a variable
    -(id)init {
        //NSArray *arr and NSDictionary *dict are both given retain @properties in our .h
        self.arr = [NSArray array];
        dict = [[NSDictionary alloc] init];
        //Both arr and dict will NOT be deallocated.
        //Although [NSArray array] returns an object with retainCount of 1 and autorelease count of 1, using the self.arr form invokes our retain property, which increases its retainCount to 2.  When the autorelease pool is drained, it will still have a retainCount of 1, and so not be deallocated.
        //We don't use the self.dict for dict.  Because we are using the alloc/init form, though, the dictionary already has a retainCount of 1 and an autorelease count of 0, so it will be retained.
    }
    -(void)dealloc {
        [arr release];
        [dict release];
        [super dealloc];
    }

    You need to make sure that any object returned by methods that you write have the correct retain and autorelease count.  Remember the convention: any object returned by a method that starts with init or copy needs to be released in the future, and any object returned by a method that does NOT start with init or copy does NOT need to be released.


Common methods
====

### NSString 
    -stringWithUTF8String: //convert from char* string to NSString
    -stringWithFormat: //Uses operators like %@ and %i to print variables
    -length
    -characterAtIndex: //gets single character
    -componentsSeparatedByString: //Splits a string into an array of strings
    -rangeOfString: //Returns location of substring
    -isEqualToString: //tests equality
    -intValue, -doubleValue, etc. //converts string to number

### NSMutableString
    -appendString:
    -deleteCharactersInRange: //remove characters
    -insertString:atIndex: //insert string
    -replaceOccurrencesOfString:withString:options:range: //replace substring
    //NSMutableString *story = @"Nate went to the store";
    //[story replaceOccurrencesOfString:@"Nate" withString:@"Nathan" options:NSLiteralSearch range:NSMakeRange(0, [story length]);
    //story is now "Nathan went to the store"

### NSArray
    -objectAtIndex: //[arr objectAtIndex:3] is the Objective-C equivalent of arr[3] in most languages
    -count
    -containsObject: //See if an object is in an array (uses isEqual:, not pointer comparison)
    -componentsJoinedByString: //Combines the elements of an array into a string, with the passed-in string in between
    //NSString *sentence = [words componentsJoinedByString:@" "];
    -sortedArrayUsingSelector: //Sorts the array
    //NSString *sortedNames = [names sortedArrayUsingSelector:@selector(compare:)];

### NSMutableArray
    -addObject: //adds object to end
    -insertObject:atIndex: //inserts object into the array
    -removeObject: //removes the object
    -removeObjectAtIndex: //removes object at specified object
    -exchangeObjectAtIndex:withObjectAtIndex: //swaps objects at specified indices
    -sortUsingSelector: //like NSArray's sortedArrayUsingSelector, but sorts the array in-place instead of returning a new one.

### NSDictionary
    -dictionaryWithObjects:forKeys: //Takes an NSArray of objects and NSArray of keys
    //NSDictionary *me = [NSDictionary dictionaryWithObjects:[NSArray arrayWithObjects:@"Nate", @"Brown", nil] forKeys:[NSArray arrayWithObjects:@"Name", @"Hair Color", nil]];
    -objectForKey: //After previous line, calling NSLog([me objectForKey:@"Hair Color"]) would print "Brown".  Returns nil if key not in dictionary.  Like calling me["Hair Color"] in most languages.
    -allKeys //Returns an array of all the keys in the dictionary
    -allValues //Returns an array of all the values
    -count //the number of key/value pairs in the dictionary
    
### NSMutableDictionary
    -setObject:forKey:
    //If me were mutable,
    //[me setObject:@"Pizza" forKey:@"Favorite Food"]
    -removeObjectForKey:
    //[me removeObjectForKey:@"Favorite Food"]

Enumeration
====
    You can loop through an array like this:
    int i;
    for (i = 0; i < [arr count]; i++) {
        id obj = [arr objectAtIndex:i];
        //Do something with obj
    }
    The better/faster/easier was is Fast Enumeration, like this:
    for (id obj in arr) {
        //do something with obj
    }
    You can also loop through all the keys in an array in the same way:
    for (id key in dict) {
        id obj = [dict objectForKey:key];
        //do something with key and obj
    
    }