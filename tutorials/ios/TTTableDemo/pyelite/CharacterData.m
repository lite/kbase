//
//  CharacterData.m
//  Three20Test
//
//  Created by Ray Wenderlich on 3/9/10.
//  Copyright 2010 Ray Wenderlich. All rights reserved.
//

#import "CharacterData.h"
#import "Character.h"

@implementation CharacterData

@synthesize characters = _characters;

- (id)init {
 
    if ((self = [super init])) {
        self.characters = [[[NSMutableArray alloc] init] autorelease];
        
        // Add default characters
        Character *char1 = [[[Character alloc] initWithName:@"Butch" level:1 xp:1000 rpgClass:kRPGClassFighter] autorelease];
        Character *char2 = [[[Character alloc] initWithName:@"Shadow" level:2 xp:2000 rpgClass:kRPGClassRogue] autorelease];
        Character *char3 = [[[Character alloc] initWithName:@"Crak" level:3 xp:3000 rpgClass:kRPGClassWizard] autorelease];
        [self.characters addObject:char1];
        [self.characters addObject:char2];
        [self.characters addObject:char3];
        
    }
    return self;
    
}

- (void) dealloc
{
    self.characters = nil;
    [super dealloc];
}

#pragma mark Singleton

static CharacterData *sharedCharacterData = nil;

+ (CharacterData *) sharedCharacterData
{
    @synchronized(self)
	{
        if (sharedCharacterData == nil)
		{
            sharedCharacterData = [[self alloc] init];
        }
    }
	
    return sharedCharacterData;
}

@end
