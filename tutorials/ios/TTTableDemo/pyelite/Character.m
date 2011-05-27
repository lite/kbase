//
//  Character.m
//  Three20Test
//
//  Created by Ray Wenderlich on 3/9/10.
//  Copyright 2010 Ray Wenderlich. All rights reserved.
//

#import "Character.h"

@implementation Character

@synthesize name = _name;
@synthesize level = _level;
@synthesize xp = _xp;
@synthesize rpgClass = _rpgClass;

- (id)initWithName:(NSString *)name level:(int)level xp:(int)xp rpgClass:(RPGClass)rpgClass {
 
    if ((self = [super init])) {
        
        self.name = name;
        self.level = level;
        self.xp = xp;
        self.rpgClass = rpgClass;
        
    }
    return self;
    
}

- (NSString *)rpgClassName {
    return [[Character sharedRpgClassNames] objectAtIndex:_rpgClass];
}

- (void) dealloc {
    self.name = nil;  
    [super dealloc];
}

#pragma mark Singleton class names

static NSArray *sharedRpgClassNames;

+ (NSArray *)sharedRpgClassNames {
    @synchronized(self)
	{
        if (sharedRpgClassNames == nil)
		{
            sharedRpgClassNames = [[NSArray alloc] initWithObjects:@"Fighter", @"Rogue", @"Wizard", nil];
        }
    }	
    return sharedRpgClassNames;
}

@end
