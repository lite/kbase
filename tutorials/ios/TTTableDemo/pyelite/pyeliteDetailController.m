//
//  pyeliteDetailController.m
//  pyelite
//
//  Created by dennisli on 3/28/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "pyeliteDetailController.h"
#import "CharacterData.h"
#import "Character.h"

@implementation pyeliteDetailController

- (id)initWithCharacterIndex:(int)characterIndex {
    
    if (self = [super init]) {
        
        self.tableViewStyle = UITableViewStyleGrouped;
        
        TTListDataSource *dataSource = 
        [[[TTListDataSource alloc] init] autorelease];
        
        NSMutableArray *characters = 
        [[CharacterData sharedCharacterData] characters];
        Character * character = 
        (Character *) [characters objectAtIndex:characterIndex];
        
        self.title = character.name;
        
        [dataSource.items addObject:[TTTableCaptionItem 
                                     itemWithText:character.name
                                     caption:@"Name"
                                     URL:@""]];        
        [dataSource.items addObject:[TTTableCaptionItem 
                                     itemWithText:
                                     [NSString stringWithFormat:@"%d", character.level]
                                     caption:@"Level"
                                     URL:@""]];        
        [dataSource.items addObject:[TTTableCaptionItem 
                                     itemWithText:
                                     [NSString stringWithFormat:@"%d", character.xp]
                                     caption:@"Exp"
                                     URL:@""]];        
        [dataSource.items addObject:[TTTableCaptionItem 
                                     itemWithText:character.rpgClassName
                                     caption:@"Class"
                                     URL:
                                     [NSString stringWithFormat:@"", characterIndex]]];
        
        self.dataSource = dataSource;
        
    }
    return self;
    
}

@end
