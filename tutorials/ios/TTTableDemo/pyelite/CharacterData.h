//
//  CharacterData.h
//  Three20Test
//
//  Created by Ray Wenderlich on 3/9/10.
//  Copyright 2010 Ray Wenderlich. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface CharacterData : NSObject {
    NSMutableArray *_characters;
}

@property (nonatomic, retain) NSMutableArray *characters;

+ (CharacterData *) sharedCharacterData;

@end
