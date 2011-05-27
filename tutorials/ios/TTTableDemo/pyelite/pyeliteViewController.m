//
//  pyeliteViewController.m
//  pyelite
//
//  Created by dennisli on 3/28/11.
//  Copyright 2011 __MyCompanyName__. All rights reserved.
//

#import "pyeliteViewController.h"
#import "CharacterData.h"
#import "Character.h"

@implementation pyeliteViewController

- (id)initWithNavigatorURL:(NSURL*)URL query:(NSDictionary*)query {
    
    if (self = [super init]) {
        
        self.tableViewStyle = UITableViewStyleGrouped;
        self.title = @"Characters";
        
        TTListDataSource *dataSource = 
        [[[TTListDataSource alloc] init] autorelease];
        
        NSMutableArray *characters = 
        [[CharacterData sharedCharacterData] characters];
        for(int i = 0; i < [characters count]; i++) {
            
            Character *character = (Character *) [characters objectAtIndex:i];
            
            TTTableItem *tableItem = 
            [TTTableSubtitleItem 
             itemWithText:character.name
             subtitle:[NSString stringWithFormat:@"Level %d %@", 
                       character.level, character.rpgClassName]
             URL:[NSString stringWithFormat:@"tt://character/%d", i]];
            
            
            [dataSource.items addObject:tableItem];
        }
        
        self.dataSource = dataSource;
        
    }
    return self;
    
}

@end
